import random

def game():
    choices = ['Камінь', 'Ножиці', 'Папір']
    player_choice = input("Виберіть Камінь, Ножиці або Папір: ").capitalize()
    computer_choice = random.choice(choices)


    print(f"Гравець вибрав: {player_choice}")
    print(f"Компʼютер вибрав: {computer_choice}")


    if player_choice == computer_choice:
        print("Нічия!")
    elif (player_choice == 'Камінь' and computer_choice == 'Ножиці') or \
            (player_choice == 'Ножиці' and computer_choice == 'Папір') or \
            (player_choice == 'Папір' and computer_choice == 'Камінь'):
        print("Гравець переміг!")
    else:
        print("Компʼютер переміг!")


while True:
    game()
    play_again = input("Хочете зіграти ще раз? (Так/Ні): ").capitalize()
    if play_again != 'Так':
        break