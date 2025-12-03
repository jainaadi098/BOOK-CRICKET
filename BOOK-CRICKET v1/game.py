import random 
score=0          # score initialization

name=input("Enter your character's name: ")       # get player's name
print(f"Welcome {name} to this game!")
print("press enter to continue...")
input()

########################################################
# Function to generate a random number between 0 and 9 #
########################################################
def random_number(): 
    return random.randint(0, 9)

def ask_to_continue():  # function to ask player if they want to continue
    while True:
        choice = input("\nDo you want to continue playing? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            print("\nNow you are in Infinite mode!\n")
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.\n")

def main(score): # main game function
    mode="Normal"  # initial game mode
    while True:    # main game loop
        number=random_number()
        if number==0: # if the random number is 0, the game ends
            print('\nYou got 0')
            print("OUT\n")
            return score  # return the final score and end the game
        elif (score+number)>=100 and mode=="Normal": # if score reaches 100, change mode to Infinite
            mode="Infinite"   # change mode to Infinite
            score+=number
            print(f"\nYou got {number}\n")
            print("----------------------------------------------------------------------------------------------------------------------")
            print("------------------You cross the Normal mode limit of 100 points! Now you are in Infinite mode!-------------------")   
            print(f"Congratulations! You Won \n Your total run is {score}")                                                            
            print("In Infinite mode, you can continue to play and accumulate points, but beware of getting a 0 which will end the game!")
            print("---------------------------------------------------------------------------------------------------------------------- ")
            input("Press enter to continue...\n")
            
            choice=ask_to_continue()  # call the function to ask player if they want to continue
            if choice==True:  # if player wants to continue
                continue  # continue the game in Infinite mode
            else:            # if player does not want to continue
                return score  # return the final score and end the game
            
        else:        # for other random numbers, add to score
            score+=number
            print(f"\n------------------You got {number} points! Your total run is {score}-------------------")
            input("Press enter to continue...\n")
            
score=main(score)  # call the main game function
print(f"\nGame Over! Your final run is {score}")
print("Thanks for playing!\n")