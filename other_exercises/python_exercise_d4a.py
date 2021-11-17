# 1.Create a function func() which prints a text ‘Hello World’
def func():
    print("Hello World")


func()
# 2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’


def func1(name):
    print(f"Hi, my name is {name}")


func1("google")
# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)


def func3(x, y, z: bool):
    if z:
        return x
    else:
        return y


func3("hello", "goodbye", True)

# 4.define a function func4(x,y) which returns the product of both the values.


def func4(x, y):
    return x * y


num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print(func4(num1, num2))
# 5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.


def is_even(num_in: int) -> bool:
    return num_in % 2 != 1


user_num = int(
    input("Please enter the number to test if even:  "))

print(f"is_even({user_num}) = {is_even(user_num)}")

# 6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.


def greater_than(num1_in: int, num2_in: int):
    return num1_in > num2_in


user_num1 = int(input("Please enter the first number: "))
user_num2 = int(input("Please enter the second number: "))

print(
    f"greater_than({user_num1}, {user_num2}) = {greater_than(user_num1, user_num2)}")
# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.


def conglom(nums):
    return sum(nums)


num_list1 = [1, 6, 7, 2, 45, 234, 34, 26]
print(f"Orig list: {num_list1}")
print(f"Summed: {conglom(num_list1)}")

# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.


def filter_evens(nums):
    return [n for n in nums if n % 2 == 0]


num_list2 = [1, 6, 7, 2, 45, 234, 34, 26]
print(f"Orig list: {num_list2}")
print(f"Filtered: {filter_evens(num_list2)}")

# 9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase
# <<give the python notebook exercises which are discussed  in .ipyb>>


def camel_catastrophe(text: str):
    result = ""
    for i in range(0, len(text)):
        if (i+1) % 2 == 1:
            result += text.upper()[i]
        else:
            result += text.lower()[i]
    return result


line = input("Please enter the string you'd like to camelcase:  ")
print(camel_catastrophe(line))

# 10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.


def complex_comparison(num1: int, num2: int) -> int:
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2


num1 = int(input("Please enter the first number to test: "))
num2 = int(input("Please enter the second number to test: "))

print(
    f"The result of our complex comparison is: {complex_comparison(num1, num2)}")


# 11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.

def start_the_same(text1: str, text2: str) -> bool:
    return text1.lower()[0] == text2.lower()[0]


word1 = input("Please enter the first word to compare: ")
word2 = input("Please enter the second word to compare: ")

if start_the_same(word1, word2):
    print("The two words start with the same letter.")
else:
    print("These words do not start with same letter.")

# 12.Given a value,return a value which is twice as far as other side of 7


def twice_the_other_side_of_seven(num: int) -> int:
    diff = num - 7
    return 7 + 2 * diff


number = int(
    input("Please enter the number you'd like to calculate from: "))
print(
    f"The number twice this side of seven is: {twice_the_other_side_of_seven(number)}")

# 13.A function that capitalizes first and fourth character of a word in a string.


def pre_cameling(word: str) -> str:
    result = ""
    for i in range(0, len(word)):
        if i == 0 or i == 3:
            result += word.upper()[i]
        else:
            result += word[i]
        return result


line = input("Please enter the word to pre-camel:  ")
print(pre_cameling(line))
