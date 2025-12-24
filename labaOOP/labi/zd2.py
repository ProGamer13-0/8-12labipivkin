class Car:
    
    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year
        self.wheels = 4
        self.seats = 5


    def display_info(self):
        print(f"Автомобиль: {self.brand} {self.model}, {self.year} года выпуска")


print("=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ 2 ===")


car1 = Car("Toyota", "Camry", 2022)
print("Создана первая машина:")
car1.display_info()
print(f"Детали: {car1.wheels} колеса, {car1.seats} мест")

print("\n" + "=" * 50)


car2 = Car("BMW", "X5", 2023)
print("Создана вторая машина:")
car2.display_info()
print(f"Детали: {car2.wheels} колеса, {car2.seats} мест")

print("\n" + "=" * 50)


car3 = Car("Lada", "2101", 1985)
print("Создана третья машина:")
car3.display_info()
print(f"Детали: {car3.wheels} колеса, {car3.seats} мест")

print("\n--- Сравнение созданных автомобилей ---")
print(f"car1 и car2 одинаковой марки? {car1.brand == car2.brand}")
print(f"car3 год выпуска: {car3.year}")