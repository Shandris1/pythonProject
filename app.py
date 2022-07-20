from flask import Flask, request, render_template


ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}




app = Flask(__name__)

def verify_contents_are_valid(string):
    keys = list(ENGLISH_TO_MORSE.keys())
    for char in string:
        if char not in keys and char != " ":
            print(f"The character {char} cannot be translated.")
            raise SystemExit


@app.route('/')
def my_form():
    return render_template('morse-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    message = text.upper()



    #message = input("> ").upper()
    verify_contents_are_valid(message)
    output_message = ""




    for char in message:
        if char == " ":
            output_message += " " * 3  # Separate words clearly
        else:
            output_message += ENGLISH_TO_MORSE[char.upper()]
            output_message += " "




    return output_message