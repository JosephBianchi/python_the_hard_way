def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers")
    print("man thats enought for a party")
    print("get a blanket.\n")


print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("or we can use variables from our script")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too")
cheese_and_crackers(10 + 20, 5+6)

print("and we can comibine the two, variable an math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def what_yo_name(sex, age):
    name = input("what's your name\n")
    print(f"so i hear you're a {age} year old {sex}, and your name is {name}")


what_yo_name('male', 20 + 10)
