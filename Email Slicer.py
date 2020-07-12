"""Python Project Idea – The email slicer is a handy program to get the username
and domain name from an email address. You can customize and send a message to
the user with this information."""

email = input("Insert your email address")
user_name = email.split("@")[0]
domain_name = email.split("@")[1]
print (f"Your username is {user_name} and your domain name is {domain_name}.")