fruits = {"apple": 130, 
          "avocado": 50, 
          "kiwifruit": 90, 
          "pear": 100,
          "sweet cherries": 100}

text =  input("Item: ").lower()

if text in fruits:
    print("Calories:", fruits[text])