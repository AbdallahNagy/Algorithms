print("Please think of a number between 0 and 100!")

low = 0
high = 100
ans = 0
secretNumber = (low + high)/2

while True:
    print("Is your secret number " + str(secretNumber) + "?")
    print("Enter 'h' to indicate the guess is too high.", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    print("Enter 'c' to indicate I guessed correctly.", end=' ')
    
    userInput = input()

    if userInput == 'c':
        break
    elif userInput == 'l':
        low = secretNumber
    elif userInput == 'h':
        high = secretNumber
    else:
        print("Sorry, I did not understand your input.")
    
    secretNumber = (low + high)//2

print("Game over. Your secret number was:", str(secretNumber))