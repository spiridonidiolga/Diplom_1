import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    def test_init_ingredient(self):
        ingredient = Ingredient(
            ingredient_type="начинка",
            name="Перец",
            price=15.0
        )
        assert ingredient.type == "начинка", "Тип ингредиента задан неверно"
        assert ingredient.name == "Перец", "Имя ингредиента задано неверно"
        assert ingredient.price == 15.0, "Цена ингредиента задана неверно"

    def test_getters(self):
        ingredient = Ingredient("начинка", "Чеснок", 25.0)
        assert ingredient.get_name() == "Чеснок", "Метод get_name() работает неверно"
        assert ingredient.get_type() == "начинка", "Метод get_type() работает неверно"
        assert ingredient.get_price() == 25.0, "Метод get_price() работает неверно"

    def test_update_price(self):
        ingredient = Ingredient("начинка", "Грибы", 60.0)
        new_price = 70.0
        ingredient.price = new_price
        assert ingredient.price == new_price, "Обновление цены работает неверно"

    def test_attributes_and_types(self):
        ingredient = Ingredient("начинка", "Помидор", 20.0)
        
        
        assert hasattr(ingredient, 'type'), "У ингредиента должен быть атрибут type"
        assert hasattr(ingredient, 'name'), "У ингредиента должен быть атрибут name"
        assert hasattr(ingredient, 'price'), "У ингредиента должен быть атрибут price"
        
        
        assert isinstance(ingredient.name, str), "Атрибут name должен быть строкой"
        assert isinstance(ingredient.type, str), "Атрибут type должен быть строкой"
        assert isinstance(ingredient.price, float), "Атрибут price должен быть числом (float)"
