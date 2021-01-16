import pytest


def get_sum(x, y):
    return x + y


@pytest.mark.parametrize(
    "x,y",
    (
            (10, 20),
            (1000000, 9999999999),
            (1, "5"),
    ),
)
def test_get_sum(
        x, y
) -> None:
    """
    Test get_sum function with different scenarios
    """
    if isinstance(x, str) or isinstance(y, str):
        with pytest.raises(TypeError):
            get_sum(x, y)
    else:
        assert get_sum(x, y) == x + y
