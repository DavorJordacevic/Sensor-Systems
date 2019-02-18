int potPin = 0;
void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int var = analogRead(potPin);
  Serial.println("\n\nStart:");
  Serial.print(var);
  digitalWrite(13, HIGH);
  delay(var);
  digitalWrite(13, LOW);
  delay(var);
  Serial.println("\n\nend:");
  Serial.print(var);
}
