import pygame
import time

import requests

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
#MORSE_TO_ENGLISH = {ENGLISH_TO_MORSE[key]: key for key in ENGLISH_TO_MORSE}

TIME_BETWEEN = 0.5  # Time between sounds
PATH = "morse_code_audio/"


def verify_contents_are_valid(string):
    keys = list(ENGLISH_TO_MORSE.keys())
    for char in string:
        if char not in keys and char != " ":
            return False
    return True




def main():

    print("### English to Morse Code Audio Converter ###")
    print("Enter your message in English: ")
    print("if the message is a single spacebar, your location will be used")
    message = input("> ").upper()
    if message == " ":
        response = requests.get("http://ip-api.com/json/")  # get location using api
        if response.status_code!=200:
            print("unable to recieve response from API, check internet connectivity")
            message = "no location found"
        else:
            location = response.json()['city'].upper()  # extract city from response
            message = location
            print(location)  # write out the location for debugging

    if verify_contents_are_valid(message):
        pygame.init()
        for char in message:
            if char == " ":
                print(" " * 3, end=" ")  # Separate words clearly
                time.sleep(5 * TIME_BETWEEN)
            else:
                print(ENGLISH_TO_MORSE[char.upper()], end=" ")
                pygame.mixer.music.load(PATH + char + '_morse_code.ogg')  # loads the sound files from the hard drive
                pygame.mixer.music.set_volume(0.1)                        # sets the volume to prevent sound being muted
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():  # while inefficient, it allows the letters to be distinct
                    pass
                time.sleep(1 * TIME_BETWEEN)
    else:
        print(f"A character cannot be translated into Morse Code.")

if __name__ == "__main__":
    main()