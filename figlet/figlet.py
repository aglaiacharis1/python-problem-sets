import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) ==3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
   f = sys.argv[2]
   if f not in fonts:
       sys.exit("Invalid usage")
else:
   
    sys.exit("Invalid usage")

figlet.setFont(font=f)

s = input("Input: ")

print(f"Output:\n{figlet.renderText(s)}")
