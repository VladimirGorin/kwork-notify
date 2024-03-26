from main import Main

import json

class Settings(Main):
    USERNAME = None
    USER_SESSION_PATH = None
    SETTINGS_PATH = "./assets/data/settings.json"

    @staticmethod
    def get_user():
        try:

            with open(Settings.SETTINGS_PATH, "r") as settings_file:
                settings_data = json.load(settings_file)

            if not len(settings_data):
                raise Exception("Файл настроек поврежден")

            Settings.USERNAME = settings_data.get("username")

            if Settings.USERNAME:
                Settings.USER_SESSION_PATH = f"./assets/sessions/{Settings.USERNAME}"

        except Exception as e:
            Main.error_message(text=e, level=1)

    @staticmethod
    def set_user():
        try:

            new_data = {
                "username": Settings.USERNAME
            }

            with open(Settings.SETTINGS_PATH, "w") as settings_file:
                json.dump(new_data, settings_file, indent=4)

        except Exception as e:
            Main.error_message(text=e, level=1)
