list1 = [1, 1, 2]
list2 = [2, 3, 4]

# list1'ni nusxalash
result = list1[0:2]

# list2'ni elementlarini list1'da yo'q bo'lsa qo'shish
for item in list2:
    if item not in list1:
        result.append(item)

print(result)

n = 5
i = 1
while i<n:
    a = i**2
    i+=1
    print(a)




txt = "hello"

result = ""
for i in range(len(txt)):
    result += txt[i]
    # Check if character is a vowel or every third character
    if txt[i] in ("a",'i','o','u','e') or (i + 1) % 3 == 0:
        # Ensure it's not the last character
        if i != len(txt)-1:
            result += "_"

print(result)


import random

# def number_guessing_game():
#     while True:
#         number_to_guess = random.randint(1, 100)
#         attempts = 10

#         print("Welcome to the Number Guessing Game!")
#         print("I have selected a number between 1 and 100. Can you guess it?")

#         while attempts > 0:
#             try:
#                 guess = int(input(f"You have {attempts} attempts remaining. Enter your guess: "))

#                 if guess < number_to_guess:
#                     print("Too low!")
#                 elif guess > number_to_guess:
#                     print("Too high!")
#                 else:
#                     print("You guessed it right!")
#                     break

#                 attempts -= 1
#             except ValueError:
#                 print("Please enter a valid number.")

#         if attempts == 0:
#             print(f"You lost. The correct number was {number_to_guess}. Want to play again?")

#         play_again = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ").strip().lower()
#         if play_again not in ['y', 'yes', 'ok']:
#             print("Thanks for playing! Goodbye!")
#             break

# number_guessing_game()

def password_checker():
    password = input("Parolingizni kiriting: ")

    if len(password) < 8:
        print("parol qisqa.")
    elif not any(char.isupper() for char in password):
        print("parolni to'g'ri kiritdingiz.")
    else:
        print("parol uzun.")

password_checker()

def print_primes():
    print("1 dan 100 gacha sonlar orasidan tub sonlarni aniqlash")
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n")

# Run the Prime Numbers Task
print_primes()


