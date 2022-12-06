import random



def hangman():
    word_list = ["python","java","computer","hacker","painter"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "_____      ",
              "|          ",
              "|    |     ",
              "|    O     ",
              "|  ／|＼   ",
              "|  ／ ＼   ",
              "|          "
              ]
    remaining_letters = list(word)
    letter_board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong_guesses < len(stages) -1:
        print("\n")
        guess = input("一文字を予想して入力してね ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print(" ".join(letter_board))
        print("\n".join(stages[0: wrong_guesses]))
        if "_" not in letter_board:
            print("あなたの勝ち！")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong_guesses]))
        print("あなたの負け！正解は {}.".format(word))

hangman()

