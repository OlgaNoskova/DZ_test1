import pytest
from main import check_age


@pytest.mark.parametrize(
    'a,expected',
    (
            [18, 'Доступ разрешён'],
            [19, 'Доступ разрешён'],
            [17, 'Доступ запрещён'],
    )
)
def test_check_age(a, expected):
    actual = check_age(a)
    assert actual == expected
