#1

def search(text, word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"

#2

def word_count(text):
    words = text.split()
    return len(words)

#3

def check_number_sign(number):
    if number > 0:
        return "number is valid"
    elif number < 0:
        return "number is invalid"
    else:
        return "number is 0"

#4

def even_odd_lists(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

#5

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)