import random 
import time
import pyttsx3 

class BookCricketGame:
    
    def __init__(self):
        self.name = ""
        self.Player_run = 0
        self.Player_status = "live"
        self.text=""
        self.mode=""
        
    
    def random_number(self): 
        return random.randint(0, 9)
    
    def display_text(self):
        print(self.text)
    
    def wellcome_message(self):
        self.text=f"Hello, {self.name} "
        self.display_text()
    
    def Valid_input_name(self):
        while True:
            name=input("Enter your character's name: ").strip()
            if name:
                self.name = name
                break
            else:
                self.text="Name cannot be empty. Please enter a valid name."
                self.display_text()
    
    
    def ask_to_continue(self):  # function to ask player if they want to continue
        while True:
            choice = input("\nDo you want to continue playing? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                print("\nNow you are in Infinite mode!\n")
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                print("\nInvalid input. Please enter 'yes' or 'no'.\n")

    
    def Game_loop(self):
        self.wellcome_message()
        # game loop
        
        while self.Player_status=="live":
            number=self.random_number()
            if number==0:
                self.text="\nYou Got 0\nYou are Out"
                self.display_text()
                self.Player_status="dead"
            elif (self.Player_run+number)>=100 and self.mode=="Normal": # if score reaches 100, change mode to Infinite
                self.mode="Infinite"   # change mode to Infinite
                self.Player_run+=number
                self.text=f"""\nYou got {number}\n"
            "----------------------------------------------------------------------------------------------------------------------
            ------------------You cross the Normal mode limit of 100 points! Now you are in Infinite mode!-------------------
            Congratulations! You Won \n Your total run is {self.Player_run}                                                          
            In Infinite mode, you can continue to play and accumulate points, but beware of getting a 0 which will end the game!
            ---------------------------------------------------------------------------------------------------------------------- """
                self.display_text()
                input("Press enter to continue...\n")
            
                choice=self.ask_to_continue()  # call the function to ask player if they want to continue
                if choice==True:  # if player wants to continue
                    continue  # continue the game in Infinite mode
                else:            # if player does not want to continue
                    return self.Player_run  # return the final score and end the game
            else:
                self.Player_run+=number
                self.text=f"\n------------------You got {number} points! Your total run is {self.Player_run}-------------------"
                self.display_text()
                input("Press enter to continue...\n")
    

if __name__ == "__main__":
    
    while True:
        game=BookCricketGame()
        game.Game_loop()
        print()
        print(f"\nGame Over! Your final run is {game.Player_run}")

        print("Do you want to play again? (yes/no)")
        
        reply=input().lower()
        if reply!='yes':
            time.sleep(0.5)
            game.text="Thank you for playing."
            game.display_text()
            
            break