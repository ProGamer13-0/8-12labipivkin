class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):

        self.balance += amount
        print(f"Счет пополнен на {amount} руб. Новый баланс: {self.balance} руб.")


    def display_info(self):
        print(f"Владелец счета: {self.owner}")
        print(f"Текущий баланс: {self.balance} руб.")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято {amount} руб. Остаток на счете: {self.balance} руб.")
        else:
            print(f"Ошибка: Недостаточно средств! На счете только {self.balance} руб.")


print("=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ 3 ===")


print("1. Создание банковского счета:")
client_account = Account("Иван Иванов")
client_account.display_info()

print("\n" + "=" * 50)


print("2. Операции по пополнению счета:")
client_account.deposit(1000)
client_account.deposit(500)
client_account.deposit(200)

print("\n" + "=" * 50)


print("3. Итоговое состояние счета:")
client_account.display_info()

print("\n" + "=" * 50)


print("4. Операции по снятию денег:")
client_account.withdraw(300)
client_account.withdraw(2000)

print("\n" + "=" * 50)


print("5. Создание второго счета с начальным балансом:")
rich_account = Account("Петр Петров", 5000)
rich_account.display_info()
rich_account.deposit(1000)