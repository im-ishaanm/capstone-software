
#include <Servo.h>
Servo myservo;
int pos=0; 
class stepper{ 
  public:
    int DIR,PUL,ENA;
    stepper(int a,int b,int c){
      ENA=a;
      DIR=b;
      PUL=c;
    }

    void set_mode(){
      pinMode(ENA,OUTPUT);      
      pinMode(DIR,OUTPUT);
      pinMode(PUL,OUTPUT);
    }

    void reverse(int steps,int DELAY){
      int i;
      digitalWrite(ENA,LOW);           //ENABLE IS ACTIVE LOW
      digitalWrite(DIR,LOW);          //SET DIRECTION
    
      for(i=0;i<steps;i++){
        digitalWrite(PUL,HIGH);
        delayMicroseconds(DELAY);
        digitalWrite(PUL,LOW);
        delayMicroseconds(DELAY);
      }
    }

    void forward(int steps,int DELAY){
      int i;
      digitalWrite(ENA,LOW);           //ENABLE IS ACTIVE LOW
      digitalWrite(DIR,HIGH);          //SET DIRECTION
    
      for(i=0;i<steps;i++){
        digitalWrite(PUL,HIGH);
        delayMicroseconds(DELAY);
        digitalWrite(PUL,LOW);
        delayMicroseconds(DELAY);
      }
    }
};

stepper double_mot(48,50,52), threerdmotor(38,40,42), gear_boi(28,30,32), nema14(22,24,26), base(7,8,9);
void setup() {

  myservo.attach(10);
  nema14.set_mode();
  threerdmotor.set_mode();
  gear_boi.set_mode();
  base.set_mode();
  double_mot.set_mode();
}

void loop() {
  gear_boi.reverse(16000,200);
  delay(1000);
  double_mot.reverse(3000,500);
  delay(1000);
  gear_boi.forward(30000,200);
  delay(1000);
  nema14.reverse(3000,400);
  delay(4000);
  for (pos=0;pos<=180;pos+=1)
  {
    myservo.write(pos);
    delay(15);
  }
  delay(1000);
  gear_boi.reverse(30000,200);
  delay(1000);
  gear_boi.reverse(5000,200);
  delay(1000);
  double_mot.forward(5000,500);
  delay(1000);
  base.forward(8000,300);
  delay(1000);
  nema14.forward(5000,400);
  delay(1000);
  for (pos=0;pos<=180;pos+=1)
  {
    myservo.write(pos);
    delay(15);
  }
  delay(1000);
}
