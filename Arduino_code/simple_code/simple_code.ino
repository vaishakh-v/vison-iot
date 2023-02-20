int ledPin = 13;  // define the LED pin

void setup() {
  pinMode(ledPin, OUTPUT);  // set the LED pin as output
  Serial.begin(9600);  // start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();  // read the data sent by Python

    if (data == '0') {
      digitalWrite(ledPin, LOW);  // turn off the LED
    } else if (data == '1') {
      digitalWrite(ledPin, HIGH);  // turn on the LED
    }
  }
}
