
import string
import datetime



def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""

    for letter in input_text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift

            if new_position >= 26:
                new_position = new_position - 26

            new_letter = alphabet[new_position]
            encoded_text = encoded_text + new_letter
        else:
            encoded_text = encoded_text + letter

    return (alphabet, encoded_text)


def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ""

    for letter in input_text.lower():
        if letter in alphabet:
            old_position = alphabet.index(letter)
            new_position = old_position - shift

            if new_position < 0:
                new_position = new_position + 26

            new_letter = alphabet[new_position]
            decoded_text = decoded_text + new_letter
        else:
            decoded_text = decoded_text + letter

    return decoded_text



class BankAccount:

    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):

        if creation_date is None:
            creation_date = datetime.date.today()

        if not isinstance(creation_date, datetime.date):
            raise Exception("Creation date must be a date")

        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
        else:
            pass

        print(self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)

    def view_balance(self):
        print(self.balance)


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        account_age = (datetime.date.today() - self.creation_date).days

        if account_age < 180:
            print(self.balance)

        elif self.balance - amount < 0:
            print(self.balance)

        else:
            self.balance = self.balance - amount
            print(self.balance)


class CheckingAccount(BankAccount):

    def withdraw(self, amount):
        self.balance = self.balance - amount

        if self.balance < 0:
            self.balance = self.balance - 30

        print(self.balance)

        




        



