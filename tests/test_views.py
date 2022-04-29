from http import HTTPStatus

import pytest
from pytest_django.asserts import assertTemplateUsed

from .test_data import EXPECTED_POSTS

try:
    from blog import views
except ImportError:
    assert False, "Файл views.py в приложении blog отсуствует"


@pytest.mark.parametrize("post_id", (0, 1, 2))
def test_post_detail(post_id, client):
    try:
        response = client.get(f"/feed/{post_id}/")
    except Exception as e:
        assert (
            False
        ), f"""Страница `feed/<int:pk>/` работает неправильно. Ошибка: `{e}`"""

    assert (
        response.status_code != HTTPStatus.NOT_FOUND
    ), "Страница `feed/<int:pk>/` не найдена, проверьте этот адрес в *urls.py*"
    assert (
        response.context is not None
    ), "Проверьте, что передали пост в контекст страницы `feed/<int:pk>/`"
    assert EXPECTED_POSTS[post_id] == response.context["post"]


def test_post_list(client):
    try:
        response = client.get("/feed/")
    except Exception as e:
        assert False, f"""Страница `/feed/` работает неправильно. Ошибка: `{e}`"""

    assert (
        response.status_code != HTTPStatus.NOT_FOUND
    ), "Страница `/feed/` не найдена, проверьте этот адрес в *urls.py*"
    assert (
        response.context is not None
    ), "Проверьте, что передали посты в контекст страницы `/feed/`"
    assert (
        EXPECTED_POSTS[::-1] == response.context["posts"]
    ), "Посты во view post_list не инвертированы"


def test_view_post_list_use_correct_template(client):
    response = client.get("/feed/")
    assertTemplateUsed(
        response, "blog/list.html"
    ), "View post_list использует неправильный  template"


@pytest.mark.parametrize("post_id", (0, 1, 2))
def test_view_post_detail_use_correct_template(post_id, client):
    response = client.get(f"/feed/{post_id}/")
    assertTemplateUsed(
        response, "blog/detail.html"
    ), "View post_detail использует неправильный  template"


def test_view_about(client):
    try:
        response = client.get(f"/about/")
    except Exception as e:
        assert False, f"""Страница `about/` работает неправильно. Ошибка: `{e}`"""

    assert (
        response.status_code != HTTPStatus.NOT_FOUND
    ), "Страница `about/` не найдена, проверьте этот адрес в *urls.py*"
    assert (
        response.context is not None
    ), "Проверьте, что передали пост в контекст страницы `about/`"


def test_view_mission(client):
    try:
        response = client.get(f"/about/mission/")
    except Exception as e:
        assert (
            False
        ), f"""Страница `about/mission/` работает неправильно. Ошибка: `{e}`"""

    assert (
        response.status_code != HTTPStatus.NOT_FOUND
    ), "Страница `about/mission/` не найдена, проверьте этот адрес в *urls.py*"
    assert (
        response.context is not None
    ), "Проверьте, что передали пост в контекст страницы `about/mission/`"


def test_view_about_use_correct_template(client):
    response = client.get(f"/about/")
    assertTemplateUsed(
        response, "about/about.html"
    ), "View about использует неправильный  template"


def test_view_mission_use_correct_template(client):
    response = client.get(f"/about/mission/")
    assertTemplateUsed(
        response, "about/mission.html"
    ), "View mission использует неправильный  template"
