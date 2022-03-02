
number = 'a'

while number !=0:
    numberText = input("Please Enter a NUmber to the Even finder")
    number = int(numberText)

    if number == 0:
        print("thanks for playing, bye")
        break
    if number % 2 == 0:
        print(f"Hurray {number} is even!")
    else:
        print(f"{number} is odd")
