from time import localtime, strftime
from csv import writer, reader

from .classes import StoreResponse, Request
from .constants import FETCH_URL, API_KEY, UPDATE_URL        


# Returns the LOCAL date and time in the following format:
# "YEAR-MONTH-DAY HOURS:MINUTES" The formatting can be changed
# below. For reference to the codes, visit: https://strftime.org/
def getDateAndTime():
    # If you wish to convert the time format from
    # LOCAL time to UTC time, replace localtime() with gmtime().
    current_time = strftime("%Y-%m-%d %H:%M", localtime())
    return current_time


def printRequestQueue(queue):
    for req in queue:
        print(req.data, req.request_type)
    
    print("\n")


def removeDuplicatesFromQueue(REQUEST_QUEUE):
    printRequestQueue(REQUEST_QUEUE)
    printRequestQueue(list(set(REQUEST_QUEUE)))
    return list(set(REQUEST_QUEUE))


def updateStore(sampleId, request_type):
    data_cols = [sampleId, request_type]

    with open('local_store.csv', 'a', newline="") as file_obj:
        writer_obj = writer(file_obj)
        writer_obj.writerow(data_cols)

        file_obj.close()

def isStoreEmpty():
    with open('local_store.csv') as csvfile:
        read = reader(csvfile)
        for i, _ in enumerate(read):
            if i:  # found the second row
                return False
    return True


def fetchAllFromStore():
    csv_obj = reader(open('local_store.csv', 'r'), delimiter=',')
    data = []
    for row in csv_obj:
        req = Request(row[0])
        req.set_type(row[1])

        data.append(req)
    
    return data  


def doesStoreHaveID(sampleId):
    csv_obj = reader(open('local_store.csv', 'r'), delimiter=',')

    for row in csv_obj:
        if sampleId == row[0]:
            return True
    
    return False

def searchStore(sampleId, req_type):
    csv_obj = reader(open('local_store.csv', 'r'), delimiter=',')

    for idx, row in enumerate(csv_obj):
        if sampleId == row[0] and req_type == row[1]:
            return StoreResponse(sampleId, req_type, idx, True)
    
    return StoreResponse(sampleId, req_type, None, False) 


def deleteFromStore(pos):
    lines = []
    csv_obj = reader(open('local_store.csv', 'r'), delimiter=',')

    for idx, row in enumerate(csv_obj):
        if idx != pos:
            lines.append(row)

    with open('local_store.csv', 'w', newline='') as writeFile:
        w = writer(writeFile)
        w.writerows(lines)


def emptyLocalStore():
    # opening the file with w+ mode truncates the file
    f = open('local_store.csv', "w+")
    f.close()

