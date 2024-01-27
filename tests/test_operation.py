import pytest

from models.operation import show_last_five_operations
from tests.setting_test_operation import TEST_DATA_1, TEST_DATA_2


@pytest.fixture
def transactions() -> list[dict]:
    return TEST_DATA_1


@pytest.fixture
def expected() -> list[dict]:
    return TEST_DATA_2


def test_show_last_five_operations(transactions: list[dict], expected: list[dict]) -> None:
    assert show_last_five_operations(transactions) == expected
