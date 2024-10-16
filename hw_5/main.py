from decouple import Config, config
from logic import GuessingGame

min_number = config('MIN_NUMBER', cast=int)
max_number = config('MAX_NUMBER', cast=int)
attempts = config('ATTEMPTS', cast=int)
initial_balance = config('INITIAL_BALANCE', cast=int)


def main():
    print("Добро пожаловать в игру 'Угадай число'!")

    game = GuessingGame(min_number, max_number, attempts, initial_balance)

    for attempt in range(attempts):
        print(f"Текущий баланс: {game.get_balance()}")
        try:
            guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
            bet = int(input("Введите вашу ставку: "))
            guessed, winnings = game.make_guess(guess, bet)

            if guessed:
                print(f"Поздравляем! Вы угадали число и выиграли {winnings}. Ваш новый баланс: {game.get_balance()}")
                break
            else:
                print(f"Вы не угадали! Остаток вашего баланса: {game.get_balance()}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    print(f"Игра окончена. Ваш итоговый баланс: {game.get_balance()}")


if __name__ == '__main__':
    main()
