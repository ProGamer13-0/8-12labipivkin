

class BankAccount:

    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance



    def get_balance(self):
        """Возвращает текущий баланс счета"""
        return self.__balance

    def get_owner(self):
        """Возвращает владельца счета"""
        return self.__owner



    def set_balance(self, amount):
        """Устанавливает новый баланс с проверкой"""
        if amount >= 0:
            self.__balance = amount
            print(f" Баланс установлен: {amount} руб.")
        else:
            print(f"Ошибка: Баланс не может быть отрицательным! ({amount} руб.)")

    def set_owner(self, new_owner):
        """Изменяет владельца счета"""
        if len(new_owner) > 0:
            self.__owner = new_owner
            print(f" Владелец счета изменен на: {new_owner}")
        else:
            print("Ошибка: Имя владельца не может быть пустым!")



    def deposit(self, amount):
        """Пополнение счета с проверкой"""
        if amount > 0:
            self.__balance += amount
            print(f" Счет пополнен на {amount} руб. Новый баланс: {self.__balance} руб.")
        else:
            print(f" Ошибка: Сумма пополнения должна быть положительной!")

    def withdraw(self, amount):
        """Снятие денег со счета с проверкой"""
        if amount <= 0:
            print(f" Ошибка: Сумма снятия должна быть положительной!")
        elif amount > self.__balance:
            print(f" Ошибка: Недостаточно средств! На счете: {self.__balance} руб.")
        else:
            self.__balance -= amount
            print(f" Снято {amount} руб. Остаток: {self.__balance} руб.")


    def display_info(self):
        """Показывает информацию о счете"""
        print(f"Владелец счета: {self.__owner}")
        print(f"Текущий баланс: {self.__balance} руб.")


print("=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ 4 ===")
print("Демонстрация принципа инкапсуляции\n")


print("1. Создание банковского счета:")
account = BankAccount("Анна Сидорова", 1000)
account.display_info()

print("\n" + "=" * 50)


print("2. Работа через методы доступа:")
account.deposit(500)
account.withdraw(200)
print(f"Текущий баланс (через геттер): {account.get_balance()} руб.")

print("\n" + "=" * 50)


print("3. Попытка установить некорректные значения:")
account.set_balance(-500)
account.set_balance(2000)
account.set_owner("")

print("\n" + "=" * 50)


print("4. Попытка прямого доступа к приватным атрибутам:")
try:
    print(account.__balance)
except AttributeError as e:
    print(f" Ошибка доступа: {e}")

try:
    print(account.__owner)
except AttributeError as e:
    print(f" Ошибка доступа: {e}")

print("\n" + "=" * 50)


print("5. Итоговое состояние счета:")
account.display_info()
print(f"Владелец (через геттер): {account.get_owner()}")
print(f"Баланс (через геттер): {account.get_balance()} руб.")

print("\n" + "=" * 50)


print("6. Демонстрация защиты данных:")
print("Даже если кто-то попытается изменить баланс напрямую...")
print("(раскомментируйте код выше чтобы увидеть разницу)")