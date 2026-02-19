import pytest
from praktikum.bun import Bun
from unittest.mock import Mock

class TestBun:
    
    def test_init_bun(self):
        bun = Bun(name="Чиабатта", price=120)
        
        assert bun.name == "Чиабатта", "Имя булочки задано неверно"
        assert bun.price == 120, "Цена булочки задана неверно"
        assert hasattr(bun, 'ingredients'), "Объект Bun должен иметь атрибут ingredients"
        assert isinstance(bun.ingredients, list), "ingredients должен быть списком"
        assert len(bun.ingredients) == 0, "Список ingredients должен быть пустым при инициализации"

    def test_get_price(self):
        bun = Bun(name="Булочка", price=100)
        assert bun.get_price() == 100, "Метод get_price() работает неверно"

    def test_get_name(self):
        bun = Bun(name="Сдобная", price=150)
        assert bun.get_name() == "Сдобная", "Метод get_name() работает неверно"

    def test_add_ingredient(self):
        bun = Bun(name="Обычная", price=80)
        ingredient = Mock()
        ingredient.price = 30
        
        bun.add_ingredient(ingredient)
        
        assert len(bun.ingredients) == 1, "После добавления длина ingredients должна быть 1"
        assert ingredient in bun.ingredients, "Ингредиент должен быть в списке ingredients"
        assert bun.price == 110, "Цена булочки должна увеличиться на цену ингредиента"

    def test_remove_ingredient(self):
        bun = Bun(name="С начинкой", price=150)
        ingredient = Mock()
        ingredient.price = 40
        
        bun.add_ingredient(ingredient)
        bun.remove_ingredient(ingredient)
        
        assert len(bun.ingredients) == 0, "После удаления ingredients должен быть пуст"
        assert bun.price == 150, "Цена должна вернуться к исходной после удаления"

    def test_add_single_ingredient(self):
        bun = Bun(name="Многослойная", price=100)
        ingredient = Mock()
        ingredient.price = 20
    
        bun.add_ingredient(ingredient)
    
        assert len(bun.ingredients) == 1, "Должен быть добавлен один ингредиент"
        assert bun.price == 120, "Цена должна увеличиться на цену ингредиента"

    def test_add_multiple_ingredients(self):
        bun = Bun(name="Многослойная", price=100)
        ingredient1 = Mock()
        ingredient1.price = 20
        ingredient2 = Mock()
        ingredient2.price = 30
    
        bun.add_ingredient(ingredient1)
        bun.add_ingredient(ingredient2)
    
        assert len(bun.ingredients) == 2, "Должны быть добавлены оба ингредиента"
        assert bun.price == 150, "Цена должна увеличиться на сумму цен ингредиентов"

    def test_remove_ingredient(self):
        bun = Bun(name="Многослойная", price=100)
        ingredient = Mock()
        ingredient.price = 20
    
        bun.add_ingredient(ingredient)
        bun.remove_ingredient(ingredient)
    
        assert len(bun.ingredients) == 0, "После удаления ингредиент должен исчезнуть"
        assert bun.price == 100, "Цена должна вернуться к исходной"

    def test_remove_multiple_ingredients(self):
        bun = Bun(name="Многослойная", price=100)
        ingredient1 = Mock()
        ingredient1.price = 20
        ingredient2 = Mock()
        ingredient2.price = 30
    
        bun.add_ingredient(ingredient1)
        bun.add_ingredient(ingredient2)
        bun.remove_ingredient(ingredient1)
    
        assert len(bun.ingredients) == 1, "Должен остаться один ингредиент"
        assert bun.price == 130, "Цена должна уменьшиться на цену удаленного ингредиента"

    def test_invalid_ingredient(self):
        bun = Bun(name="Простая", price=90)
        ingredient = Mock()
        del ingredient.price  
        
        with pytest.raises(ValueError) as excinfo:
            bun.add_ingredient(ingredient)
        assert str(excinfo.value) == "Ингредиент должен иметь атрибут price"
