# COMS-BC-3930-Module2
Rock, Paper, Scissors Digital Game - Interactive Devices Project

Description: This project allows a human user to play a digital version of the classic game Rock, Paper, Scissors. Twist the potentiometer knob to choose a move (Rock, Paper, or Scissors). Press the button labeled "Select" to input your choice. Look at the laptop screen to see whether you or the computer player won the game! Press the button labeled "Play Again" to play another round with the computer. 

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
Pencil
Painter's Tape
Packing Tape
Hole Puncher

Process:
1. Solder Male Electronic Headers to both sides of ESP32 TTGO (tutorial: https://www.youtube.com/watch?v=rqZaLtoW9_Y)
![IMG_0312](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/52f04e1b-3076-41f2-8421-32437c0a4533)

2. Connect potentiometer and buttons to ESP32 with wires via breadboard. Ensure that you:
  a. Secure the potentiometer knob cap on the top of the potentiometer. 
  b. For the potentiometer connect the left pin to 3V pin, the middle pin to an analog pin, and the right pin to Ground. 
  c. For each button connect one pin to Ground and one to a GPIO pin.
![IMG_0305](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/51f1b2af-02fa-40b5-8c9c-b5d3473a4114)

3. Configure Board and Port in the Tools section of the Arduino app for compatibility with your ESP32 TTGO. 
4. Develop program (in C++ Arduino IDE) on laptop (MacBook Pro) for ESP32 TTGO to connect hardware to game. Ensure that you:
  a. Define pin numbers for potentiometer and buttons. 
  b. Define thresholds for rock, paper, and scissors moves using potentiometer.
  c. Define baud rate for serial communication & initialize serial communication.
5. Flash program from laptop to ESP32 TTGO via Usb-C (ensure that your Usb-c cable has all the necessary pins for this to work). 
![IMG_0307](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/c0deab84-6331-4699-94f4-ceaa4817f0e7)

6. Develop program (in Python) for the game visuals to be displayed on the laptop screen via pygame. Ensure that you:
  a. Write a function to read serial data from the ESP32. 
  b. Write a function to perform the game logic where Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
7. Close the Arduino app and run the Python program. Perform debugging and make any adjustments to your code as necessary.  
  INSERT PIC OF ESP32 WITH WIRING CONNETCTED TO LAPTOP 
8. In pencil sketch the shape of the game controller on cardboard and cut it out using the scissors. Place the cutout on another piece of cardboard, trace the outline, and cut out the second game controller outline. These are the top and bottom of the device enclosure.
9. On one of the game controller outlines (this will be the top piece) trace the outline of the potentiometer and buttons in appropriate spots. Cut out these circles using an X-Acto knife. Insert the buttons and potentiometer into their respective holes and secure the buttons with their screws.
![IMG_0237](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/cee13796-6148-429c-8f30-cfa5c1318d16)

10. Using sharpie, label the buttons correctly ("Select" and "Play Again") and label the appropriate ranges for "Rock, Paper, Scissors" on the potentiometer. 
![IMG_0304](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/d56baf48-bb26-47fc-a5d1-05fa15e36ad2)

11. Cut two long strips about 1.5 inches in width out of the cardboard. Roll and unroll the cardboard lengthwise into spirals to make the material less rigid. Staple the two pieces together so that there is enough length to fully connect to the top of the enclosure. Then use a hot glue gun to connect the strip of cardboard to the top of the enclosure cardboard piece. This will connect the top and bottom of the device enclosure.
![IMG_0302](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/c2d004e4-39c7-4a91-9329-2f8b5d8eb5f6)

12. Check to see where the usb-c cord naturally points out of the ESP32 and use a hole puncher to make a cutout of the height strip for the cord to be thread through to the laptop.
![IMG_0301](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/7fc6fa2a-aa22-4401-a8eb-0fa4b10c15c8)

13. Add cardboard pieces on top of the circuitry to secure it within the enclosure. Secure them in place with painter's tape.
![IMG_0300](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/c6e1dc35-3c47-419f-8774-d8f1fb3ccc31)

14. Place the bottom game controller outline on top of the cardboard covering the circuitry and secure it in place with strips packing tape.
![IMG_0238](https://github.com/nicoleneil/COMS-BC-3930-Module2/assets/158202481/7a9c4f49-3495-4c0a-9652-9d32384fd4fe)
