// Include necessary libraries
#include <Arduino.h>
#include <TFT_eSPI.h>

// Define pin numbers for potentiometer and buttons
#define POTENTIOMETER_PIN 15
#define BUTTON_PIN 12
#define RESET_BUTTON_PIN 13

// Define thresholds for rock, paper, and scissors
#define ROCK_THRESHOLD 1500
#define PAPER_THRESHOLD 3000
#define SCISSORS_THRESHOLD 4500

// Define baud rate for serial communication
#define BAUD_RATE 115200

TFT_eSPI tft; // Initialize TFT_eSPI object

void setup() {
  // Initialize serial communication
  Serial.begin(BAUD_RATE);

  // Initialize TFT screen
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK); 

  // Print "Rock, Paper, Scissors" text on the screen
  tft.setTextColor(TFT_WHITE);
  tft.setTextSize(1);
  int textWidth = tft.textWidth("Rock, Paper, Scissors");
  int textX = (tft.width() - textWidth) / 2; 
  tft.setCursor(textX, 50); 
  tft.print("Rock, Paper, Scissors");

  // Set button pins as inputs
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(RESET_BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  // Read the value from the potentiometer
  int potValue = analogRead(POTENTIOMETER_PIN);

  // Determine the selected option based on potentiometer value
  String selectedOption;
  if (potValue < ROCK_THRESHOLD) {
    selectedOption = "Rock";
  } else if (potValue < PAPER_THRESHOLD) {
    selectedOption = "Paper";
  } else if (potValue < SCISSORS_THRESHOLD) {
    selectedOption = "Scissors";
  }

  // Check if the button is pressed
  if (digitalRead(BUTTON_PIN) == LOW) {
    // Send the selected option over serial communication
    Serial.println(selectedOption);
    delay(500); // debounce delay
  }

  // Check if the reset button is pressed
  if (digitalRead(RESET_BUTTON_PIN) == LOW) {
    // Send the signal for button press over serial communication
    Serial.println("pressed");
    delay(500); // debounce delay
  }

  delay(100); // Add a small delay to avoid reading too frequently
}
