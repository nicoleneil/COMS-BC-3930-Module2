# COMS-BC-3930-Module2
Rock, Paper, Scissors Digital Game - Interactive Devices Project

Description: This project allows a human user to play a digital version of the classic game Rock, Paper, Scissors. Twist the potentiometer knob to choose a move (Rock, Paper, or Scissors). Press the button labeled "Select" to input your choice. Look at the laptop screen to see whether you or the computer won the game! Press the button labeled "Play Again" to play another round. 

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


Materials: 
ESP32 TTGO 
2 Male Electronic Headers
Breadboard
2 Buttons
Potentiometer
Potentiometer Knob Cap
Usb-c Cable
Laptop (MacBook Pro)
Solder
Soldering Iron 
Wire 
Cardboard
Stapler & Staples
Scissors
X-Acto Knife
Hot Glue Gun
Sharpie
Pen
Pencil
Eraser
Maksing Tape
Packing Tape
Hole puncher

Process:
1. Solder Male Electronic Headers to both sides of ESP32 TTGO (tutorial: https://www.youtube.com/watch?v=rqZaLtoW9_Y)
  INSERT PIC OF SOLDERED ESP32
2. Connect ESP32 to breadboard. 
3. Connect potentiometer and buttons to ESP32 with wires via breadboard. Ensure that you:
  a. For the potentiometer connect the left pin to 3V pin, the middle pin to an analog pin, and the right pin to Ground. 
  b. For each button connect one pin to Ground and one to a GPIO pin.
  INSERT PIC OF FULL CIRCUITRY
5. Configure Board and Port in the Tools section of the Arduino app for compatibility with your ESP32 TTGO. 
6. Develop program (in C++ Arduino IDE) on laptop (MacBook Pro) for ESP32 TTGO to connect hardware to game. Ensure that you:
  a. Define pin numbers for potentiometer and buttons. 
  b. Define thresholds for rock, paper, and scissors moves using potentiometer.
  c. Define baud rate for serial communication & initialize serial communication.
7. Flash program from laptop to ESP32 TTGO via Usb-C (ensure that your Usb-c cable has all the necessary pins for this to work). 
  INSERT PIC OF ESP32 WITH WIRING CONNETCTED TO LAPTOP
![IMG_9882](https://github.com/nicoleneil/COMS-BC-3930-Module1/assets/158202481/c6d48623-c219-463e-a6cb-fe191962a506)
8. Develop program (in Python) for the game visuals to be displayed on the laptop screen via pygame. Ensure that you:
  a. Write a function to read serial data from the ESP32. 
  b. Write a function to perform the game logic where Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
9. Close the Arduino app and run the Python program. Perform debugging and make any adjustments to your code as necessary.  
10. In pencil sketch the shape of the game controller on cardboard and cut it out using the scissors. Place the cutout on another piece of cardboard, trace the outline, and cut out the second game controller outline. These are the top and bottom of the device enclosure.
11. Cut two long strips about 1.5 inches in width out of the cardboard. Roll the cardboard lengthwise into spirals to make the material less rigid. This will connect the top and bottom of the device enclosure.



12. Use the hole puncher to make holes in the envelope. Thread string through these holes and tie knots to secure the string. Tie the other ends of the strings to the popsicle stick and tape the knots down to secure them to the wood. 

13. Solder crimp connector to wire with Soldering iron (performed by Prof Santolucito). 
![IMG_9883](https://github.com/nicoleneil/COMS-BC-3930-Module1/assets/158202481/b38447d0-781f-4b92-a2d5-cd6b2ce23229)

14. Place a sectin of heat shrink wrap tubing over the soldered connection between the crimp connector and wire. Be sure to have hair and sleeves tied/pulled back to avoid injury and use the heat gun to melt the heat shrink wrap tubing to cover the soldered connection and prevent the black and red wires from touching.
![IMG_9884](https://github.com/nicoleneil/COMS-BC-3930-Module1/assets/158202481/c6fd26e3-2e76-446f-ab80-d5a8e5b859a4)

15. Within the white connector end of the wire attached to the 220 mA battery, connect the black wire to the black wire of the battery  and connect the red wire to the red wire of the battery. Connect the white connector end of the wire to the port on the back of the ESP32 TTGO. 
![IMG_9913](https://github.com/nicoleneil/COMS-BC-3930-Module1/assets/158202481/d4a38062-64ea-440d-91bb-b93565bfbc8d)

16. Place the ESP32 TTGO attached with wires to the battery into the decorated envelope and seal it with tape.
![IMG_9945](https://github.com/nicoleneil/COMS-BC-3930-Module1/assets/158202481/9d92e5dc-044f-4586-8fdb-253618240a94)

17. Hang the full project in the designated vent using the popsicle stick.
![IMG_9946](https://github.com/nicoleneil/COMS-BC-3930-Module1/assets/158202481/a9b9db71-b9c0-4cbf-89ad-c7edb5fbbb8c)
