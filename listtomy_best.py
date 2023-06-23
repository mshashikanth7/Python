# %%
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)

# %% [markdown]
# # the above code represents and creation and printing of the list

# %% [markdown]
# #the lists can contain multiple data types together

# %%
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

# %% [markdown]
# #From Python's perspective, lists are defined as objects with the data type 'list':

# %%
mylist = ["banana", "cherry", "grapes"]
print(type(mylist))

# %% [markdown]
# #Acessing items in list

# %%
L = ["a", "c", "d"]
print(L[1])

# %% [markdown]
# #trick to print the last item in the list just set the index to -1

# %%
thel = ["apple", "banana", "carrot", "grape", "orange"]
index = ["1", "2", "3", "4", "5"]

#now to print  from (inclusive) the range of item we can use the : between two indexe as shown below1
for i in thel:
    print(i,end= "   ")
print()
print(index)
print(thel[1:3])#prints til 3(not inculuding 3)
print("to print the elements util the index excluding index")
print(thel[:4])#prints till 4(not including 4 )
print("to print the elements from start the index to 4") 
print(thel[2:])#starts printing from 2(not including 2)

# %% [markdown]
# #note the the last element is excluseive type

# %% [markdown]
# negative indexes used to print the elements in reverse order an it starts form -1 

# %% [markdown]
# Checking for the existance of an item

# %%
thl =[ "3", "5","6", " 7"]
if "3" in thl:
    print("its there")

# %% [markdown]
# NOW MANUPALATING THE ITEMS IN THE STRING 
# 

# %%
#CHANGING THE SINGLE VALUE
list = ["appple", "mango", "guava", "carrot", "rabbit", "hobbit" ]
list[1] = "blackcurrant"
print(list)

# %%
list = ["appple", "mango", "guava", "carrot", "rabbit", "hobbit" ]
list[1:4] = ["3", "4", "5"]
print(list)

# %% [markdown]
# INSERTING AN ITEM

# %%
#inserting an item
list = ["appple", "mango", "guava", "carrot", "rabbit", "hobbit" ]
list.insert(2,"watermelon")
print(list)

# %% [markdown]
# EXTENDING THE LIST

# %%
list = ["appple", "mango", "guava", "carrot", "rabbit", "hobbit" ]
thl =[ "3", "5","6", " 7"]
list.extend(thl)
print(list)

# %% [markdown]
# THE MAIN DIFFERENCE BETWEEN LISTS AND TUPLES IS THAT LISTS US [] WHILE TUPLES USE ()
# 

# %%
tuple = ("orange ", ["pineapple", "banana", "ornage"])
thl =[ "3", "5","6", " 7"]
list = ["appple", "mango", "guava", "carrot", "rabbit", "hobbit" ]
list.extend(tuple)
print(list)
print(type(list))
#!tuple.extend(list)


# %% [markdown]
# REMOVING LIST ITEM
# 1.pop() REMOVES LAST ITEM IF () LEFT EMPTY 
# 2.remove() spefic item calling itsel from list (NO NEED OF KNOWING INDEX)
# del keyword removes the mentioned item in the list with index 
# 
# 

# %% [markdown]
#                  

# %%
list = []
for x in range(5):
    y = int(input())
    list.append(y)
    if x == 5:
        break
print(list)


