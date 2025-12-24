
class Product:


    def __init__(self, product_id, name, price, category="Разное", stock=0):
        # Основные атрибуты товара
        self.__product_id = product_id  # уникальный идентификатор товара
        self.__name = name  # название товара
        self.__price = price  # цена товара
        self.__category = category  # категория товара
        self.__stock = stock  # количество на складе
        self.__is_available = stock > 0  # доступен ли для покупки

    # ГЕТТЕРЫ для доступа к приватным атрибутам
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def get_stock(self):
        return self.__stock

    def is_available(self):
        return self.__is_available

    # СЕТТЕРЫ с проверками
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
            print(f"  Цена товара '{self.__name}' изменена на {new_price} руб.")
        else:
            print("  Ошибка: Цена не может быть отрицательной!")

    def set_stock(self, new_stock):
        if new_stock >= 0:
            self.__stock = new_stock
            self.__is_available = new_stock > 0
            print(f"   Количество товара '{self.__name}' на складе: {new_stock} шт.")
        else:
            print("    Ошибка: Количество не может быть отрицательным!")

    # ОСНОВНЫЕ МЕТОДЫ ТОВАРА

    def apply_discount(self, percent):
        """Применяет скидку к товару в процентах"""
        if 0 <= percent <= 100:
            discount_amount = self.__price * percent / 100
            new_price = self.__price - discount_amount
            old_price = self.__price
            self.__price = new_price
            print(f"   Скидка {percent}% применена к товару '{self.__name}'")
            print(f"   Старая цена: {old_price} руб.")
            print(f"   Новая цена: {new_price:.2f} руб.")
            print(f"   Экономия: {discount_amount:.2f} руб.")
        else:
            print("    Ошибка: Скидка должна быть от 0% до 100%!")

    def increase_price(self, percent):
        """Увеличивает цену товара на указанный процент"""
        if percent >= 0:
            increase_amount = self.__price * percent / 100
            new_price = self.__price + increase_amount
            old_price = self.__price
            self.__price = new_price
            print(f"   Цена товара '{self.__name}' увеличена на {percent}%")
            print(f"   Старая цена: {old_price} руб.")
            print(f"   Новая цена: {new_price:.2f} руб.")
        else:
            print(" Ошибка: Процент увеличения не может быть отрицательным!")

    def sell(self, quantity=1):
        """Продает указанное количество товара"""
        if quantity <= 0:
            print(" Ошибка: Количество для продажи должно быть положительным!")
            return False
        elif quantity > self.__stock:
            print(f" Ошибка: Недостаточно товара на складе! Доступно: {self.__stock} шт.")
            return False
        else:
            self.__stock -= quantity
            total_cost = self.__price * quantity
            self.__is_available = self.__stock > 0
            print(f" Продано {quantity} шт. товара '{self.__name}'")
            print(f" Общая стоимость: {total_cost:.2f} руб.")
            print(f" Остаток на складе: {self.__stock} шт.")
            return True

    def restock(self, quantity):
        """Пополняет запас товара на складе"""
        if quantity > 0:
            self.__stock += quantity
            self.__is_available = True
            print(f" Запас товара '{self.__name}' пополнен на {quantity} шт.")
            print(f" Теперь на складе: {self.__stock} шт.")
        else:
            print(" Ошибка: Количество пополнения должно быть положительным!")

    def display_info(self):
        """Выводит полную информацию о товаре"""
        status = " В наличии" if self.__is_available else "  Нет в наличии"
        print(f"\n ИНФОРМАЦИЯ О ТОВАРЕ:")
        print(f"   ID товара: {self.__product_id}")
        print(f"   Название: {self.__name}")
        print(f"   Категория: {self.__category}")
        print(f"   Цена: {self.__price:.2f} руб.")
        print(f"   На складе: {self.__stock} шт.")
        print(f"   Статус: {status}")

    def get_profit_if_sold(self, quantity):
        """Рассчитывает потенциальную прибыль от продажи"""
        if quantity <= self.__stock:
            profit = self.__price * quantity
            return profit
        else:
            return 0


# ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА
print("=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ 7 ===")
print("Собственный класс Product для информационной системы магазина\n")

# Создаем несколько товаров для демонстрации
print("1. СОЗДАНИЕ ТОВАРОВ:")
laptop = Product("P001", "Ноутбук игровой", 75000, "Электроника", 5)
book = Product("P002", "Учебник по Python", 1500, "Книги", 10)
mouse = Product("P003", "Компьютерная мышь", 2500, "Электроника", 0)

# Показываем информацию о созданных товарах
laptop.display_info()
book.display_info()
mouse.display_info()

print("\n" + "=" * 60)

# Демонстрация работы методов
print("2. ДЕМОНСТРАЦИЯ РАБОТЫ МЕТОДОВ:")

print("\n--- Применение скидки ---")
laptop.apply_discount(15)  # Скидка 15% на ноутбук

print("\n--- Продажа товаров ---")
book.sell(3)  # Продаем 3 учебника
book.sell(10)  # Пробуем продать больше чем есть

print("\n--- Пополнение запасов ---")
mouse.restock(8)  # Пополняем запас мышей
mouse.display_info()

print("\n--- Изменение цены ---")
book.set_price(1800)  # Повышаем цену учебника
book.set_price(-100)  # Пробуем установить отрицательную цену

print("\n" + "=" * 60)

# Демонстрация использования в информационной системе
print("3. ИСПОЛЬЗОВАНИЕ В ИНФОРМАЦИОННОЙ СИСТЕМЕ:")

# Создаем каталог товаров
catalog = [laptop, book, mouse]

print("\n--- Проверка доступности товаров ---")
available_products = [p for p in catalog if p.is_available()]
print(f"Доступно для покупки: {len(available_products)} товаров")

print("\n--- Расчет общей стоимости склада ---")
total_inventory_value = sum(p.get_price() * p.get_stock() for p in catalog)
print(f"Общая стоимость товаров на складе: {total_inventory_value:.2f} руб.")

print("\n--- Поиск товаров по категории ---")
electronics = [p for p in catalog if p.get_category() == "Электроника"]
print(f"Товары в категории 'Электроника': {len(electronics)}")

print("\n" + "=" * 60)

# Дополнительная демонстрация
print("4. ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ:")

# Создаем новый товар и тестируем все методы
new_product = Product("P004", "Наушники", 5000, "Электроника", 20)
new_product.display_info()

print("\n--- Полный цикл работы с товаром ---")
new_product.apply_discount(10)
new_product.sell(5)
new_product.increase_price(5)
new_product.sell(2)
new_product.restock(10)
new_product.display_info()

print("\n--- Расчет потенциальной прибыли ---")
potential_profit = new_product.get_profit_if_sold(15)
print(f"Потенциальная прибыль при продаже 15 шт.: {potential_profit:.2f} руб.")

print("\n" + "=" * 60)
print(" КЛАСС Product ГОТОВ К ИСПОЛЬЗОВАНИЮ В ИНФОРМАЦИОННОЙ СИСТЕМЕ!")