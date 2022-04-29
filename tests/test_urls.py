import pytest
from about.urls import urlpatterns as about_urlpatterns
from blog.urls import urlpatterns as blog_urlpatterns
from homepage.urls import urlpatterns as homepage_urlpatterns

from yatube.urls import urlpatterns as yatube_urlpatterns


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (about_urlpatterns, ("about", "mission")),
        (blog_urlpatterns, ("post_list", "post_detail")),
        (homepage_urlpatterns, ("index",)),
    ],
)
def test_url_names(test_input, expected):
    for url, expected_url_name in zip(test_input, expected):
        assert (
            url.name == expected_url_name
        ), f"Неверный атрибут name={url.name } для url {url.pattern._route}, ожидалось {expected_url_name}"


def test_url_namespaces():
    expected_namespaces = {"blog", "homepage", "about", "admin"}
    try:
        for url in yatube_urlpatterns:
            assert (
                url.namespace in expected_namespaces
            ), f"Неверный атрибут namespace={url.namespace} для url {url.pattern._route}"
    except Exception as e:
        assert (
            False
        ), f"Что то пошло не так, возможно не был определен namespace для приложения. {e}"
