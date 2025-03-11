"""
Author:  Joshua Wright
Date: 03/07/2025
Purpose: Practice different formatting strings and user inputs in Python.

I added time to some of the lines because it can be hard navigate where your reading. I also added a 
while loop to allow the user to review the information and make any necessary changes.
"""

import time

print ("Let's create your ID Badge. I'll need some information from you to do so.")

while True:
    print ("Please enter the following information:")
    first_name = input("First name:").capitalize()
    last_name = input("Last name:").capitalize()
    email = input("Email address:").lower()
    phone = input("Phone number:")
    job_title = input("Job title:").title()
    ID_number = input("ID number:")
    hair_color = input("Hair color:").title()
    eye_color = input("Eye color:").title()
    month_started =input("Month you started:").title()
    training = input("Training completed: Yes or No:").title()
    print ("")
    print ("One moment please...")
    time.sleep(1)
    print ("")
    print ("Please review your ID Badge below:")
    time.sleep(2)
    print ("")
    print (f"{last_name}, {first_name}")
    print (f"{job_title}")
    print (f"ID: {ID_number}")
    print ("")
    print (f"{email}")
    print (f"{phone}")
    print ("")
    print (f"Hair: {hair_color}         Eyes: {eye_color}")
    print (f"Month: {month_started}      Training: {training}")
    print ("")
    time.sleep(2)
    validate = input("Is this information correct? Yes or No:").title()
    if validate ==  "Yes":
        break
    else:
            ("")
            print ("Let's try again.")
print ("")       
print ("thank you for your time. Your ID badge will be printed shortly.")



