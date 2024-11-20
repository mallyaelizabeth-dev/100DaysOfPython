def greet(name, work, like): # more than one input
    # name = input("My name is: ")
    # work = input("I work at: ")
    # like = input("I like: ")
    print(f"My name is {name} I work at {work} and I like {like}")
    # print(f"I work at {work}")
    # print(f"I like {like}")
    # Functions with keyword arguments like below don't care about the position of the arguements and parameters
greet(name=input("Name: "), work=input("Work at: "), like=input("I like: "))  # functions with keyword arguments and not position