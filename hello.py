
#
#print ("hello")
#x=1
#y=2
#print (x+y)

# print 4 numbers 2 4 6 8 and end print we have 4 numbers
count = 0
for i in range(1,10):
    if i % 2 == 0:
        print (i)
        count = count + 1
    
print (f"we have {count}even numbers")


# fizz buzz rules
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 != 0) :
        print("fizz")
    elif (input % 3 != 0) and (input % 5 == 0):
        print("buzz")
    elif (input % 3 == 0) and (input % 5 == 0):
        print("fizz_buzz")
    else:
        print(input)

fizz_buzz(7)


# find the most repeated character

#from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char = sorted(char_frequency.items(), key= lambda kv:kv[1], reverse=True)

print(sorted_char[0][0])


    







      

    