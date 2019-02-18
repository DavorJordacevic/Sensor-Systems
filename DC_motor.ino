int outPin = 5 ;

void setup()
{
  pinMode(5, OUTPUT);
}

void loop()
{
  for(int i=0;i<5;i++){
    digitalWrite(outPin,HIGH);
    delay(250);
    digitalWrite(outPin,LOW);
    delay(250);
  }
  delay(1000);
}
