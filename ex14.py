from sys import argv

script, user_name, sex = argv

prompt = '> '

print(f"hi {user_name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")

print(f"what's your {sex}?")
sex_choice = input("male or female")

print(f"do you like me {user_name}")
likes = input("give me you likes now")

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is.
and you have a {computer}. nice.
Also, heard you were {sex_choice}
""")
