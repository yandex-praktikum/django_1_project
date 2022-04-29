import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir_content = os.listdir(BASE_DIR)
PROJECT_DIR_NAME = "yatube"

MANAGE_PATH = os.path.join(BASE_DIR, PROJECT_DIR_NAME)
project_dir_content = os.listdir(MANAGE_PATH)
FILENAME = "manage.py"


# def test_django_version():
#     from django.utils.version import get_version

#     assert get_version() < "3.0.0", "Пожалуйста, используйте версию Django < 3.0.0"


def test_project_folder_in_place():
    if PROJECT_DIR_NAME not in root_dir_content or not os.path.isdir(
        os.path.join(BASE_DIR, PROJECT_DIR_NAME)
    ):
        assert False, (
            f"В директории `{BASE_DIR}` не найдена папка c проектом `{PROJECT_DIR_NAME}`. "
            f"Убедитесь, что у вас верная структура проекта."
        )


def test_manage_file_in_place():
    # проверяем, что структура проекта верная, и manage.py на месте
    if FILENAME not in project_dir_content:
        assert False, (
            f"В директории `{MANAGE_PATH}` не найден файл `{FILENAME}`. "
            f"Убедитесь, что у вас верная структура проекта."
        )


def test_apps_were_registered_in_INSTALLED_APPS():

    from tests.test_data import (NEW_STYLE_APP_REGISTRATION,
                                 OLD_STYLE_APP_REGISTRATION)
    from yatube.settings import INSTALLED_APPS

    assert all(app in INSTALLED_APPS for app in OLD_STYLE_APP_REGISTRATION) or all(
        app in INSTALLED_APPS for app in NEW_STYLE_APP_REGISTRATION
    ), "Пожалуйста зарегистрируйте приложения в `settings.INSTALLED_APPS`"
