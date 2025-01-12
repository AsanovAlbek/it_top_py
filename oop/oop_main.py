from bank_account import BankAccount, SberAccount, AlfaAccount, TinkoffAccount, MirAccount, Account
from enum import Enum

class AccountType(Enum):
    SBER = 1
    ALFA = 2
    TINKOFF = 3
    MIR = 4

def bank_account_factory(
    name: str,
    email: str,
    password: str,
    pin: str,
    account_type: AccountType
) -> BankAccount:
    match account_type:
        case AccountType.SBER: return SberAccount(name, email, password, pin)
        case AccountType.ALFA: return AlfaAccount(name, email, password, pin)
        case AccountType.TINKOFF: return TinkoffAccount(name, email, password, pin)
        case AccountType.MIR: return MirAccount(name, email, password, pin)


ivan_accounts = []
for account_type in list(AccountType):
    print(f"type {account_type}")
    account = bank_account_factory(
        name="Ivan",
        email="ivan@example.com",
        password="ivan_password",
        pin="1234",
        account_type=account_type
    )
    ivan_accounts.append(account)

for acc in ivan_accounts:
    print(acc)


