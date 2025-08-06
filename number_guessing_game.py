def number_guessing():
    import random
    choices=['easy','medium','hard']
    for i,item in enumerate(choices):
        print(f"{i}. {item}")
    level = input("Choose level: Easy(1-10)\n Medium(1-50)\n Hard(1-100): ").lower()
    if level == choices[0]:
        secret_number = random.randint(1,10)
        value = int(input("Your guess : "))
        while value != secret_number:
            if value <secret_number:
               print("Too low! 📉")
            elif value > secret_number:
               print("Too high! 📈")
            value = int(input("Your guess : "))  
        print("Nice guess kiddo!!🥳 You got it right!")
    elif level == choices[1]:
        lives = 7
        secret_number = random.randint(1,50)
        value = int(input("Your guess : "))
        while value != secret_number and lives != 0:
            if value <secret_number:
               print("Too low! 📉")
               lives -= 1
            elif value > secret_number:
               print("Too high! 📈")
               lives -= 1
            print(f"{lives} lives left!!")
            value = int(input("Your guess : ")) 
        if lives ==0:
            print(f"Better luck next time! The number was {secret_number}") 
        else:  
            print(f"Nice guess kiddo!!🥳 You got it right with {lives} lives left")
    elif level == choices[2]:
        lives = 5
        secret_number = random.randint(1,100)
        value = int(input("Your guess : "))
        while value != secret_number and lives != 0:
            if value <secret_number:
               print("Too low! 📉")
               lives -= 1
            elif value > secret_number:
               print("Too high! 📈")
               lives -= 1
            print(f"{lives} lives left!!")
            value = int(input("Your guess : "))
        if lives ==0:
            print(f"Better luck next time! The number was {secret_number}") 
        else: 
            print(f"Nice guess kiddo!!🥳 You got it right with {lives} lives left")
    else:
        print("Choose the level!!")

number_guessing()