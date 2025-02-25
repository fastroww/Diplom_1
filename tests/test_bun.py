import pytest
from data import bun_test_data
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", bun_test_data)
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", bun_test_data)
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

