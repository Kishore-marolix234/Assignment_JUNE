#Positional arguments:
def greet(name, message):
    greeting = "Hello, {}! {}".format(name, message)
    print(greeting)
greet("Alice", "How are you?")  # Positional arguments passed based on position
#or
def greet(name, message):
    greeting = "Hello, {}! {}".format(name, message)
    return greeting

result = greet("Alice", "How are you?")  # Positional arguments passed based on position
print(result)
print("--------------------------------")

#2.Keyword arguments:
def greet(name, message):
    greeting = "Hello, {name}! {message}".format(name=name, message=message)
    print(greeting)

greet(message="How are you?", name="Bob")# Keyword arguments passed using parameter names
#or
def greet(name, message):
    greeting = "Hello, {name}! {message}".format(name=name, message=message)
    return greeting

result = greet(message="How are you?", name="Bob")# Keyword arguments passed using parameter names
print(result)
print("--------------------------------")

#3.Default arguments:
def greet(name, message="Hello"):
    greeting = "{}, {}!".format(message, name)
    print(greeting)

greet("Alice")  # Using default value for the message argument
greet("Bob", "Hi")  # Overriding the default value of the message argument
#or
def greet(name, message="Hello"):
    greeting = "{}, {}!".format(message, name)
    return greeting

print(greet("Alice"))  # Using default value for the message argument
print(greet("Bob", "Hi"))  # Overriding the default value of the message argument
print("--------------------------------")

#4.a) Variable-length arguments:
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

add(1, 2, 3, 4, 5)  # Passing multiple positional arguments
#or
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = add(1, 2, 3, 4, 5)  # Passing multiple positional arguments
print(result)
#4.b)Variable-length arguments:
def process_info(**details):
    for key, value in details.items():
        print("{}: {}".format(key, value))

process_info(name="Alice", age=25, city="New York")  # Passing multiple keyword arguments
#or
def process_info(**details):
    info = ""
    for key, value in details.items():
        info += "{}: {}\n".format(key, value)
    return info

result = process_info(name="Alice", age=25, city="New York")  # Passing multiple keyword arguments
print(result)
print("---------------END-----------------")
