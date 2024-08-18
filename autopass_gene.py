# Hii guyzz welcome back with new python programming code
# Today we are going to learn about auto password generator by throught python code

# So let's get statered our code

import random      # it will generator randow numbers and pick in numberical num
import string      # this will allow user to give srting value like " kdb55$623kkdHGG"  like this

# this variable is used to get length of pass by choice of user
length = int(input("Enter Length: "))

def generate_password(length):

    # this will allow to pick random Alphabets(Upper & Lower Both), Numberical (1,2,3,4,....etc), punctuation(!@#$%%^^&&*). 
    char = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(char) for _ in range(length) ) 
    return password

print(f'Your Random Generate Password is: {generate_password(length)}')



                        # Thank You For Watching
                        # I hope you learn some thing from my code
                        # See you in next Video Byee Byee Tata Khatam Geya :))