import pygame
import serial
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")

# Function to read serial data from ESP32
def read_serial_data():
    SERIAL_PORT = '/dev/cu.wchusbserial54FC0114321' 
    BAUD_RATE = 115200
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    try:
        while True:
            data = ser.readline().decode().strip()
            if data:
                return data
    except KeyboardInterrupt:
        ser.close()
        print("Serial connection closed.")

# Function to reset the game
def reset_game():
    # Clear the screen
    screen.fill(WHITE)

    # Draw border
    pygame.draw.rect(screen, BLACK, (0, 0, screen_width, screen_height), 15)
    
    # Display title text
    font_title = pygame.font.Font(None, 85)
    text_title = font_title.render("Rock, Paper, Scissors", True, BLACK)
    title_rect = text_title.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(text_title, title_rect)
    
    # Display instruction text
    font_play = pygame.font.Font(None, 70)
    text_play = font_play.render("Make your move!", True, BLACK)
    play_rect = text_play.get_rect(center=(screen_width // 2, screen_height * 2 // 3))
    screen.blit(text_play, play_rect)

    pygame.display.flip()

# Initialize Pygame
pygame.init()

# Load images
comp_rock_img = pygame.image.load('comp_rock.jpeg')
comp_paper_img = pygame.image.load('comp_paper.jpeg')
comp_scissors_img = pygame.image.load('comp_scissors.jpeg')

# Display initial screen
reset_game()

# Function to play game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read user's choice from serial port
    user_choice = read_serial_data()

    if user_choice: 
        # Generate computer's choice
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Compare choices and determine winner
        if user_choice == computer_choice:
            result_text = "It's a tie!"
            result_color = BLACK
            border_color = BLACK
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result_text = "You Win!"
            result_color = GREEN
            border_color = GREEN
        else:
            result_text = "You Lose!"
            result_color = RED
            border_color = RED

        # Clear the screen
        screen.fill(WHITE)

        # Draw border
        pygame.draw.rect(screen, border_color, (0, 0, screen_width, screen_height), 15)

        # Display user's choice 
        font_user_move = pygame.font.Font(None, 36)
        text_user_move = font_user_move.render("Your Move", True, BLACK)
        user_move_rect = text_user_move.get_rect(center=(screen_width - 200, 100))
        screen.blit(text_user_move, user_move_rect)

        if user_choice == "Rock":
            screen.blit(comp_rock_img, (screen_width - 250, 150))
        elif user_choice == "Paper":
            screen.blit(comp_paper_img, (screen_width - 250, 150))
        elif user_choice == "Scissors":
            screen.blit(comp_scissors_img, (screen_width - 250, 150))

        #Display VS
        font_versus = pygame.font.Font(None, 75)
        text_versus = font_versus.render("VS", True, BLACK)
        screen.blit(text_versus, (367, 200))

        # Display computer's choice 
        font_comp_move = pygame.font.Font(None, 36)
        text_comp_move = font_comp_move.render("Computer's Move", True, BLACK)
        comp_move_rect = text_comp_move.get_rect(center=(200, 100))
        screen.blit(text_comp_move, comp_move_rect)

        if computer_choice == "Rock":
            screen.blit(comp_rock_img, (150, 150))
        elif computer_choice == "Paper":
            screen.blit(comp_paper_img, (150, 150))
        elif computer_choice == "Scissors":
            screen.blit(comp_scissors_img, (150, 150))

        # Display result
        font_result = pygame.font.Font(None, 100)
        text_result = font_result.render(result_text, True, result_color)
        result_rect = text_result.get_rect(center=(screen_width // 2, screen_height * 17 // 24))
        screen.blit(text_result, result_rect)

        # Display "Press button to play again" at the bottom
        font_play_again = pygame.font.Font(None, 36)
        text_play_again = font_play_again.render("Press Play Again", True, BLACK)
        screen.blit(text_play_again, (screen_width // 2 - text_play_again.get_width() // 2, screen_height * 5 // 6))

        pygame.display.flip()

        # Wait for button press to play again
        while True:
            button_state = read_serial_data()
            if button_state == "pressed":
                reset_game()
                break  # Break out of the loop when button is pressed


# Quit Pygame
pygame.quit()