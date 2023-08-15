import random
import array

MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Lowe_Case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

Upper_Case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

Symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
          '>', '(', ')', '<']

Combined_List = DIGITS + Upper_Case + Lowe_Case + Symbol

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(Upper_Case)
rand_lower = random.choice(Lowe_Case)
random_symbol = random.choice(Symbol)

temp_pass = rand_digit + rand_upper + rand_lower + random_symbol

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(Combined_List)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x

print(password)
