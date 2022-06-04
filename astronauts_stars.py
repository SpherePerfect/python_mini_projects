print("Enter the number of stars you want - ")
entered_number = int(input())
print("Enter True or False - ")
entered_binary = str(input())

if entered_binary == "True":
    i = 0
    while i < entered_number:
        print("*"*i)
        i = i+1
elif entered_binary == "False":
    i = entered_number
    while i != 1:
        print("*" * i)
        i = i-1



