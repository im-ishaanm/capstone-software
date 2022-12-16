
#include <Servo.h>
Servo myservo;                        //object of class servo
int pos=0;                            //initial position of the servo motor
class stepper{                        //Class managing all stepper motors
  public:
    int DIR,PUL,ENA;
    stepper(int a,int b,int c){      //Constructor for defining pin numbers to ENA DIR and PUL
      ENA=a;
      DIR=b;
      PUL=c;
    }

    void set_mode(){                 //method for setting all pins to output mode
      pinMode(ENA,OUTPUT);      
      pinMode(DIR,OUTPUT);
      pinMode(PUL,OUTPUT);
    }

    void reverse(int steps,int DELAY){  //method to move motor in anticlockwise direction
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

    void forward(int steps,int DELAY){  //method to movet the motor in clockwise direction
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

stepper nema23(48,50,52), wrist_rotation(38,40,42), gearbox_nema17(28,30,32), nema14(22,24,26), base(7,8,9);   //objects of class stepper for each motor
void setup() {

  myservo.attach(10);              //set pin for servo motor
  nema14.set_mode();
  wrist_rotation.set_mode();
  gearbox_nema17.set_mode();
  base.set_mode();
  nema23.set_mode();
}

void loop() {
  gearbox_nema17.reverse(16000,200);
  delay(1000);
  nema23.reverse(3000,500);
  delay(1000);
  gearbox_nema17.forward(30000,200);
  gearbox_nema17.forward(4000,200);
  delay(1000);
  nema14.reverse(3000,400);
  delay(1000);
  for (pos=0;pos<=180;pos+=1)
  {
    myservo.write(pos);
    delay(15);
  }
  delay(1000);
  gearbox_nema17.reverse(30000,200);
  gearbox_nema17.reverse(10000,200);
  delay(1000);
  nema23.forward(5000,500);
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
  base.reverse(7000,300);
  delay(1000);
  nema23.reverse(2100,300);
  delay(1000);
  gearbox_nema17.forward(16000,300);
  delay(1000);
}
