
int pinTrigger = 2;
int pinEcho = 4;
int pinLed = 13;

const int leftMotorDirPin = 7;
const int leftMotorPwmPin = 9;
const int rightMotorDirPin = 8;
const int rightMotorPwmPin = 10;

const int driveForwardTimeMs = 10;
const int turnBackTimeMs = 2000;

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
boolean sendData = false;

// send a ping from ultrasonic sensor HC-SR04 and return 
// distance in cm
float ping()
{
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

void driveForward() {
  digitalWrite(leftMotorDirPin, LOW);
  digitalWrite(rightMotorDirPin, LOW);
  analogWrite(leftMotorPwmPin, 133); // left
  analogWrite(rightMotorPwmPin, 128); //right
  delay(driveForwardTimeMs);
}

void driveBack() {
  digitalWrite(leftMotorDirPin, HIGH);
  digitalWrite(rightMotorDirPin, HIGH);
  analogWrite(leftMotorPwmPin, 65);
  analogWrite(rightMotorPwmPin, 64);
  delay(3000);
}

void stopDriving() {
  digitalWrite(leftMotorDirPin, LOW);
  digitalWrite(rightMotorDirPin, LOW);
  analogWrite(leftMotorPwmPin, 0);
  analogWrite(rightMotorPwmPin, 0);
  delay(driveForwardTimeMs);
}

void turnBack() {
  driveBack();
  digitalWrite(leftMotorDirPin, LOW);
  digitalWrite(rightMotorDirPin, HIGH);
  analogWrite(leftMotorPwmPin, 80);
  analogWrite(rightMotorPwmPin, 80);

  int turnBackTimeMsRand = random(1000, 4000);
  delay(turnBackTimeMsRand);
  driveForward();
}

void turnLedOn() {
  digitalWrite(pinLed, HIGH);   // turn the LED on (HIGH is the voltage level)
}

void turnLedOff() {
  digitalWrite(pinLed, LOW);    // turn the LED off by making the voltage LOW  
}

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

// the loop function runs over and over again forever
void loop() {
  //driveForward();
  raspberry();
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    
    // add it to the inputString:
    if (inChar != ';') {
      inputString += inChar;
    }
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == ';') {
      stringComplete = true;
    }
  }
}

void raspberry() {
  if (stringComplete) {
    if (inputString == "on") {
      turnLedOn();
      //turnBack();
      //turnLedOff();
    } else if (inputString == "off") {
      turnLedOff();
      //driveForward();
    } else if (inputString == "stop") {
      stopDriving();
    } else if (inputString == "read") {
      sendPing();
    }

    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

void sendPing() {
  // send a ping
  float dist = ping();
  Serial.println(dist);
  delay(10);
}

