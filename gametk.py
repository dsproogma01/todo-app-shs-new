import tkinter as tk
import random


def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])


def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья!"
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
            (player_choice == 'ножницы' and computer_choice == 'бумага') or \
            (player_choice == 'бумага' and computer_choice == 'камень'):
        return "ПОздравляю Вы выиграли!"
    else:
        return "Вы проиграли!"


def play(player_choice):
    computer_choice = get_computer_choice()
    result = winner(player_choice, computer_choice)


    label_computer_choice.config(text=f"Компьютер выбрал: {computer_choice}")
    label_result.config(text=result)


root = tk.Tk()
root.title("Игра камень, ножницы, бумага")


label_title = tk.Label(root, text="Игра камень, ножницы, бумага", font=("Arial", 16))
label_title.pack(pady=10)

button_rock = tk.Button(root, text="камень", width=20, command=lambda: play('камень'))
button_rock.pack(pady=5)

button_scissors = tk.Button(root, text="ножницы", width=20, command=lambda: play('ножницы'))
button_scissors.pack(pady=5)

button_paper = tk.Button(root, text="бумага", width=20, command=lambda: play('бумага'))
button_paper.pack(pady=5)

label_computer_choice = tk.Label(root, text="компьютер выбрал: ", font=("Arial", 12))
label_computer_choice.pack(pady=5)

label_result = tk.Label(root, text="Результат игры: ", font=("Arial", 12))
label_result.pack(pady=5)

root.mainloop()
