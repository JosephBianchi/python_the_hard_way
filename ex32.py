the_count = [1, 2, 3, 4]
fruits = ["apples", "oranges", "pairs", "plum"]

change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"this is count {number}")

# also we can go through mixed lists too
for fruit in fruits:
    print(f"a fruit of type: {fruit}")

# also we can go through mixed lists too notice we have to use{} since
elements = []
for i in range(0, 6):
    print(f"adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)
# now we can print them out too
for i in elements:
    print(f"element was: {i}")
