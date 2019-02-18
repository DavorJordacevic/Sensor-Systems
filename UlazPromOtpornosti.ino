int ledPin=13;
int analogPin=0;
void setup()
{}

void loop()
{
  for(int i =0;i<=255;i++){
    analogWrite(ledPin,i);
    delay(delayVal());
  }
   for(int i =255;i>=0;i--){
    analogWrite(ledPin,i);
    delay(delayVal());
   }
}

int delayVal(){
  int v;
    v = analogRead(analogPin);
    v=v/8;
    return v;
}
