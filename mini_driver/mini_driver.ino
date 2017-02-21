
int pinTrigger = 2;
int pinEcho = 4;
int pinLed = 13;

const int leftMotorDirPin = 7;
const int leftMotorPwmPin = 9;
const int rightMotorDirPin = 8;
const int rightMotorPwmPin = 10;

// ------------------------------------ main ------------------------------------------

// the loop function runs over and over again forever
void loop() {
  readData();
}

// Input:       'device:device_specific_data;'
// Led:         'led:on/off;'
// Motor:       'motor:{left_speed}:{right_speed};'
// Ultrasonic:  'ultrasonic;'
void readData() {
  String data = Serial.readStringUntil(';');
  if (data != "") {
    String device = getValue(data, ':', 0);
    if (device == "led") {
      process_led(data);
    } else if (device == "motor") {
      process_motor(data);
    } else if (device == "ultrasonic") {
      process_ultrasonic_sensor();
    }
  }
}

void process_led(String data) {
  String command = getValue(data, ':', 1);
  if (command == "on") {
    turnLedOn();
  } else if (command == "off") {
    turnLedOff();
  }
}

void process_motor(String data) {
  String left = getValue(data, ':', 1);
  String right = getValue(data, ':', 2);
  driveLeft(left.toInt());
  driveRight(right.toInt());
}

void process_ultrasonic_sensor() {
  sendUltrasonicDistance();
}

String getValue(String data, char separator, int index) {
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

void driveLeft(int power) {
  drive(leftMotorDirPin, leftMotorPwmPin, power);
}

void driveRight(int power) {
  drive(rightMotorDirPin, rightMotorPwmPin, power);
}

void drive(int dirPin, int pwmPin, int power) {
  int pinLevel = LOW;
  if (power < 0) {
     pinLevel = HIGH;
  }
  digitalWrite(dirPin, pinLevel);
  analogWrite(pwmPin, limitPower(power));
}

int limitPower(int power) {
  if (power > 250) {
    return 250;
  } else if (power < -250) {
    return -250;
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

