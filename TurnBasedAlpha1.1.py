#Made By Nanotixx/Hanprince
#Note From Nano: If you don't type anything inside the input command, it will proceed without caution so pick 1 or 2!

import random
import colorama
from colorama import init, Fore, Back, Style
import time

Boss = 100
Player = 100
print("Welcome To TurnBased Game By Nanotixx! | Version: 1.1 Alpha")

while True:
    print("\n[HP: " + Fore.GREEN + str(Player) + Fore.WHITE + "]" + "   [Boss HP: " + Fore.RED + str(Boss) + Fore.WHITE + "]")
    
    In = input("Attack - 1 Heal - 2: ")
    
    if In == "1":
        Dice = random.randint(1, 30)
        Dice2 = random.randint(1, 10)
        Dice3 = random.randint(1, 30)
        SecretDice = random.randint(1, 1000)
        if SecretDice == 1 or SecretDice == 12:
            Boss = Boss - 1000
            print(Fore.RED + "\nBLACK FLASH! 1 out of 1000 Miracle! The Boss HP Is Now " + str(Boss) + Fore.WHITE + "\n")
            print("You Won!")
            exit()
        Boss = Boss - Dice
        print("\nYou Damaged The Boss By " + Fore.BLUE + str(Dice) + Fore.WHITE + " The Boss Health Is Now " + Fore.RED +str(Boss) + Fore.WHITE +"\n")
        if Dice > 20:
            print(Fore.GREEN + "A Critical Hit!" + Fore.WHITE)
        if Dice2 > 7:
            print("\nYou've Paralyzed The Boss! You Get Another Turn.")
            In2 = input("Attack - 1 Heal - 2: ")
            if In2 == "1":
                Boss = Boss - Dice3
                print("\nYou Damaged The Boss By " + Fore.BLUE + str(Dice3) + Fore.WHITE + " The Boss Health Is Now " + Fore.RED +str(Boss) + Fore.WHITE +"\n")
                if Dice3 > 20:
                    print(Fore.GREEN + "A Critical Hit!" + Fore.WHITE)
                
            if In2 == "2":
                Player = Player + 20
                print("You Healed, Your Health Is Now " + Fore.GREEN + str(Player) + Fore.WHITE)
        if Boss < 0 or Boss == 0:
            print("\nYou Won!")
            break
            
    if In == "2":
        Player = Player + 20
        print("You Healed, Your Health Is Now " + Fore.GREEN + str(Player) + Fore.WHITE)
    
    for Ba in range(3, 0, -1):
        print("\n" + str(Ba) + "...\n")
        time.sleep(0.8)
        BossDice1 = random.randint(1, 30)
        BossDice2 = random.randint(1, 2)
            
        if Ba == 1:
            if BossDice2 == 1:
                Player = Player - BossDice1
                print("The Boss Damaged You By " + Fore.BLUE + str(BossDice2) + Fore.WHITE + " Your Health Is Now " + Fore.GREEN + str(Player) +Fore.WHITE)
                if BossDice1 > 20:
                    print(Fore.RED + "A Critical Hit!" + Fore.WHITE)
            if BossDice2 == 2:
                Boss = Boss + 20
                print("The Boss Healed, His Health Is Now " + Fore.RED + str(Boss) + Fore.WHITE)
                 
        if Player < 0 or Player == 0:
            print("You Died.")
            exit()              