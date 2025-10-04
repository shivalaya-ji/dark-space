def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    print("and, the reversed string is: ", reversed_string)


string = input("enter a string: ")
print("you've entered", string)
reverse(string)
