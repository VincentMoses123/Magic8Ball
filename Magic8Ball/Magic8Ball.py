import random

while True:
    print("Welcome to the magic 8 ball, type out your question, or type 'exit' to end.")
    answer = input("Type here: ")
    # Lets you type your question
    if answer.lower() == 'exit':
        print("Come back anytime!")
        break  # exit the loop if the user types 'exit'

    random_answer = random.randint(1, 12)

    if random_answer == 1:
        print("It is decidedly so.")
    elif random_answer == 2:
        print("Without a doubt.")
    elif random_answer == 3:
        print("Yes definitely.")
    elif random_answer == 4:
        print("You may rely on it.")
    elif random_answer == 5:
        print("Ask again later.")
    elif random_answer == 6:
        print("Better not tell you now.")
    elif random_answer == 7:
        print("Cannot predict now.")
    elif random_answer == 8:
        print("Concentrate and ask again.")
    elif random_answer == 9:
        print("My reply is no.")
    elif random_answer == 10:
        print("My sources say no.")
    elif random_answer == 11:
        print("Outlook not so good.")
    else:
        print("Very doubtful.")
        #ALL the diffrent answers.