#!/opt/local/bin/python3.12

import random
letter_to_morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}
letters = list(letter_to_morse.keys())

for i in range(10):
    random_letter = random.choice(letters)
    answer = input(f"What does {letter_to_morse[random_letter]} morse code stand for? : ")
    if answer.lower() == random_letter.lower():
        print("Correct")
    else:
        print(f"False, the correct answer is {random_letter}")
