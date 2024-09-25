""" food = input("Do you like Chicken?")
if food == "yes" or "Yes" or "Yep" or "yep" or "Ye" or "ye" or "Definitely" or "definitely":
    print("correct")
else:
    print("incorrect") """

""" x = int(3)
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" x = "test"
print(f"hello {x}")  """

""" temp = input("what is the temperature?")
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" number = input("what is number")
if int(number) % 2 == 0:
    print("even")
else:
    print("odd") """

""" bill = input("how much was bill?")
print(bill)
tip = input("how good was the service? bad, okay, good , or great?")
if tip == ("bad"):
    print("0% tip")
    print(int(bill) * 1)
elif tip ==("okay"):
    print("15% tip")
    print(int(bill) * 1.15)
elif tip ==("good"):
    print("20% tip")
    print(int(bill) * 1.2)
elif tip ==("great"):
    print("25% tip")
    print(int(bill) * 1.25)
else:
    print("try again") """

""" bill = int(input("how much was bill?"))
print(bill)
tip = input("how good was the service? bad, okay, good , or great?")
if tip == ("bad"):
    print("0% tip")
    print(bill * 1)
elif tip ==("okay"):
    print("15% tip")
    print(bill * 1.15)
elif tip ==("good"):
    print("20% tip")
    print(bill * 1.2)
elif tip ==("great"):
    print("25% tip")
    print(bill * 1.25)
else:
    print("try again") """

""" sentence = input("give me a sentence")
words = sentence.split( )
wordnumber = len(words)
print(wordnumber) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
 """

""" number = (int(input("give me a number")))
for i in range(1, number + 1):
    if number % i == 0:
        print(i)

number = (int(input("give me another number")))
for i in range(1, number + 1):
    if number % i == 0:
        print(i) """


x = (int(input("give me a number")))
y = (int(input("give me another number")))
def greatest(x, y):
    if x > y:
        num = y
    else:
        num = x
    for i in range(1, num+1):
        if((x % i == 0) and (y % i == 0)):
            factor = i
    return factor
print("gcf is", greatest(x,y))
# answer = 54
# answer2 = 24
# answer = input("give me a number")
# answer2 = input("give me another number")