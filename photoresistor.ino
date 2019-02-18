int pResistor = A0;
int ledPin1 = 10;
int ledPin2 = 9;
int ledPin3 = 8;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin1,OUTPUT);
  pinMode(ledPin2,OUTPUT);
  pinMode(ledPin3,OUTPUT);
  pinMode(pResistor,INPUT);
}

void loop() {
  int value = analogRead(pResistor);
  Serial.println(value);
  Serial.println("\n");
  int writeValue= map(value,0,1023,0,255);
  if (value < 45){
    digitalWrite(ledPin1,HIGH);
    digitalWrite(ledPin2,HIGH);
    digitalWrite(ledPin3,HIGH); 
  }
  else if (value>=45 && value<150){
    digitalWrite(ledPin1,HIGH);
    digitalWrite(ledPin2,HIGH);
    digitalWrite(ledPin3,LOW);
  }
  else if(value>=150 && value<256){
    digitalWrite(ledPin1,HIGH);
    digitalWrite(ledPin2,LOW);
    digitalWrite(ledPin3,LOW);  
  }
  else{
    digitalWrite(ledPin1,LOW);
    digitalWrite(ledPin2,LOW);
    digitalWrite(ledPin3,LOW);   
  }
}
