print("Welcome to love calculator!")
name1=input("What is your name?\n")
name2=input("What is their name?\n")


name=(name1.lower() + name2.lower())
trial=name.count("t")+name.count("r")+name.count("u")+name.count("e")
second_trial=name.count("l")+name.count("o")+name.count("v")+name.count("e")

#print(type(trial))

Love_Score=int(str(trial)+str(second_trial))

print(f"{Love_Score}%")
print(type(Love_Score))

if (Love_Score<=10)or(Love_Score>=90):
    print(f"Your Love score is {Love_Score}, you go together like coke and mintos.")
elif (Love_Score>=40)and(Love_Score<=50):
    print(f"Your Love score is {Love_Score}%, you are alright together.")
else:
    print(f"You Love score is {Love_Score}%.")
