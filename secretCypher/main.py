# Connor Pavicic, secretCypher

def cypher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    secret_alphabet = 'zyxwvutsrqponmlkjihgedcba'
    i = 0

    which_decode = input("Would you like to translate or de-translate?: ")
    if which_decode == 'translate':
        translate = input("What would you like to translate?: ")
        translate = list(translate)
        length_translate = len(translate)-1
        while i < length_translate:
            translate[i] = secret_alphabet[i]
            i += 1
            final_translate = str(translate)
        
        return final_translate
    elif which_decode == 'de-translate' or 'detranslate':
        detranslate = input("What would you like to detranslate?:")
        detranslate = str(detranslate)
        length_de = len(detranslate)-1
        while i < length_de:
            detranslate[i] = alphabet[i]
            i += 1
            final_detranslate = str(detranslate)
        
        return final_detranslate
    

print(cypher())
