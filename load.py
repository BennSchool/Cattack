import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

from colorama import Fore
def bootup():
  print("Benneasy")
  time.sleep(.1)
  clearConsole()
  print("enneasyB")
  time.sleep(.1)
  clearConsole()
  print("nneasyBe")
  time.sleep(.1)
  clearConsole()
  print("neasyBen")
  time.sleep(.1)
  clearConsole()
  print("easyBenn")
  time.sleep(.1)
  clearConsole()
  print("asyBenne")
  time.sleep(.1)
  clearConsole()
  print("syBennea")
  time.sleep(.1)
  clearConsole()
  print("yBenneas")
  time.sleep(.1)
  clearConsole()
  print(Fore.RED + "Benneasy, 2021" + Fore.RESET)
  print('"Debating this load animation."')
  time.sleep(3)
  print("\n\n\n" + "This is a game, based in " + Fore.GREEN + "python" + Fore.RESET + ". Please, do not expect fluidity or bugless-ness. Cheers.")
  time.sleep(2)
  clearConsole()