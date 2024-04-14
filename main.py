# Python program to implement Morse Code Translator
from array import array

from unidecode import unidecode

import googletrans
from googletrans import Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
                   'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
                   'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
                   'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
                   'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.',  ')': '-.--.-', '!':'-.-.--',
                   ':':'',';':''
                   }


# Function to encrypt the string
# according to the morse code chart
def encrypt_to_cw(message):
    cipher = ''
    for letter in message:
        if letter not in MORSE_CODE_DICT.keys():
            cipher += ' '
            continue
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            # Add ; to separate each morse character
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

def translate_text_to_lan( translate_text, source_translate, dest_translate):

    # Translator Class
    translator = Translator()

    results_translate = []
    try:
        for text in translate_text:
            # Strip the text from new lines
            text = text.strip()

            if text is '':
                results_translate.append('\n')
                continue
            else:
                # Translate the Text
                result = translator.translate(text=text, src=source_translate, dest=dest_translate)

                if dest_translate is "sr":
                    out_text = unidecode(result.pronunciation)
                else:
                    out_text = unidecode(result.text)
                results_translate.append(out_text + '\n')

    except Exception as e:
        print("Something went wrong in the translation: ", e)
        return ''

    print("Text has been Translated")

    return results_translate

def write_cw_to_file(file_path, cw_text):
    with open(file_path, "w") as output:
        output.writelines(cw_text)

def get_text_from_file(file):
    with open(file, "r", encoding="utf-8") as output:
        text_list = output.readlines()
    return text_list

def encript_multiline_to_cw(multilene_text):

    results_list = []

    for text in multilene_text:
        # Remove all the new line characters
        text = text.strip()

        # If text is empty continue with the next text
        if text is '':
            results_list.append('\n')
        else:
            # Remove special characters and set upper characters all
            out_message = unidecode(text).upper()
            # Convert text to CW
            result = encrypt_to_cw(out_message)
            # Split all the words and give space
            result = result.replace('  ', "/")
            result = result.replace(' ', ";")

            result = result.replace('/', " / ")
            result = result.replace(';', " ; ")

            print(text)
            print("%s\n" % result)

            results_list.append(result + '\n')

    return results_list


# Hard-coded driver function to run the program
def main():

    original_text_lan = 'hu'
    translate_text_lan = 'en'
    translate_text = 1

    text_list = get_text_from_file("idezetek.txt")

    if translate_text:
        translated_text = translate_text_to_lan(text_list, original_text_lan, translate_text_lan)
    else:
        translated_text = text_list

    result = encript_multiline_to_cw(translated_text)

    cw_file_name = translate_text_lan + '_cw_translated_text' + '.txt'
    write_cw_to_file(cw_file_name, result)

    print("File has been properly generated")


# Executes the main function
if __name__ == '__main__':
    main()