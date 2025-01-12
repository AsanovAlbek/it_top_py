import random
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, name = "Unnamed", email = "noemail@mail.ru", password = "1234567890"):
        assert len(name.strip()) >= 2, "Имя должно быть из 2 и более букв"
        assert "@" in email, "Неверный формат электронной почты"
        assert 8 <= len(password.strip()) <= 16, "Пароль должен быть от 8 до 16 символов"
        self.__name = name
        self.__email = email
        self.__password = password

    def __str__(self) -> str:
        return f"Account(name={self.__name}, email={self.__email}, password={ "*" * len(self.__password) })"
    
    @property
    def name(self): return self.__name

    @property
    def email(self): return self.__email

    def set_name(self, name, password = None):
        assert password == self.__password, "Неверный пароль"
        print("Доступ разрешён")
        self.__name = name

    @abstractmethod
    def some_abstract_kostyl():
        pass

class BankAccount(Account, ABC):
    _bank_code: str = None

    
    def __init__(
        self, 
        name="Unnamed", 
        email="noemail@mail.ru", 
        password="1234567890",
        pin=None
    ):
        super().__init__(name, email, password)
        assert pin, "Нужно ввести пин код"
        assert len(pin) == 4, "Пин код должен быть из 4 цифр"
        self._card_number = self._generate_card_number()
        self._balance = 0.0
        self._pin = pin

    def deposit(self, money, pin = None):
        assert money > 0, "Нельзя положить отрицательную сумму"
        assert pin == self._pin, "Пин код введён неверно"
        self._balance += money

    def pay(self, money, pin = None):
        assert money > 0, "Нельзя потратить отрицательную сумму"
        assert money <= self._balance, "Недостаточно средств"
        assert pin == self._pin, "Пин код введён неверно"
        self._balance -= money

    def get_balance(self, pin = None):
        assert pin == self._pin, "Пин код введён неверно"
        return self._balance

    def _generate_card_number(self):
        card_number = ""
        for i in range(0, 4):
            if i == 0 and self._bank_code:
                card_number += self._bank_code
            else:
                card_number += str(random.randint(1000, 9999))
            if i != 3: card_number += " "
        print(f"Номер карты = {card_number}")
        return card_number
    
    def __str__(self) -> str:
        masked_card_number = self._card_number[:4] + " **** **** ****"
        return f"{super().__str__()},\nbalance = {self._balance},\npin={len(self._pin) * "*"},\ncard_number = {masked_card_number}"
    
    @abstractmethod
    def some_abstract_kostyl():
        pass


class SberAccount(BankAccount):
    _bank_code = "2200"
    def __init__(self, name="Unnamed", email="noemail@mail.ru", password="1234567890", pin=None):
        print('Создан аккаунт СБЕР')
        super().__init__(name, email, password, pin)

    def some_abstract_kostyl():
        pass

class AlfaAccount(BankAccount):
    _bank_code = "4567"

    def __init__(self, name="Unnamed", email="noemail@mail.ru", password="1234567890", pin=None):
        print('Создан аккаунт Альфа-Банка')
        super().__init__(name, email, password, pin)

    def some_abstract_kostyl():
        pass

class MirAccount(BankAccount):
    _bank_code = "2202"

    def __init__(self, name="Unnamed", email="noemail@mail.ru", password="1234567890", pin=None):
        print('Создан аккаунт МИР')
        super().__init__(name, email, password, pin)

    def some_abstract_kostyl():
        pass

class TinkoffAccount(BankAccount):
    _bank_code = "5213"

    def __init__(self, name="Unnamed", email="noemail@mail.ru", password="1234567890", pin=None):
        print('Создан аккаунт Тинькофф')
        super().__init__(name, email, password, pin)

    def some_abstract_kostyl():
        pass