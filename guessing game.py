import random

print("-----------------------")
print("   M&M Guessing Game   ")
print("-----------------------")

mm_count = random.randint(0, 101)
attempt_limit = 5
attempt = 0

while attempt < attempt_limit:
    guess_text = input("Please guess the number of M&M's in the jar: ")
    guess = int(guess_text)
    attempt += 1
    if mm_count == guess:
        print(f"Nice, you got free lunch! it was {guess}")
        break
    elif guess < mm_count:
        print("sorry the guess was too LOW")
    else:
        print("sorry the guess was to HIGH")


print(f"{mm_count}")
print("Bye")
