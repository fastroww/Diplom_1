import pytest
from unittest.mock import Mock

class TestBurger:
    def test_set_buns_return_correct_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredients(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredients(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(Mock())
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price_burger(self, burger, mock_ingredient, mock_bun):
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        assert burger.get_price() == 300

    def test_get_reciept(self, burger, mock_ingredient, mock_bun):
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert "= sauce hot sauce =" in receipt
        assert "==== black ====" in receipt
        assert "300" in receipt
