types_of_people = 10
x = f"there are {types_of_people} types of people"

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

# f string allows for string interperlation
print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False

joke_evaluation = "isnt that joke so funny?! {}"

# format string using .format() syntax
print(joke_evaluation.format(hilarious))

w = "this is the left side of..."
e = "a strin with a right side"

print(w + e)
