
morse_code_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', ':': '---...',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '=': '-...-', ' ': ' ',
}



choice = int(input("Welcome to the Morse Code Converter. "
                   "If converting to Morse Code, type 1, if converting to English type 2."))

if choice == 1:
    english_phrase = list(input("Please enter the word or phrase you would like converted into morse code").upper())
    morse_code_phrase = [morse_code_dict[character] for character in english_phrase]
    translation = ", ".join(str(character) for character in morse_code_phrase)
    print(f"Your phrase in Morse Code is {translation}")

elif choice ==2:
    morse_code_phrase = input("Please enter the word or phrase in Morse Code that you would like to convert"
                              "to English.  Separate each character with a comma")
    morse_code_list = morse_code_phrase.split(",")
    morse_code_dict = {value: key for key, value in morse_code_dict.items()}
    english_phrase_list = [morse_code_dict[character] for character in morse_code_list]
    translation = "".join(str(character) for character in english_phrase_list)
    print(f"Your phrase in English is {translation}")
