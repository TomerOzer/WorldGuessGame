import random as r
from colorama import *
import time as t
import requests

class WorldGuessGame:
    def __init__(self, words=None):
        self.words = words
        english_words = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt").text.split("\n")
        if self.words is None:
            self.words = english_words
        else:
            self.words = self.words
        


    
    def random_word(self, max_length=None, min_length=None):
        filtered_words = [word for word in self.words if (max_length is None or len(word) <= max_length) and (min_length is None or len(word) >= min_length)]
        if filtered_words:
            return r.choice(filtered_words)
        else:
            return None

#EASY
    def play_easy(self, chosen_word):
        print(Fore.MAGENTA+"WELCOME!\nThis is the Word Guess Game!"+Fore.RESET)
        guessed_letters = []
        attempts = 20
        print(Fore.GREEN+"You have", attempts, "attempts to guess the word!"+ Fore.RESET)

        # Start playing the game!:
        while attempts > 0:
            print("Your word:", "".join([x if x in guessed_letters else Fore.CYAN+"X" +Fore.RESET for x in chosen_word]))
            print(Fore.YELLOW+"Attempts left:",  Fore.LIGHTMAGENTA_EX+str(attempts)+Fore.RESET)
            guess = input(Fore.CYAN+"Enter a letter: "+Fore.RESET).lower()
            
            #chackes if the gussed letter in the word
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in chosen_word:
                guessed_letters.append(guess)
                if all(x in guessed_letters for x in chosen_word):
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"YOU DID IT! The word is:", chosen_word+Fore.RESET)
                    return
                else:
                    print(Fore.GREEN+"Correct guess!!!"+Fore.RESET)
            else:
                print(Fore.RED+Style.BRIGHT+"Wrong guess!"+Fore.RESET)
                guessed_letters.append(guess)
                attempts -= 1

        print(Fore.RED+"Game over! You ran out of attempts. The word was:", Fore.CYAN+chosen_word+Fore.RESET)

#MEDIUM

    def play_medium(self, chosen_word):
        print(Fore.MAGENTA+"WELCOME!\nThis is the Word Guess Game!"+Fore.RESET)
        guessed_letters = []
        attempts = 15
        print(Fore.GREEN+"You have", attempts, "attempts to guess the word!"+ Fore.RESET)

        # Start playing the game!:
        while attempts > 0:
            print("Your word:", "".join([x if x in guessed_letters else Fore.CYAN+ "X" +Fore.RESET for x in chosen_word]))
            print(Fore.YELLOW+"Attempts left:",  Fore.LIGHTMAGENTA_EX+str(attempts)+Fore.RESET)
            guess = input(Fore.CYAN+"Enter a letter: "+Fore.RESET).lower()
            #chackes if the gussed letter in the word
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in chosen_word:
                guessed_letters.append(guess)
                if all(x in guessed_letters for x in chosen_word):
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"YOU DID IT! The word is:", chosen_word+Fore.RESET)
                    return
                else:
                    print(Fore.GREEN+"Correct guess!!!"+Fore.RESET)
            else:
                print(Fore.RED+Style.BRIGHT+"Wrong guess!"+Fore.RESET)
                guessed_letters.append(guess)
                attempts -= 1

        print(Fore.RED+"Game over! You ran out of attempts. The word was:", Fore.CYAN+chosen_word+Fore.RESET)
#HARD
    
    def play_hard(self, chosen_word):
        print(Fore.MAGENTA+"WELCOME!\nThis is the Word Guess Game!"+Fore.RESET)
        guessed_letters = []
        attempts = 15
        print(Fore.GREEN+"You have", attempts, "attempts to guess the word!"+ Fore.RESET)

        # Start playing the game!:
        
        while attempts > 0:
            print("Your word:", "".join([x if x in guessed_letters else Fore.CYAN+" " +Fore.RESET for x in chosen_word]))
            print(Fore.YELLOW+"Attempts left:",  Fore.LIGHTMAGENTA_EX+str(attempts)+Fore.RESET)
            guess = input(Fore.CYAN+"Enter a letter: "+Fore.RESET).lower()

            #chackes if the gussed letter in the word

            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in chosen_word:
                guessed_letters.append(guess)
                if all(x in guessed_letters for x in chosen_word):
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"YOU DID IT! The word is:", chosen_word+Fore.RESET)
                    return
                else:
                    print(Fore.GREEN+"Correct guess!!!"+Fore.RESET)
            else:
                print(Fore.RED+Style.BRIGHT+"Wrong guess!"+Fore.RESET)
                guessed_letters.append(guess)
                attempts -= 1

        print(Fore.RED+"Game over! You ran out of attempts. The word was:", Fore.CYAN+chosen_word+Fore.RESET)


