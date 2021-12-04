from load import bootup, clearConsole
import colorama
import time
import sys
import random

scrollSpeed = 0.1

def scrollTxt(text):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(scrollSpeed)

bootup()
while True:
  clearConsole()
  scrollQuery = input("Scroll text? (y/n)\n")
  if scrollQuery == "y" or scrollQuery == "Yes" or scrollQuery == "Y":
    scrollTxt(colorama.Fore.GREEN + "Perfect!" + colorama.Fore.RESET)
    break
  elif scrollQuery == "n" or scrollQuery == "N" or scrollQuery == "No":
    scrollSpeed -= 0.1
    scrollTxt(colorama.Fore.GREEN + "Perfect!" + colorama.Fore.RESET)
    break
  else:
    print("Enter valid input!")
    time.sleep(1)
    continue
    
time.sleep(2)
clearConsole()