import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_______",
              "|",
              "|      |",
              "|      0",
              "|     /|\ ",
              "|     / \ ",
              "|"
              ]
    separate_list = list(word)
    hint_list = ["_"] * len(word)

    while True:
        inp = input("入力:")
        if inp in separate_list:
            n = separate_list.index(inp)
            hint_list[n] = inp
            separate_list[n] = "$"
            print(hint_list)
        else:
            wrong += 1
            print("\n".join(stages[:wrong+1]))

        if wrong > len(stages) - 2:
            print("\n".join(stages))
            print("You lose! The answer is '{}'!".format(word))
            break

        if "_" not in hint_list:
            print("You've guessed '{}' correctly!".format(word))
            break

word_list = ["alpha","beta","charlie","delta""epsilon"]
a = random.choice(word_list)
hangman(a)
