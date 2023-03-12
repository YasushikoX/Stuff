import time
import random
import pyautogui
import keyboard

def type_text(text):
    paragraphs = text.split("\n") # Split text into paragraphs
    for paragraph in paragraphs:
        lines = paragraph.split(". ") # Split each paragraph into lines based on the period and space
        for line in lines:
            if keyboard.is_pressed('esc'): # Check if the Esc key is pressed
                print("Program aborted.")
                return
            pyautogui.typewrite(line + ". ", interval=random.uniform(0.01, 0.1)) # Add period and space back to each line, and wait between each keystroke
            if random.randint(1, 1000) == 1: # 1 in 1000 chance of taking a break
                print("Taking a break for 60 seconds...")
                time.sleep(60)
            else:
                time.sleep(random.uniform(5, 15))
        pyautogui.typewrite("\n") # Move to the next line after each paragraph

text_to_type = """Text Here"""
time.sleep(10) # Wait for 10 seconds
type_text(text_to_type)
