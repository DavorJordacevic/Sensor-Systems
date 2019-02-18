// defines pins numbers
const int buzzpin = 6;
const int trigPin = 4;
const int echoPin = 5;
int ledPin1 = 7;
int ledPin2 = 8;
long duration;
int distance;

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzpin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int value = calculate();
  if ( distance < 20){
    tone(buzzpin, 1000);
    digitalWrite(ledPin1,HIGH); 
    digitalWrite(ledPin2,HIGH); 
    delay(10); 
    noTone(buzzpin);
    digitalWrite(ledPin1,LOW);
    digitalWrite(ledPin2,LOW); 
    delay(10);   
  }
  else if (distance < 50){
    tone(buzzpin, 1000); 
    digitalWrite(ledPin2,HIGH);
    delay(100); 
    noTone(buzzpin);
    digitalWrite(ledPin2,LOW);
    delay(100); 
  }
  else if (distance < 100){
    tone(buzzpin, 1000); 
    delay(200); 
    noTone(buzzpin);
    delay(200); 
  }
  else {
    noTone(buzzpin);
  }
}

int calculate(){
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance= duration*0.034/2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);
  return distance;
}
