
#include <Servo.h>  // servo library
#include "SparkFunLIS3DH.h"
#include "Wire.h"
#include "SPI.h"

const int pinTrigger = 11;
const int pinEcho = 12;
const int pinLed = 13;

const int pinPan = 3;
const int pinTilt = 4;

const int ktir1 = A3;
const int ktir2 = A6;
const int ktir3 = A7;

Servo pan;
Servo tilt;

LIS3DH myIMU; //Default constructor is I2C, addr 0x19.

// LIS3DH Hardware connections:
// Connect I2C SDA line to A4
// Connect I2C SCL line to A5
// Connect GND and 3.3v power to the IMU

// ------------------------------------ main ------------------------------------------

// the loop function runs over and over again forever
void loop() {
   readData();
}

// Input:         'device:device_specific_data;'
// Led:           '0:{state};' on - 1, off - 0
// Ultrasonic:    '1;'
// Servo:         '2;{device}:{position}' pan - 0, tilt - 1
// Accelerometer: '3;'
// ktir:          '4;'
void readData() {
  const String data = Serial.readStringUntil(';');
   if (data != "") {
     const int device = getValue(data, ':', 0);
     switch(device) {
        case 0:
          processLed(data);
          break;
        case 1:
          processUltrasonicSensor();
          break;
        case 2:
          processServo(data);
          break;
        case 3:
          processAccelerometer();
          break;
        case 4:
          processKtir();
          break;
      }
   }
}

void processLed(const String& data) {
  getValue(data, ':', 1) ? turnLedOn() : turnLedOff();
}

void processUltrasonicSensor() {
  sendUltrasonicDistance();
}

void processServo(const String& data) {
  getValue(data, ':', 1) ? processPan(data) : processTilt(data);
}

void processPan(const String& data) {
  setPanPosition(getValue(data, ':', 2));
}

void processTilt(const String& data) {
  setTiltPosition(getValue(data, ':', 2));
}

void processAccelerometer() {
  sendAccelerometerData();
}

void processKtir() {
  sendKtirData();
}

int getValue(const String& data, char separator, int index) {
  int found = 0;
  int indexStart = 0;
  int indexStop = -1;
  const int maxIndex = data.length() - 1;

  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
        found++;
        indexStart = indexStop + 1;
        indexStop = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(indexStart, indexStop).toInt() : 99;
}


// ------------------------------------ setup ------------------------------------------

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  // initialize digital pin 13 as an output.
  pinMode(pinLed, OUTPUT);

  // set up ultrasonic sensor pins
  pinMode(pinTrigger, OUTPUT);
  pinMode(pinEcho, INPUT);

  // set up pan pin
  pan.attach(pinPan);

  // set up tilt pin
  tilt.attach(pinTilt);

  // set up LIS3DH
  myIMU.begin();
}

// ------------------------------------ led ------------------------------------------

void turnLedOn() {
  digitalWrite(pinLed, HIGH);   // turn the LED on (HIGH is the voltage level)
}

void turnLedOff() {
  digitalWrite(pinLed, LOW);    // turn the LED off by making the voltage LOW
}

// ------------------------------------ ultrasonic sensor HC-SR04 ------------------------------------------

void sendUltrasonicDistance() {
  int dist = getUltrasonicDistance();
  Serial.println(dist);
}

// send a ping from ultrasonic sensor HC-SR04 and return distance in cm
int getUltrasonicDistance() {
  // send a 10us+ pulse
  digitalWrite(pinTrigger, LOW);
  delayMicroseconds(20);
  digitalWrite(pinTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrigger, LOW);
  delayMicroseconds(20);

  //  read duration of echo
  int duration = pulseIn(pinEcho, HIGH);

  // dist = duration * speed of sound * 1/2
  // dist in cm = duration in us * 1 x 10^{-6} * 340.26 * 100 * 1/2
  // =  0.017*duration
  float dist = 0.017 * duration;

  return (int)dist;
}

// ------------------------------------ pan ------------------------------------------

void setPanPosition(int panPosition) {
  pan.write(panPosition);
}

// ------------------------------------ tilt ------------------------------------------

void setTiltPosition(int tiltPosition) {
  tilt.write(tiltPosition);
}

// ------------------------------------ accelerometer LIS3DH ------------------------------------------

void sendAccelerometerData() {
  String data = getAccelerometerData();
  Serial.println(data);
}

String getAccelerometerData() {
  return String(myIMU.readFloatAccelX()) + ";" + String(myIMU.readFloatAccelY()) + ";" + String(myIMU.readFloatAccelZ());
}

// ------------------------------------ sensors KTIR0711S ------------------------------------------

void sendKtirData() {
  String data = getKtirData();
  Serial.println(data);
}


String getKtirData() {
  return String(analogRead(ktir1)) + ";" + String(analogRead(ktir2)) + ";" + String(analogRead(ktir3));
}

