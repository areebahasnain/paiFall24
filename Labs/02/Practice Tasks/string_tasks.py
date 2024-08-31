# string task 1
def user_help():
    user_name = input("your good name!\n")
    print("Hello!", user_name)
    choice = input("I hope you are fine, let me know how I can help you!\n")

    if choice != "yes":
        print("Okay! Good to see you, stay connected")
    problem = input("share your problem with us\n")
    print("Thanks for your feedback, we will resolve your problem")
user_help()
print("\n")

# string task 2
def get_first_last_name(full_name):
    separated_name = full_name.split(' ')
    return separated_name[0] + " " + separated_name[-1]
print(get_first_last_name("Areeba Hasnain"))
    

