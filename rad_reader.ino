
// global variables to hold the pin input and read value from the detector
int analogPin = A7;
int analogVal = 0;
int radVal = 0;

void setup() {
  // initial setup
  Serial.begin(9600);
}

void loop() {
  // grab the analog reading from the detector, print it to serial monitor
  analogVal = analogRead(analogPin);
  radVal = (analogVal > 512) ? 1 : 0;
  Serial.println(radVal);
}
