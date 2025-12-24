
class Person:
    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека

    def display_info(self):
        """Выводит базовую информацию о человеке"""
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age} лет")

    def greet(self):
        """Метод приветствия"""
        print(f"Привет! Я {self.name}!")



class Student(Person):

    def __init__(self, name, age, student_id):

        super().__init__(name, age)

        self.student_id = student_id


    def display_info(self):
        """Выводит информацию о студенте (расширенная версия)"""
        print(f"Студент: {self.name}")
        print(f"Возраст: {self.age} лет")
        print(f"Студенческий билет: {self.student_id}")


    def study(self, subject):
        """Метод, который есть только у студентов"""
        print(f"Студент {self.name} изучает {subject}")


print("=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ 5 ===")
print("Демонстрация наследования классов\n")


print("1. Создание объекта Person:")
person1 = Person("Мария Иванова", 30)
person1.display_info()
person1.greet()

print("\n" + "=" * 50)


print("2. Создание объекта Student:")
student1 = Student("Алексей Петров", 20, "STU12345")
student1.display_info()
student1.greet()
student1.study("Python")

print("\n" + "=" * 50)


print("3. Создание второго студента:")
student2 = Student("Екатерина Сидорова", 22, "STU67890")
student2.display_info()
student2.study("Математику")

print("\n" + "=" * 50)


print("4. Демонстрация полиморфизма:")
people = [person1, student1, student2]

print("Все люди приветствуют:")
for person in people:
    person.greet()

print("\n" + "=" * 50)


print("5. Проверка наследования:")
print(f"student1 является экземпляром Student? {isinstance(student1, Student)}")
print(f"student1 является экземпляром Person? {isinstance(student1, Person)}")
print(f"person1 является экземпляром Student? {isinstance(person1, Student)}")
print(f"Student является подклассом Person? {issubclass(Student, Person)}")

print("\n" + "=" * 50)


print("6. Сравнение методов:")
print("Методы Person:", [method for method in dir(person1) if not method.startswith('_')])
print("Методы Student:", [method for method in dir(student1) if not method.startswith('_')])