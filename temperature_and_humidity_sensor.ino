#include <DHT.h>

#define DHTYPE DHT11

const int DHTPin = 7;
DHT dht(DHTPin, DHTTYPE);
static char celsiusTemp[7];
static char fahrenheitTemp[7];
static char humidityTemp[7];

void setup() {
  Serial.begin(9600);
  dht.begin()
}

void loop() {
  Serial.println();

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    strcpy(celsiusTemp,"Failed");
    strcpy(fahrenheitTemp, "Failed");
    strcpy(humidityTemp, "Failed");    
  }else{
    float hic = dht.computeHeatIndex(t, h, false);       
    dtostrf(hic, 6, 2, celsiusTemp);             
    float hif = dht.computeHeatIndex(f, h);
    dtostrf(hif, 6, 2, fahrenheitTemp);         
    dtostrf(h, 6, 2, humidityTemp);    

    println("CelsiusTemp:",celsiusTemp);
    println("FahrenheitTemp:",fahrenheitTemp);
    println("Humidity:",humidity);
  }
