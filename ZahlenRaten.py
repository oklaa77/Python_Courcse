#Es gibt Fehler

import random

max_num_of_guesses = 5
min_allowed_number = 1
max_allowed_number = 100
number_to_guess = random.randint(min_allowed_number, max_allowed_number) # Zuweisung
print(number_to_guess)

for i in range(max_num_of_guesses): # magic number
    #print(i+1)
    user_input = input(
        f"Bitte gebe eine Zahl ein (zwischen {min_allowed_number} und {max_allowed_number}): "
    )
    try:
        user_input_as_int = int(user_input)
    except ValueError:
        print("Bitte Zahlen eingeben")
        continue
        
    if (user_input_as_int > max_allowed_number) or (user_input_as_int < min_allowed_number): 
        # Achtung! Einrueckung (4 Leerzeichen)-> If-body
        print("Die eingegebe Zahl liegt ausserhalb der erlaubten Grenzen !!!")
        print("Bitte versuche es nochmal")
    else:       
        # print("jetzt schaue ich nach, ob das die gesuchte Zahl ist...")
        if user_input_as_int == number_to_guess: # Vergleich
            print("Bingo! Gut gemacht!")
            break
        else:
            print("Leider falsch!")

print(f"AUf Wiedersehen (nach {i+1} Versuch(en))")  