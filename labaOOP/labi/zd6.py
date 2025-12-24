class WebPage:
    def __init__(self, title):
        self.title = title  # заголовок страницы

    def show(self):
        """Базовый метод отображения страницы"""
        print(f" Заголовок страницы: {self.title}")

    def get_content(self):
        """Возвращает содержимое страницы"""
        return f"Содержимое страницы '{self.title}'"



class SpecialPage(WebPage):
    def __init__(self, title, description):
        # Вызываем конструктор родителя
        super().__init__(title)
        # Добавляем новый атрибут
        self.description = description


    def show(self):
        """Расширенный метод отображения (полиморфизм)"""
        print(f" СПЕЦИАЛЬНАЯ СТРАНИЦА")
        print(f" Заголовок: {self.title}")
        print(f" Описание: {self.description}")


    def get_content(self):
        """Расширенное содержимое"""
        return f"Специальная страница: {self.title} - {self.description}"



class NewsPage(WebPage):
    def __init__(self, title, news_text):
        super().__init__(title)
        self.news_text = news_text
        self.publish_date = "2024-01-15"


    def show(self):
        """Свой вариант отображения для новостей"""
        print(f" НОВОСТНАЯ СТРАНИЦА")
        print(f" Заголовок: {self.title}")
        print(f" Дата публикации: {self.publish_date}")
        print(f" Текст новости: {self.news_text}")


print("=== РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ 6 ===")
print("Демонстрация полиморфизма\n")


print("1. Создание страниц разных типов:")
regular_page = WebPage("Главная страница")
special_page = SpecialPage("Акции", "Скидки до 50% на все товары!")
news_page = NewsPage("Важное объявление", "Завтра технические работы")

print("\n" + "=" * 50)


print("2. Демонстрация полиморфизма - метод show():")
pages = [regular_page, special_page, news_page]

for page in pages:
    print("\n" + "-" * 30)
    page.show()

print("\n" + "=" * 50)


print("3. Демонстрация полиморфизма - метод get_content():")
for page in pages:
    content = page.get_content()
    print(f" {content}")

print("\n" + "=" * 50)


print("4. Сравнение реализации методов:")
print("Типы объектов и их методы show():")
for i, page in enumerate(pages, 1):
    print(f"{i}. {type(page).__name__}: {page.show.__qualname__}")

print("\n" + "=" * 50)


print("5. Практическое применение полиморфизма:")


def render_website(pages_list):
    """Функция, которая работает с ЛЮБЫМИ страницами благодаря полиморфизму"""
    print(" Запуск рендеринга сайта...")
    for page in pages_list:
        print("\n" + "=" * 40)
        page.show()



website_pages = [
    WebPage("О компании"),
    SpecialPage("Контакты", "Свяжитесь с нами удобным способом"),
    NewsPage("Новости", "Открытие нового филиала"),
    SpecialPage("Доставка", "Бесплатная доставка по городу")
]

render_website(website_pages)