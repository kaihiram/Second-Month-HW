import random

class GuessingGame:
    def __init__(self, min_number, max_number, attempts, initial_balance):
        self.min_number = min_number
        self.max_number = max_number
        self.attempts = attempts
        self.balance = initial_balance
        self.target_number = random.randint(self.min_number, self.max_number)

    def make_guess(self, guess, bet):
        if bet > self.balance:
            raise ValueError("Ставка не может превышать текущий баланс.")
        self.balance -= bet
        if guess == self.target_number:
            winnings = bet * 2
            self.balance += winnings
            return True, winnings
        else:
            return False, 0

    def get_balance(self):
        return self.balance
