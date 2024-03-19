# COMS-BC-3930-Module2
COMS-BC-3930-Module2 

Lab Steps
Connect potentiometer  left pin to 3V pin, middle pin to any analog pin, right pin to ground
Connect one side of button to ground, otherside to any analog pin

Code:
const int buttonPin = 12; // GPIO pin used for the button
const int potPin = 15; // Analog pin used for the potentiometer

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP); // Enable internal pull-up resistor
}

void loop() {
  int potValue = analogRead(potPin); // Read the potentiometer value
  int buttonState = digitalRead(buttonPin); // Read the button state
  
  // Print the values to the Serial Monitor
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print("\tButton State: ");
  Serial.println(buttonState);

  delay(100); // Small delay to make the serial output more readable
}
