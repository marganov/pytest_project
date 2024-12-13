import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Класс для управления браузером
class BrowserManager:
    def __init__(self, browser_name, user_language):
        # Инициализация атрибутов класса
        self.browser_name = browser_name  # Имя браузера (chrome или firefox)
        self.user_language = user_language  # Язык интерфейса
        self.browser = None  # Экземпляр браузера

    # Метод для запуска браузера
    def start_browser(self):
        # Проверка выбранного браузера и его инициализация
        if self.browser_name == "chrome":
            print("\nstart chrome browser for test..")  # Логирование запуска Chrome
            options = Options()  # Создание объекта опций для Chrome
            options.add_experimental_option('prefs', {'intl.accept_languages': self.user_language})  # Установка языка интерфейса
            self.browser = webdriver.Chrome(options=options)  # Инициализация Chrome с заданными опциями
        elif self.browser_name == "firefox":
            print("\nstart firefox browser for test..")  # Логирование запуска Firefox
            fp = webdriver.FirefoxProfile()  # Создание профиля для Firefox
            fp.set_preference("intl.accept_languages", self.user_language)  # Установка языка интерфейса
            self.browser = webdriver.Firefox(firefox_profile=fp)  # Инициализация Firefox с заданным профилем
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")  # Ошибка, если браузер не поддерживается

    # Метод для завершения работы браузера
    def quit_browser(self):
        if self.browser:
            print("\nquit browser...")  # Логирование завершения работы браузера
            self.browser.quit()  # Завершение работы браузера

# Функция для добавления опций командной строки в pytest
def pytest_addoption(parser):
    # Опция для выбора браузера (chrome или firefox)
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",  # Значение по умолчанию — "chrome"
        help="Choose browser: chrome or firefox"  # Подсказка для пользователя
    )
    # Опция для выбора языка интерфейса
    parser.addoption(
        "--language",
        action="store",
        default="en",  # Значение по умолчанию — английский язык
        help="Choose language: en, ru, fr, etc."  # Подсказка для пользователя
    )

# Фикстура для получения значения языка интерфейса из параметра командной строки
@pytest.fixture(scope="function")
def user_language(request):
    return request.config.getoption("--language")  # Получение значения языка из параметра командной строки

# Фикстура для инициализации и завершения работы браузера
@pytest.fixture(scope="function")
def browser(request, user_language):
    # Получение значения параметра '--browser_name' из командной строки
    browser_name = request.config.getoption("browser_name")
    # Создание экземпляра BrowserManager с заданными параметрами
    browser_manager = BrowserManager(browser_name, user_language)
    # Запуск браузера
    browser_manager.start_browser()
    # Передача управления тесту, возвращая объект браузера
    yield browser_manager.browser
    # Завершение работы браузера после выполнения теста
    browser_manager.quit_browser()
