print("Welcome to the Calculator!")
print("Please choose your language")
a=input("your language: (Chinese:C, English:E)")
if a=="C" or a=="c":
    import Lan.Chinese
elif a=="E" or a=="e":
    import Lan.English
else:
    print("Your Language is not suppoted.")