#Very hard
    def play_very_hard(self, chosen_word):
        timer = 30  
        start_time = t.time()

        print(Fore.MAGENTA + "WELCOME!\nThis is the Word Guess Game!" + Fore.RESET)
        guessed_letters = []
        attempts = 15
        print(Fore.GREEN + "You have", attempts, "attempts to guess the word!" + Fore.RESET)

        # Start playing the game
        while attempts > 0:
            elapsed_time = t.time() - start_time
            remaining_time = timer - elapsed_time

            if remaining_time <= 0:
                print(Fore.RED + "Time's up!")
                print(Fore.RED + "Game over! You ran out of time!\nThe word was:", Fore.CYAN + chosen_word + Fore.RESET)
                return

            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            print(Fore.YELLOW + f"Time remaining: {minutes:02d}:{seconds:02d}" + Fore.RESET)

            print("Your word:", "".join([x if x in guessed_letters else Fore.CYAN + " " + Fore.RESET for x in chosen_word]))
            print(Fore.YELLOW + "Attempts left:", Fore.LIGHTMAGENTA_EX + str(attempts) + Fore.RESET)
            guess = input(Fore.CYAN + "Enter a letter: " + Fore.RESET).lower()

            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in chosen_word:
                guessed_letters.append(guess)
                if all(x in guessed_letters for x in chosen_word):
                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "YOU DID IT! The word is:", chosen_word + Fore.RESET)
                    return
                else:
                    print(Fore.GREEN + "Correct guess!!!" + Fore.RESET)
            else:
                print(Fore.RED + Style.BRIGHT + "Wrong guess!" + Fore.RESET)
                guessed_letters.append(guess)
                attempts -= 1

        print(Fore.RED + "Game over! You ran out of attempts. The word was:", Fore.CYAN + chosen_word + Fore.RESET)


    def run(self):
        choose_difficulty = input(Fore.MAGENTA + "Enter difficulty game level (easy/medium/hard/very hard): " + Fore.RESET).lower()

        Easy_word = self.random_word(max_length=5, min_length=1) if choose_difficulty == "easy" else self.random_word()
        Medium_word = self.random_word(max_length=7, min_length=5) if choose_difficulty == "medium" else self.random_word()
        Hard_word = self.random_word(max_length=None, min_length=6) if choose_difficulty == "hard" else self.random_word()
        Very_Hard_word = self.random_word(max_length=None, min_length=6) if choose_difficulty == "very hard" else self.random_word()

        if choose_difficulty == "easy":
            self.play_easy(Easy_word)
        elif choose_difficulty == "medium":
            self.play_medium(Medium_word)
        elif choose_difficulty == "hard":
            self.play_hard(Hard_word)
        elif choose_difficulty == "very hard":
                self.play_very_hard(Very_Hard_word)

    def run_the_game(self):
        while True:
            game.run()
            check = self.CheckIfContinue()
            if check == True:
                continue
            else:
                break

            
            

    def CheckIfContinue(self):
        while True:
            Ifcontinue = input("Do you want to continue to another game? (yes/no): ").lower()
            if Ifcontinue == "yes" or Ifcontinue == "y":
                return True
            elif Ifcontinue == "no" or Ifcontinue == "n":
                break
            else:
                print("Invalid Input, Please try again")
                self.CheckIfContinue()


if __name__ == "__main__":
    game = WorldGuessGame()


game.run_the_game()


