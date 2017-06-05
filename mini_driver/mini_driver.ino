
#include <Servo.h>  // servo library

const int pinTrigger = 2;
const int pinEcho = 4;
const int pinLed = 13;

const int leftMotorDirPin = 8;
const int leftMotorPwmPin = 10;
const int rightMotorDirPin = 7;
const int rightMotorPwmPin = 9;

const int servoPin = 12;

Servo servo1;  // servo control object

// ------------------------------------ main ------------------------------------------

// the loop function runs over and over again forever
void loop() {
  readData();
}

// Input:       'device:device_specific_data;'
// Led:         'led:on/off;'
// Motor:       'motor:{left_speed}:{right_speed};'
// Ultrasonic:  'ultrasonic;'
// Servo:       'servo:{position}'
void readData() {
  const String data = Serial.readStringUntil(';');
  if (data != "") {
    const String device = getValue(data, ':', 0);
    if (device == "led") {
      processLed(data);
    } else if (device == "motor") {
      processMotor(data);
    } else if (device == "ultrasonic") {
      processUltrasonicSensor();
    } else if (device == "servo") {
      processServo(data);
    }
  }
}

void processLed(const String& data) {
  const String command = getValue(data, ':', 1);
  if (command == "on") {
    turnLedOn();
  } else if (command == "off") {
    turnLedOff();
  }
}

void processMotor(const String& data) {
  const String left = getValue(data, ':', 1);
  const String right = getValue(data, ':', 2);
  setLeftEngineSpeed(left.toInt());
  setRightEngineSpeed(right.toInt());
}

void processUltrasonicSensor() {
  sendUltrasonicDistance();
}

void processServo(const String& data) {
  const String servoPosition = getValue(data, ':', 1);
  setServoPosition(servoPosition.toInt());
}

String getValue(const String& data, char separator, int index) {
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length() - 1;

  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
        found++;
        strIndex[0] = strIndex[1] + 1;
        strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

// ------------------------------------ setup ------------------------------------------

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(pinLed, OUTPUT);

  // set up sensor pins 
  pinMode(pinTrigger, OUTPUT);
  pinMode(pinEcho, INPUT);

  // set up motor pins 
  pinMode(leftMotorDirPin, OUTPUT);
  pinMode(leftMotorPwmPin, OUTPUT);
  pinMode(rightMotorDirPin, OUTPUT);
  pinMode(rightMotorPwmPin, OUTPUT);

  // set up servo pin
  servo1.attach(servoPin);

  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// ------------------------------------ ultrasonic sensor HC-SR04 ------------------------------------------

void sendUltrasonicDistance() {
  float dist = getUltrasonicDistance();
  Serial.println(dist);
  delay(10);
}

// send a ping from ultrasonic sensor HC-SR04 and return distance in cm
float getUltrasonicDistance() {
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
  
  return dist;
}

// ------------------------------------ motor ------------------------------------------

void setLeftEngineSpeed(int power) {
  setEngineSpeed(leftMotorDirPin, leftMotorPwmPin, power);
}

void setRightEngineSpeed(int power) {
  setEngineSpeed(rightMotorDirPin, rightMotorPwmPin, power);
}

void setEngineSpeed(int dirPin, int pwmPin, int power) {
  int pinLevel = LOW;
  if (power < 0) {
     pinLevel = HIGH;
  }
  digitalWrite(dirPin, pinLevel);
  analogWrite(pwmPin, limitPower(power));
}

int limitPower(int power) {
  if (power > 245) {
    return 245;
  } else if (power < -245) {
    return -245;
  } else {
    return power;
  }
}

// ------------------------------------ led------------------------------------------

void turnLedOn() {
  digitalWrite(pinLed, HIGH);   // turn the LED on (HIGH is the voltage level)
}

void turnLedOff() {
  digitalWrite(pinLed, LOW);    // turn the LED off by making the voltage LOW  
}

// ------------------------------------ servo------------------------------------------

void setServoPosition(int servoPosition) {
  servo1.write(servoPosition);
}

