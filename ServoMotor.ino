#include <Servo.h>
#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int potPin = 0;
int pos = 0;
Servo servo_9;

char angle[7];

void setup()
{
  lcd.begin(16, 2);
  servo_9.attach(9);
  lcd.print("hello, world!");
}

void loop()
{
  int var = analogRead(potPin);
  var = map(var,0,1023,0,180); 
  servo_9.write(var);
  lcd.setCursor(0, 1);
  dtostrf(var,3,3, angle);
  lcd.print(angle);
}
