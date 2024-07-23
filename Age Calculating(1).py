# Display a message asking the user to press enter
input("Press Enter (2x) to continue...")

# Check if the user pressed enter (the input will be an empty string)
if input() == '':
    print("Very Good")
else:
    print("jitna bola utna kar na be")

# Ask for the user's age
a = input("Enter your age: ")
if a.isdigit():
    number = int(a)
    print("Now")

else:
    print("Age should be an integer ┬┬﹏┬┬")

# Ask for the age gap between user and father
b = input("Enter the age gap between you and your father: ")
if b.isdigit():
    number = int(b)
    print("Your Father's age is:", number + int(a))
else:
    print("Age should be an integer ┬┬﹏┬┬")

# Ask if the answer provided was correct
d = input("Did I give the correct answer? (yes/no): ")
if d.lower() == "yes":
    print("Dekhaaaa, mujhe sab pata hai! :)")
elif d.lower() == "no":
    print("Mujhe bewakoof mat samajh ~_~")
else:
    print("Jitna bola utna kar")

print ("Ab Program Khatam Ho Gya :) Bye Bye, Kisi Aur program me milenge")

#developed by m_pharkya
print (" For More Such Python codes , Stay tuned and visit!: (github.com/m-pharkya)" )
