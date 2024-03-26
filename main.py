from utils.User import Settings

import logging, sys

class Main:
    def __init__(self):
        self.init_logger("./assets/logs/main.log")
        Settings.get_user()

        self.run()

    def info_message(self, text):
        text = f"[{Settings.USERNAME}] {text}"

        self.logger.info(text)

    def error_message(self, text, level=0):
        if level == 0:
            text = f"[{Settings.USERNAME}] Ошибка! {text}"
            self.logger.error(text)
        elif level == 1:
            text = f"[{Settings.USERNAME}] Фатальная ошибка! {text}"
            self.logger.error(text)
            sys.exit(1)

    def init_logger(self, log_file_path):
        # Настройка логгера
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Настройка обработчика
        self.handler = logging.FileHandler(log_file_path)
        self.handler.setLevel(logging.DEBUG)

        # Настройка форматтера
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        # Добавление обработчика к логгеру
        self.logger.addHandler(self.handler)

    def run(self):
        try:

            if not Settings.USERNAME:

                self.info_message("\nВведите ваш юзернейм как на кворке\nПример: VladimirGorin\n\n")
                username = input(">> ").replace(" ", "_")

                Settings.USERNAME = username
                Settings.set_user()

            self.info_message(f"Привет :)")

        except Exception as e:
            self.error_message(e, level=1)

if __name__ == "__main__":
    Main()

input("Нажмите ENTER что бы выйти.")
