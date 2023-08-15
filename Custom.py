import pyinputplus as pyip

bread = pyip.inputMenu(['White', 'Wheat', 'Sourdough'], prompt='What type of bread would you like:\n')
print("You chose "+ bread)

meat = pyip.inputMenu(['Chicken', 'Turkey', 'Ham'], prompt='What type of bread would you like:\n')
print("You chose "+ meat)

prompt = "Would you like cheese?\n"
response = pyip.inputYesNo(prompt)

if response == "yes":
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    print("you chose " +cheese)

prompt2 = "would you like mayo, mustard, lettuce or tomato"
response2 = pyip.inputYesNo(prompt2)

if response2 == "yes":
    condiments = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
    print("you chose " + condiments)

howMany = pyip.inputInt()