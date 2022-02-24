import random
import os

def play():
    user = input("what is your choice ?  (r) for rock , (p) for paper or (s) for scissors")
    computer = random.choice(["r" , "p" , "s"])
    if user == computer:
        print("It's a tie")
        return 0
    if is_win(user , computer):
        print("You won")
        return 1 

    else :
        print("You lost")
        return -1

    
def is_win (player , opponent) :
    if (player== "r" and opponent == "s")  or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True   

def start_game():
    play_flag = True
    while play_flag:
        status = play()
        if status == 1:
            play_flag = False

start_game()