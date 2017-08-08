
const int pinLed = 13;

const int leftMotorDirPin = 8;
const int leftMotorPwmPin = 10;
const int rightMotorDirPin = 7;
const int rightMotorPwmPin = 9;

// ------------------------------------ main ------------------------------------------

// the loop function runs over and over again forever
void loop() {
   readData();
}

// Input:       'device:device_specific_data;'
// Led:         '0:{state};' on - 1, off - 0
// Motor:       '1:{left_speed}:{right_speed};'
void readData() {
  const String data = Serial.readStringUntil(';');
   if (data != "") {
     const int device = getValue(data, ':', 0);
     switch(device) {
        case 0:
          processLed(data);
          break;
        case 1:
          processMotor(data);
          break;
      }
   }
}

void processLed(const String& data) {
  getValue(data, ':', 1) ? turnLedOn() : turnLedOff();
}

void processMotor(const String& data) {
  setLeftEngineSpeed(getValue(data, ':', 1));
  setRightEngineSpeed(getValue(data, ':', 2));
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

  // set up motor pins 
  pinMode(leftMotorDirPin, OUTPUT);
  pinMode(leftMotorPwmPin, OUTPUT);
  pinMode(rightMotorDirPin, OUTPUT);
  pinMode(rightMotorPwmPin, OUTPUT);
}

// ------------------------------------ led ------------------------------------------

void turnLedOn() {
  digitalWrite(pinLed, HIGH);   // turn the LED on (HIGH is the voltage level)
}

void turnLedOff() {
  digitalWrite(pinLed, LOW);    // turn the LED off by making the voltage LOW
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

