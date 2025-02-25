import pytest
from praktikum.ingredient import Ingredient
from data import test_ingredient_data

class TestIngredient:
    @pytest.mark.parametrize("type, name, price", test_ingredient_data)
    def test_get_price_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("type, name, price", test_ingredient_data)
    def test_get_name_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("type, name, price", test_ingredient_data)
    def test_get_type_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type
