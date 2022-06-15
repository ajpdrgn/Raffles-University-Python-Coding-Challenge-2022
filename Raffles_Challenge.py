import random

#MAIN CODE
def main():
    print("\nPlease type a number to indicate which challenge you want to try out! \nChallenge 1 = 1 \nChallenge 2 = 2 \nChallenge 3 = 3\n")
    challengeNum = int(input("Type number here: "))
    print("\n")
    if challengeNum == 1:
        print("Hello, User! You have selected Challenge 1 for the Python Coding Challenge \n")
        print("This challenge prints the second largest number in a list! Below are the options: \n")
        challengeOne()
    elif challengeNum == 2:
        print("Hello, User! You have selected Challenge 2 for the Python Coding Challenge \n")
        gradeMarkings()
    elif challengeNum == 3:
        print("Hello, User! You have selected Challenge 3 for the Python Coding Challenge \n")
        challengeThree()

#CHALLENGE 1 CODE
def challengeOne():
    print("Type 1 for a Randomly Generated List")
    print("Type 2 to Create Your Own List \n")
    picker = int(input("Type number here: "))
    if picker == 1:
        randomizedList()
    elif picker == 2:
        ownList()
    
class detector:
    def __init__(self, numList):
        self.numList = numList
    def checkSecNum(self):
        sortedNumList = self.numList
        sortedNumList.sort()
        print("Sorted List:",sortedNumList)
        print("\nThe second largest number in the list is:", sortedNumList[-2])
        challengeComplete()

def randomizedList():
    randomizedList = random.sample(range(1,100),10)
    print("\nThe generated randomized number list is:", randomizedList)
    listChecker = detector(randomizedList)
    listChecker.checkSecNum()

def ownList():
    listCount = int(input("\nHello, user! How many numbers would you like to be in your list? "))
    userList = []
    for x in range(1,listCount+1):
        n = int(input(f"Please enter integer {x}: "))
        userList.append(n)
    listChecker = detector(userList)
    listChecker.checkSecNum()

#CHALLENGE 2 CODE
def gradeMarkings():
    print("Please input your 5 scores for the exam. This program will determine your average score and your final marking!")
    gradeList = []
    for x in range(1,6):
        score = input(f"Please input grade {x}: ")
        gradeList.append(int(score))
    print("List of grades:", gradeList)
    sum = 0
    for grade in gradeList:
        sum = sum + grade
    average = sum/5
    print("Average:",average)
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
    challengeComplete()
     
#CHALLENGE 3 CODE
        
def challengeThree():
    print("This is a word guessing game that has 3 modes: Easy, Medium, and Hard! \n")
    print("Easy Mode = 1")
    print("Medium Mode = 2")
    print("Hard Mode = 3")
    mode = int(input("\nPlease input a number to choose your mode: "))
    print("\n")
    if mode == 1:
        print("Easy Round will now begin! \nPlease remember to type in a *character* only for guessing. If the answer already seems clear, type in the full word!\n")
        easyMode()
    elif mode == 2:
        print("Medium Round will now begin! \nPlease remember to type in a *character* only for guessing. If the answer already seems clear, type in the full word!\n")
        mediumMode()
    elif mode == 3:
        print("Hard Round will now begin! \nPlease remember to type in a *character* only for guessing. If the answer already seems clear, type in the full word! \n")
        hardMode()
    else:
        print("Input not within the choices. Please restart the program.")
        quit()
        
#Create class for every mode
class GuessingGame:
    def __init__(self,wordList,numberOfTries):
        self.wordList = wordList
        self.numberOfTries = numberOfTries
        
    def guessword(self):
        word = random.choice(self.wordList).lower()
        tries = self.numberOfTries
        
        #store every user input for checking
        correctLetters = []
        incorrectLetters = []

        #make sure that user still has "lives" for the game to continue
        while tries > 0:
            output = ''
            for letter in word:
                if letter in correctLetters:
                    output += letter
                else:
                    output += ' - '
                #to hide the letters of the word
            if output == word:
              break
            
            #where the game starts first
            print("Guess the word: ", output)
            print(tries,"chances left")
            userGuess = input().lower()
            if userGuess == word:
                break
            if userGuess in correctLetters or userGuess in incorrectLetters:
                print("Try again. Already guessed")
                tries = tries - 1
                print(correctLetters, incorrectLetters)
            elif userGuess in word:
                print("Great, you guessed a letter correctly!")
                correctLetters.append(userGuess)
            else:
                print("Wrong letter, please try again!")
                tries = tries - 1
                incorrectLetters.append(userGuess)
        
        if tries > 0:
            print("you guessed the word! Awesome job!")
        else:
            print(f"Wrong answer. The word was {word}, please restart the game and try again.")

def easyMode():
    easy = ["eat","rat","dog","fig"]
    easyGuessingGame = GuessingGame(easy, 6)
    easyGuessingGame.guessword()
    challengeComplete()

def mediumMode():
    medium = ["four","pair","star","near","ruin","park"]
    mediumGuessingGame = GuessingGame(medium, 5)
    mediumGuessingGame.guessword()
    challengeComplete()

def hardMode():
    hard = ["zebra","spark","jeans"]
    hardGuessingGame = GuessingGame(hard, 4)
    hardGuessingGame.guessword()
    challengeComplete()

#CHALLENGE COMPLETE
def challengeComplete():
    print("\nChallenge complete!")
    print("Please type YES if you want to explore other challenges and NO if you want to exit the program!")
    decision = input()
    if decision.lower() == "yes":
        main()
    else:
        quit()



#START OF PROGRAM
print("Hello, user! Welcome to my entry for the Raffles University Python Coding Challenge!")
main()

        
        
        


    
