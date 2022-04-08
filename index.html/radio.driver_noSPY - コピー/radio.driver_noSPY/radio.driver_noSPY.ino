
const int PIN_right_go = 2;
const int PIN_right_back = 3;
const int PIN_left_go = 4;
const int PIN_left_back = 5;
const int PIN_STBY = 13;
 
void setup() 
  {
    pinMode(PIN_right_go,OUTPUT);
    pinMode(PIN_left_go,OUTPUT);
    pinMode(PIN_right_back,OUTPUT);
    pinMode(PIN_left_back,OUTPUT);
    pinMode(PIN_STBY,OUTPUT);

  }

void loop() 
  {
    digitalWrite(PIN_STBY,HIGH);
               
    digitalWrite(PIN_right_go,HIGH);
    digitalWrite(PIN_left_go,HIGH);
    delay(100);
            
    digitalWrite(PIN_right_back,HIGH);
    digitalWrite(PIN_left_back,HIGH);
    delay(100);
            
    digitalWrite(PIN_right_go,HIGH);
    digitalWrite(PIN_left_back,HIGH);
    delay(100);
     
    digitalWrite(PIN_right_back,HIGH);
    digitalWrite(PIN_left_go,HIGH);
    delay(100);
       
  }

  
