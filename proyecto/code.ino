/**
 * Nombre: Proyecto.ino
 * objetivo: leer multiples sensores utilizando arduino y python
 * autoor: Ernesto Velasco
 * Fecha: 29/08/2018
 */

#include <DHT.h>
#define DHTPIN 7
#define DHTYPE DHT11
DHT dht (DHTPIN,DHTYPE);

// Puertos actuadores
int p13Led = 13;
int p12Motor =12;
// Puertos para los sensores
int p7TemHum = 7;
int p5Gas = 5;

void setup() {
  // Salida
  pinMode(p13Led, OUTPUT);
  pinMode(p12Motor, OUTPUT);
  
  // Entrada
  pinMode(p7TemHum, INPUT);
  pinMode(p5Gas, INPUT);

  // Analogicos
  pinMode(A0, INPUT);//LM35
  pinMode(A1, INPUT);//Intenciddad luminosa
  // Activar puerto serie
  Serial.begin(9600);
  // Inicializamos el sensor dht11
  dht.begin();
}

void loop() {
  // Leer sensores
  if (Serial.available()>0){
    char cad = Serial.read();
    //Leer temperatura lm35
    if (cad == 't'){
      Serial.println(getTemperatura());
    }
    // Leer Humedad dht11
    else if (cad == 'h'){
      Serial.println(getHumidity());
    }
    // Leer luminosidad fotosensor
    else if (cad == 'f'){
      Serial.println(getLuminosidad());
    }
    // Leer Gas mq3
    else if (cad == 'g'){
      detectaGas();
    }
    // Encender LED
    else if (cad == 'l'){
      encenderLed();
    }
    // Encender MOTOR
    else if (cad == 'm'){
      enciendeMotor();
    }
    // Leer todos los sensores
    else if (cad == 'd'){
      datos();
    }
  }
}

// Funcion para leer el puerto A0 del LM35
float getTemperatura(){
  float grados = 0.0;
  float valor = 0.0;
  valor = analogRead(A0);
  grados = float(valor * 500/1024);
  return grados;
}
// Funcion para el sensor de humedad - dht11
float getHumidity(){
  float h = dht.readHumidity();
  return h;
}
// Funcion para el sensor de luminosidad - fotoresistencia
int getLuminosidad(){
  int vl = analogRead(A1);
  return vl;
}
// Funcion para detectar gas con el sensor mq9
void detectaGas(){
  if (digitalRead(p5Gas)==HIGH){
    Serial.println("Detectado");
  }
  else{
    Serial.println("Libre");
  }
}
// Funcion para encender un led
void encenderLed(){
  if(digitalRead(p13Led) == HIGH){
    digitalWrite(p13Led, LOW);
  }
  else{
    digitalWrite(p13Led, HIGH);
  }
}
// Funcion para encender el motor
void enciendeMotor(){
  if(digitalRead(p12Motor)==HIGH){
    digitalWrite(p12Motor, LOW);
  }
  else{
    digitalWrite(p12Motor,HIGH);
  }
}
// Leer todos los sensores
void datos(){
  Serial.print(getTemperatura());
  Serial.print("\t");
  Serial.print(getHumidity());
  Serial.print("\t");
  Serial.print(getLuminosidad());
  Serial.println();
}
