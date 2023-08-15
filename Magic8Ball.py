import random

message = ["It is certain", "Yes definitely", "Reply hazy",
           "Ask again later", "Concentrate and ask again",
           "My reply is no", "Outlook not so good", "Very doubtful"]

print(message[random.randint(0, len(message) - 1)])