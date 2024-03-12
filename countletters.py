# instructions: type a phrase and the computer will tell you how many letters, upper case letters, 
# lower case letters and special characters/numbers there are in your text

player_text = input(str('Enter any text: '))

lower = 0
upper = 0
numbers = 0

for i in player_text:
    # check if i is a letter
    if i.isalpha():
        # return True if is an upper case string
        test_upper = i.isupper()
        # add +1 to upper or lower variables
        if test_upper:
            upper = upper + 1
        elif not test_upper:
            lower = lower + 1
    # add +1 to numbers variable if it's now a letter
    elif not i.isalpha():
        numbers = numbers + 1

print(f'Your text have {len(player_text)} characters, there are {upper} upper case letters, {lower} lower case '
      f'letters \nand {numbers} special characters and/or numbers')
