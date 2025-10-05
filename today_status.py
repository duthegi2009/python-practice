# Today's Status Program

# Name
name = "" #Please write your name between."

# Age
age = "" #Please write your age in between."

# Sleepiness calculation
sleepy_level = int() #If you say you're sleepy from 1 to 10, write your own level of sleep
is_sleepy = (sleepy_level >= 7)

# Result
print("\n=== Today's Status Card ===")
print("Name :", name)
print("Age :", age,"years old")

if is_sleepy: 
    print("Sleepy state: True -> sleepy right now 😴")
else: 
    print("Sleepy state: False → not sleepy yet 🙂")
