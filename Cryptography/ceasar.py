# move all letters by one modulo 26
def moveLetterBy(letter, amount):
    ascii = ord(letter)
    order = ascii - 97
    new_order = (order + amount) % 26
    new_ascii = new_order + 97
    return chr(new_ascii)

def shiftTextByAmount(text, amount):
    shifted = ""
    for letter in text:
        shifted += moveLetterBy(letter,amount)
    return shifted

text = input("Enter text to shift 26 times: ")
for i in range(26):
    print(f"The text shifted by {i} is {shiftTextByAmount(text,i)}")
    input()
