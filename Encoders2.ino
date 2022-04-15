#include <Wire.h>

const byte ledPin = 13;

const byte enc0 = 22;
const byte enc0B =26;


volatile byte state = LOW;
volatile int  offset = 500000;
volatile unsigned int encoder0Pos = 0;


volatile unsigned int demandA = 0;


int a =0;
int r =0;
int mspeed = 0;
int pconst = 2;
int minspeed = 30;
int error =0;

String serialResponse = "";
char sz[] = "Here; is some; sample;100;data;1.414;1020";
String num = "";

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(enc0, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(enc0), count0, CHANGE);
  pinMode(enc0B, INPUT_PULLUP);

  
 Serial.begin(9600);//9600

encoder0Pos = offset;

}

void loop() {

printenc();    
  }

//


  
void count0(){
 if (digitalRead(enc0) == HIGH) {  
    if(digitalRead(enc0B) == LOW){
      encoder0Pos = encoder0Pos + 1;
    }
    else
    {
      encoder0Pos = encoder0Pos - 1;
    }
}
 if(digitalRead(enc0) == LOW){
    if(digitalRead(enc0B) == LOW){
      encoder0Pos = encoder0Pos - 1;
    }
    else
    {
      encoder0Pos = encoder0Pos + 1;
    }
 }
 //Serial.println(encoder0Pos,DEC);
}



void printenc(){
// Serial.print(millis());
//Serial.print(" ");
Serial.print(encoder0Pos);
Serial.println(" ");

}


void reset(){

encoder0Pos = 0; 

}
