from distutils.debug import DEBUG
import json
import asyncio
import aiohttp


from .constants import API_KEY, FETCH_URL, UPDATE_URL
from .classes import Request, Response, Debugger
from .misc import emptyLocalStore, getDateAndTime, printRequestQueue, removeDuplicatesFromQueue, updateStore, isStoreEmpty, fetchAllFromStore

REQUEST_QUEUE = []
DEBUG_FLAG = True

async def send_request(session, request):

    d = Debugger(DEBUG_FLAG)

    if request.is_fetch():
        document_body = {
            "SampleId" : request.data,
            "BatchNo":"" ,
            "apikey": API_KEY
        }
    else:
         document_body = {
            "SampleId": request.data,
            "BatchNo": "",
            "ReceiveDate": getDateAndTime(),
            "apikey": API_KEY
        }       

    try:
        d.debug("? Attemping to {} ID {}".format(request.request_type, request.data))
        async with session.post(request.url, data = document_body) as resp:
            return_data = await resp.text()
            response = Response(request.data, json.loads(return_data), request.url, "SUCCESS", request.request_type)
            return response
        # Catch HTTP errors/exceptions here
    except Exception as e:
        d.debug("! Could not {} data: {}".format(request.request_type, e))
        return Response(request.data, {}, request.url, "FAILURE", request.request_type)


async def fetch_concurrent():

    d = Debugger(DEBUG_FLAG)

    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession() as session:
        tasks = []

        for request in REQUEST_QUEUE:
            tasks.append(loop.create_task(send_request(session, request)))


        # for item in urls:
        #     tasks.append(loop.create_task(send_request(session, item)))

        for result in asyncio.as_completed(tasks):
            res = await result

            for index, request in enumerate(REQUEST_QUEUE):

                if res.is_matching_request(request):
                    original_req = request
                    del REQUEST_QUEUE[index]

            try:
                if res.is_success():
                    data = res.data
                    # print(data["StatusMessage"], res.id, res.request_type)
                    d.debug("> {} {} {}".format(data["StatusMessage"], res.id, res.request_type))
                        
                    if res.is_fetch():
                        update_req = Request(res.id)
                        update_req.set_update_type()
                        REQUEST_QUEUE.append(update_req)

                        extractDataFromFetch(data['Data'], res.id, res.request_type)
            
                else:
                    updateStore(original_req.data, original_req.request_type)
                    # LOCAL_STORE.append(original_req)
            
            except Exception as e:
                d.debug("! Error processing Data: {}".format(e))
                updateStore(original_req.data, original_req.request_type)


def processSample(sampleId):

    d = Debugger(DEBUG_FLAG)

    sample = Request(sampleId)
    sample.set_fetch_type()
    REQUEST_QUEUE.append(sample)

    if isStoreEmpty():
        d.debug("! Localstore is Empty")
    else:
        # Append request queue with all pending requests from local store.
        store_values = fetchAllFromStore()
        REQUEST_QUEUE.extend(store_values)        
        
        globals()['REQUEST_QUEUE'] = removeDuplicatesFromQueue(REQUEST_QUEUE)
        emptyLocalStore()
    
    asyncio.run(fetch_concurrent())


def cleanUpRequests():

    d = Debugger(DEBUG_FLAG)
    
    if isStoreEmpty():
        # fill up queue with any pending requests
        pass
        # d.debug("! Localstore is Empty")
        
    else:
        store_values = fetchAllFromStore()
        REQUEST_QUEUE.extend(store_values)
        emptyLocalStore()

    asyncio.run(fetch_concurrent())


def extractDataFromFetch(data, requested_id, extra = ""):
    d = Debugger(DEBUG_FLAG)
    required_data = [sample for sample in data if sample["BarcodeId"] == requested_id][0]
    d.output("{} {} | Tests: {} {}".format(required_data['Title'], required_data['Name'], len(required_data['TestList']), extra))



def setDebug(b = True):
    globals()['DEBUG_FLAG'] = b

    







