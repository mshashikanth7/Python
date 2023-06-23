#while loops in python
# i =  3
# while i != 0:
#     print("meow")
#     i-= 1

#for loop in python
    #hear range is a function that careats a list of numbers over which the for loop
    #iterates

    #moreover while loop is used to validat the input\

"""while True:
    i = int(input("whats the value of i "))
    if i > 0:
        break
        """
#we can do the same in a function
def main():
    num = getinput()
    meow(num)
# main function getting input and passing it meow
def meow(i):
    for _ in range(i):
        print("meow")

def getinput():
    while True:
        x = int(input("what's the value of x?"))
        if x > 0:
            return x
        break
    #the above return statement can be written after the break statemnt just make sure that it is in the for loop as
    #  while True:
     #   x = int(input("what's the value of x?"))
     #   if x > 0:
     #       return x
     #   break

main()
#gfgfghj
