
def func(greater, plus):

    i = 0
    numbers = []

    while i < greater:
        print(f"at the top i is {i}")
        numbers.append(i)

        i = i + plus
        print("Numbers now: ", numbers)

        print(f"at the bottom i is {i}")

    print("the numbers:")
    for num in numbers:
        print(num)

func(22, 5)
