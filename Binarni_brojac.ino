int ledPin[] = {2,3,4,5};
int delay_time = 500;
//const int buttonPin1 = 6;
//const int buttonPin2 =  7;
//int buttonState1 = 0;
//int buttonState2 = 0;

void  setup()
{

  //pinMode(buttonPin1,INPUT);
  //pinMode(buttonPin2,INPUT);
  
  for (int i =0;i<4;i++)
  {
    pinMode(ledPin[i], OUTPUT);
    digitalWrite(ledPin[i],LOW);
  }
}

void convertToBinary(unsigned int n)
{
    if (n % 2 == 1) {
        digitalWrite(ledPin[3], HIGH);
    }else{
        digitalWrite(ledPin[3], LOW);
    }
    n = n/2 ;
    if (n % 2 == 1) {
        digitalWrite(ledPin[2], HIGH);
    }else{
        digitalWrite(ledPin[2], LOW);
    }
    n = n/2 ;
    if (n % 2 == 1) {
        digitalWrite(ledPin[1], HIGH);
    }
    else{
        digitalWrite(ledPin[1], LOW);
    }
    n = n/2 ;
    if (n % 2 == 1) {
        digitalWrite(ledPin[0], HIGH);
    }else{
        digitalWrite(ledPin[0], LOW);
    }
 }

void loop() 
{
  for(int i = 1; i < 16; i++){
    //checkButton();
    convertToBinary(i); 
    delay(delay_time);   
  }
}

/*
void checkButton(){
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);

  if (buttonState1 == HIGH) {
    delay_time= delay_time * 2;
  }else if (buttonState2 == HIGH) {
    delay_time= delay_time / 2;
  }    
}
*/
