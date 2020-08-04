#Function Exercises
#make sure you add code to each to check for good input before using the input
#also add comments with each line explaining what its doing

#Exercise 1
x = input('Input: ')
def is_two(x):
    if x == '2' or x == 2:
        return True
    else:
        return False

#Exercise 2
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
def is_vowel(char):
    if char in vowels:
        return True
    else:
        return False

#Exercise 3
def is_consonant(char):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    if char not in vowels:
        return True
    else:
        return False

#Exercise 4
def str_cap(word):
    assert type(word) == str, "Invalid input - must be string."
    if is_consonant(word[0]) and (' ' not in word):
        str[0].upper()
        return word
    else:
        return word

#Exercise 5
def calculate_tip(tip_per, bill_total):
    assert type(tip_per) == float, "Please use a float"
    assert type(bill_total) == float, "Please use a float"
    tip_amount = (tip_per * bill_total)
    return tip_amount

#Exercise 6
def apply_discount(orig_price, discount):
    return (orig_price - (orig_price * discount))

#Exercise 7
def handle_commas(str):
    assert type(string) == str
    new_num = int(str.replace(',', ''))
    return new_num

#Exercise 8
def get_letter_grade(num_grade):
    num_grade = int(num_grade)
    if num_grade >= 88:
        return "A"
    elif 80 <= num_grade < 88:
        return "B"
    elif 67 <= num_grade < 80:
        return "C"
    elif 60 <= num_grade < 67:
        return "D"
    else:
        return "F"

#Exercise 9
def remove_vowels(str):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for char in str:
        if char not in vowels:
            char.pop()
    return str

#Gabbys
def remove_vowels(str):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    chars = []
    for i in string:
        if i not in vow:
            chars.append(i)
    return joinchars
    #didnt catch the rest

#Exercise 10
def normalize_name(any_str):
    newstr = any_str.lower()
    space = ' '
    char = '!@#$%^&*'
    for string in any_str:
        if string in space:
            newstr = newstr.replace(space, '_')
    for string in any_string:
        if string in char:
            newstr = newstr.replace(string, '')
    return newstr


#Exercise 11
def cumulative_sum(list[]):
    for num in list:
        sum = list[num - 1] + list[num]

def cumulative_sum(nums_list):
    return [sum(nums_list[:i+1])] for i in range(len(nums_list))]