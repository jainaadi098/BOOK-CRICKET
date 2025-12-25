import random 
import time
import pyttsx3 


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.say(text)
    engine.runAndWait()
    

print("Enter your character's name: ")
speak("Enter your character's name: ")
name=input("" )     # get player's name

print(f'''Welcome {name} to this game!
press enter to continue...''')

speak(f'''Welcome {name} to this game!
press enter to continue...''')
input()

def random_number(): 
    return random.randint(0, 9)

def ask_to_continue():  # function to ask player if they want to continue
    while True:
        print("Do you want to continue playing? (yes/no):")
        speak("\nDo you want to continue playing? (yes/no): ")
        choice = input().strip().lower()
        
        if choice in ['yes', 'y']:
            print("\n RESTARTING GAME...\n")
            speak("\n RESTARTING GAME...\n")
            return True
        elif choice in ['no', 'n']:
            print("\n Thanks for playing!")
            speak("\n Thanks for playing!")
            return False
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.\n")
            speak("\nInvalid input. Please enter 'yes' or 'no'.\n")

def process(run,total): 
    if run==0:             
            
            print("OUT\n")
            speak("OUT\n")
            return total,"death" 
    elif (total+run)>=100:
        total+=run
        return total,"live"
    
    else:
        total+=run
        return total,"live"

def player_computer():
    player_run=0
    player_status="live"
    computer_run=0
    computer_status="live"
    
    turn=random.randint(1,2)
    
    while True:
        if turn==1:
            if player_status=="live":
                time.sleep(0.6)
                print("\n\nYour Turn")
                speak("Your Turn")
                print("Press Enter")
                speak("Press Enter")
                input()
                run=random_number()
                
                print(f"Runs : {run}")
                speak(f"Runs {run}")
                player_run,player_status=process(run,player_run)
                
                print(f"Total Runs : {player_run}")
                speak(f"Total Runs : {player_run}")
                if player_status=="death" and computer_run>player_run:
                    
                    break
                if player_run>=100:
                    print("You cross the Target")
                    speak("You cross the Target")
                    break
                elif player_run>computer_run and computer_status=="death":
                    print("You Overtake the Computer")
                    speak("You Overtake the Computer")
                    break
            turn=2
        else:
            if computer_status=="live":
                time.sleep(0.6)
                print("\n\nComputer Turn\n")
                speak("Computer Turn")
                
                
                run=random_number()
                # time.sleep(1)
                print("Runs : ",run)
                speak(f"Runs {run}")
                computer_run,computer_status=process(run,computer_run)
                print(f"Computer Total Runs : {computer_run}")
                speak(f"Computer Total Runs : {computer_run}")
                if computer_status=="death" and player_run>computer_run:
                    break
                if computer_run>=100:
                    print("\nComputer cross the Target")
                    speak("Computer cross the Target")
                    break
                elif computer_run>player_run and player_status=="death":
                    print("\nComputer Overtake You")
                    speak("Computer Overtake You")
                    break
            turn=1
        if player_status=="death" and computer_status=="death":
            print("Both Out")
            speak("Both Out")
            break
    if player_run>computer_run:
        print("You Won")
        speak("You Won")
    elif player_run<computer_run:
        print("Computer Won")
        speak("Computer Won")
    else:
        print("Match Tied")
        speak("Match Tied")

while True:
    player_computer()
    choice=ask_to_continue()
    if not choice:
        break