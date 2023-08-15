# Define your functions
def coffee_bot():
    print('Welcome to the cafe!')

    size = get_size()
    print(size)


def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        return "That is not an option"


# Call coffee_bot()!
coffee_bot()
