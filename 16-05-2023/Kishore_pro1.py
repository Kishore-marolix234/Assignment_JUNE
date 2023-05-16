username = input("Enter a username: ")#taking a username from the console.
password = input("Enter a password: ")#taking a password from the console.

while len(username) < 5 or len(password) < 8: #while length of the username is less than 5 and length of the password is less than 8 the body of loop will executed
    print("Username should be at least 5 characters long and password should be at least 8 characters long.")
    username = input("Enter a username: ")#taking username from console inside a while body
    password = input("Enter a password: ")#taking password from console inside a while body

print("Username and password created successfully!")#as soon as while condition gets false then command will come out of the loop and this statement will be executed.
