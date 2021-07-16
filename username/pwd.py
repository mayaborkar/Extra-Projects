def valid_name(name):
    if len(name) < 2:
        print("Your name should be more than 1 character")
        return False
    else:
        if name.isalpha():
            return True
        else:
            print("Your name should only be letters")


def get_name(text):
    get_input = True
    while get_input:
        name = input(text)
        get_input = not valid_name(name)
    return(name)


def uppercase(pwd):
    counter = 0
    for i in range(0, len(pwd)):
        if pwd[i].isupper():
            counter += 1
    if counter < 2:
        print("The password must have at least 2 upper case letters")
        input("Please input your desired password: ")

# At least 2 letters and cannot be any numbers
# main
first_name = get_name("Please input your first name: ")
last_name = get_name("Please input your last name: ")

username = input("Please input your desired username: ")
while len(username) < 8:
    print("Username must be more than 8 characters")
    username = input("Please input your desired username: ")

pwd_1 = input("Please input your desired password: ")

while len(pwd_1) < 8:
    print("Password must be more than 8 characters")
    pwd_1 = input("Please input your desired password: ")

uppercase(pwd_1)

pwd_2 = input("Please re-enter your password to confirm: ")
while pwd_1 != pwd_2:
    print("You have entered a different password please try again")
    pwd_2 = input("Please re-enter your password to confirm: ")

