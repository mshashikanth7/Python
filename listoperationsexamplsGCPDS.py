#User
'''Write a program that asks the user to enter a list of at least five integers. Do the following:
(a)	Print out the total number of items in the list.
(b)	Print out the fourth item (index 3) in the list.
(c)	Print out the last three items in the list.
(d)	Print out all the items in the list except the first two.
(e)	Print out the list in reverse order.
(f)	Print out the largest and smallest values in the list.
(g)	Print out the sum of all the values in the list.
(h)	If the list contains a zero, print out the index of the first zero in the list, and otherwise print out a message saying there are no zeroes.
(i)	Sort the list and print out the list after sorting.
(j)	Delete the first item from the (now sorted) list and print out the new list.
(k)	Change the second-to-last item in the list to 9876 and print out the new list.
(l)	Append the value -500 to the end of the list and print out the new list.

#Test Case example:
case=t1
input=20,10,50,40,30
output=
(a) Number of items: 5
(b) Fourth item: 40
(c) Last 3 items: (50, 40, 30)
(d) Everything except first two items: (50, 40, 30)
(e) Reversed: (30, 40, 50, 10, 20)
(f) Largest: 50 Smallest: 10
(g) Sum: 150
(h) No zeroes in the list.
(i) Now sorted: [10, 20, 30, 40, 50]
(j) After deleting first item: [20, 30, 40, 50]
(k) After changing second-to-last item: [20, 30, 9876, 50]
(l) After appending -500 to list: [20, 30, 9876, 50, -500]
'''# Function to print a list with parentheses
def print_list(lst):
    print("(" + ", ".join(str(item) for item in lst) + ")")

# Get input from user
input_str = input("Enter a list of at least five integers, separated by commas: ")
input_list = [int(item.strip()) for item in input_str.split(",")]

# (a) Total number of items in the list
print("(a) Number of items:", len(input_list))

# (b) Fourth item (index 3)
print("(b) Fourth item:", input_list[3])

# (c) Last three items
print("(c) Last 3 items:", input_list[-3:])

# (d) Everything except first two items
print("(d) Everything except first two items:", input_list[2:])

# (e) Reversed list
print("(e) Reversed:", input_list[::-1])

# (f) Largest and smallest values
print("(f) Largest:", max(input_list), "Smallest:", min(input_list))

# (g) Sum of all values
print("(g) Sum:", sum(input_list))

# (h) Check for zeroes
zero_index = next((i for i, x in enumerate(input_list) if x == 0), None)
if zero_index is not None:
    print("(h) Index of first zero:", zero_index)
else:
    print("(h) No zeroes in the list.")

# (i) Sorted list
sorted_list = sorted(input_list)
print("(i) Now sorted:", sorted_list)

# (j) Delete first item from sorted list
del sorted_list[0]
print("(j) After deleting first item:", sorted_list)

# (k) Change second-to-last item
sorted_list[-2] = 9876
print("(k) After changing second-to-last item:", sorted_list)

# (l) Append -500 to the list
sorted_list.append(-500)
print("(l) After appending -500 to list:", sorted_list)


# Example list
my_list = [10, 5, 20, 15, 25]

# Find the largest number in the list
largest_number = max(my_list)

# Print the largest number
print("Largest number:", largest_number)


#&To find the smallest item larger than 10 in a list, you can iterate through the list and keep track of the smallest value that meets the condition. Here's an example:

# Example list
my_list = [5, 8, 15, 12, 20, 7]

# Initialize smallest_larger variable to a value larger than any possible element in the list
smallest_larger = float('inf')

# Iterate through the list
for item in my_list:
    if item > 10 and item < smallest_larger:
        smallest_larger = item

# Check if a value larger than 10 was found
if smallest_larger != float('inf'):
    print("Smallest item larger than 10:", smallest_larger)
else:
    print("No item larger than 10 found in the list.")

#&Riffle shuffle two lists

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D', 'E']

# Initialize the shuffled list
shuffled_list = []

# Perform the riffle shuffle
for item1, item2 in zip(list1, list2):
    shuffled_list.append(item1)
    shuffled_list.append(item2)

# Check if any remaining elements in list1
if len(list1) > len(list2):
    shuffled_list.extend(list1[len(list2):])
# Check if any remaining elements in list2
elif len(list2) > len(list1):
    shuffled_list.extend(list2[len(list1):])

# Print the shuffled list
print("Riffle shuffled list:", shuffled_list)


#&Rotate items in a list of left

# Example list
my_list = [1, 2, 3, 4, 5]

# Perform left rotation
rotated_list = my_list[1:] + [my_list[0]]

# Print the rotated list
print("Left rotated list:", rotated_list)

#& Given list of strings and list of indices create a new list of all the strings from the list that are not at those indices

# Example lists
strings = ['apple', 'banana', 'orange', 'grape', 'kiwi']
indices = [1, 3]

# Create a new list excluding strings at the specified indices
new_list = [string for index, string in enumerate(strings) if index not in indices]

# Print the new list
print("New list:", new_list)

#& count the number of strings from a given list of strings

# Example list
strings = ['apple', 'banana', 'orange', 'grape', 'kiwi']

# Count the number of strings in the list
string_count = len(strings)

# Print the count
print("Number of strings:", string_count)

#& Write a Python program to calculate the difference between the two lists.

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Calculate the difference between the two lists
difference = [item for item in list1 if item not in list2]

# Print the difference
print("Difference between list1 and list2:", difference)

#& Remove consecutive duplicates of a given list

# Example list
my_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

# Remove consecutive duplicates
new_list = [my_list[i] for i in range(len(my_list)) if i == 0 or my_list[i] != my_list[i-1]]

# Print the new list without consecutive duplicates
print("List without consecutive duplicates:", new_list)

#& Remove consecutive duplicates of a given list

# Example list
my_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

# Remove consecutive duplicates
new_list = []
for i in range(len(my_list)):
    if i == 0 or my_list[i] != my_list[i - 1]:
        new_list.append(my_list[i])

# Print the new list without consecutive duplicates
print("List without consecutive duplicates:", new_list)

