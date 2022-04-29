from tests.test_data import EXPECTED_POSTS

try:
    from blog.views import posts
except ImportError:
    assert False, "список словарей(posts),который был дан в прекоде отсутсвует"


def test_posts_not_inverted():
    assert (
        EXPECTED_POSTS == posts
    ), "Структура данных post не должна быть инвертирована, инверсия должна происходить во view"
