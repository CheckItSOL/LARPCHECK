import os
import time
from colorama import Fore, Style

# ANSI colors and styles
CYAN = Fore.CYAN
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT
DIM = Style.DIM

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    """Type text with a cool effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
