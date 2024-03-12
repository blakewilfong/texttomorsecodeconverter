from dictionary import morse_code_dict

def conversion():
    global morse_code_dict
    choice = int(input("If converting to Morse Code, type 1, if converting to English type 2: "))
    if choice == 1:
        english_phrase = list(input("Please enter the word or phrase you would like converted in to morse code").upper())
        morse_code_phrase = [morse_code_dict[character] for character in english_phrase]
        translation = ", ".join(str(character) for character in morse_code_phrase)
        return print(f"Your phrase in Morse Code is {translation}")

    elif choice ==2:
        morse_code_phrase = input("Please enter the word or phrase in Morse Code that you would like to convert"
                                  " to English.  Separate each character with a comma: ").replace(" ", "")
        morse_code_list = morse_code_phrase.split(",")
        print(morse_code_list)
        english_dict = {value: key for key, value in morse_code_dict.items()}
        english_phrase_list = [english_dict[character] for character in morse_code_list]
        translation = "".join(str(character) for character in english_phrase_list)
        return print(f"Your phrase in English is {translation}")


running = True

print("Welcome to the Morse Code converter")

while running:
    conversion()
    user_choice = input("Enter 'q' to quit or hit any other key to continue converting")
    if user_choice.lower() == 'q':
        running = False
