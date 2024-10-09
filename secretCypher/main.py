# Connor Pavicic, secretCypher

def cypher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    secret_alphabet = 'zyxwvutsrqponmlkjihgfedcba'

    which_decode = input("Would you like to translate or de-translate?: ").lower()
    
    if which_decode == 'translate':
        translate = input("What would you like to translate?: ").lower()
        final_translate = ''
        i = 0
        
        while i < len(translate):
            char = translate[i]
            if char in alphabet:
                index = alphabet.index(char)
                final_translate += secret_alphabet[index]
            else:
                final_translate += char
            i += 1
        
        return final_translate
    
    elif which_decode == 'de-translate' or which_decode == 'detranslate':
        detranslate = input("What would you like to detranslate?: ").lower()
        final_detranslate = ''
        i = 0
        
        while i < len(detranslate):
            char = detranslate[i]
            if char in secret_alphabet:
                index = secret_alphabet.index(char)
                final_detranslate += alphabet[index]
            else:
                final_detranslate += char
            i += 1
        
        return final_detranslate
    else:
        return "That's not an option"

print(cypher())

