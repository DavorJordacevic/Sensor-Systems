
// Joystick var
int sX = A0;     //joystick x axis, analog input
int sY = A1;     //joystick y axis, analog input
int sSX;         //state of x, reading from sX
int sSY;         //state of y, reading from sY
int sS;          //converted state

void setup() {

  pinMode(sX, INPUT);
  pinMode(sY, INPUT);

  Serial.begin(9600);
}

void loop() {

  //stick stuff
  sSX = analogRead(sX); //reading x axis input
  delay(100);
  sSY = analogRead(sY); //reading y axis input

  //converting y and x inputs to 4 possibilities. 0 and 1023 are the maximum values on each axis of the joystick
  sS=0;
  switch (sSX) {
    case 0:
          sS=1;      // Left
          Serial.print(sS);
          Serial.print(";");
          break;
    case 1023:
          sS=2;      // Right
          Serial.print(sS);
          Serial.print(";");
          break;
  }
  switch (sSY) {
    case 0:
          sS=3;      // Up
          Serial.println(sS);
          break;
    case 1023:
          sS=4;      // Down
          Serial.println(sS);
          break;
  }
}