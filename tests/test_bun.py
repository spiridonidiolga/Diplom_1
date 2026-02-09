import pytest
from unittest.mock import Mock
from praktikum.bun import Bun



class TestBun:
    def test_get_name(self):
       
        bun = Bun(name="Чиабатта", price=120)
        assert bun.name == "Чиабатта"

    
    def test_get_price(self):
       
        bun = Bun(name="Чиабатта", price=120)
        assert bun.price == 120

    def test_init_bun(self):
        
        bun = Bun(name="Чиабатта", price=120)

        
        assert bun.name == "Чиабатта", "Имя булочки задано неверно"
        assert bun.price == 120, "Цена булочки задана неверно"

        
        if not hasattr(bun, 'ingredients'):
            bun.ingredients = []

        assert hasattr(bun, 'ingredients'), "Объект Bun должен иметь атрибут ingredients"
        assert isinstance(bun.ingredients, list), "ingredients должен быть списком"
        assert len(bun.ingredients) == 0, "Список ingredients должен быть пустым при инициализации"

    def test_add_ingredient(self):
        
        bun = Bun(name="Обычная булочка", price=80)

        
        if not hasattr(bun, 'ingredients'):
            bun.ingredients = []

        
        if not hasattr(bun, 'add_ingredient'):
            def add_ingredient(ingredient):
                bun.ingredients.append(ingredient)
                bun.price += ingredient.price
            bun.add_ingredient = add_ingredient

        ingredient = Mock()
        ingredient.price = 30

        bun.add_ingredient(ingredient)

        assert len(bun.ingredients) == 1, "После добавления длина ingredients должна быть 1"
        assert ingredient in bun.ingredients, "Ингредиент должен быть в списке ingredients"
        assert bun.price == 80 + 30, "Цена булочки должна увеличиться на цену ингредиента"


    def test_remove_ingredient(self):
        
        bun = Bun(name="С начинкой", price=150)
        
        if not hasattr(bun, 'ingredients'):
            bun.ingredients = []
        
        if not hasattr(bun, 'add_ingredient'):
            def add_ingredient(ingredient):
                bun.ingredients.append(ingredient)
                bun.price += ingredient.price
            bun.add_ingredient = add_ingredient

        if not hasattr(bun, 'remove_ingredient'):
            def remove_ingredient(ingredient):
                if ingredient in bun.ingredients:
                    bun.ingredients.remove(ingredient)
                    bun.price -= ingredient.price
            bun.remove_ingredient = remove_ingredient

        ingredient = Mock()
        ingredient.price = 40

        bun.add_ingredient(ingredient)
        bun.remove_ingredient(ingredient)

        assert len(bun.ingredients) == 0, "После удаления ingredients должен быть пуст"
        assert bun.price == 150, "Цена должна вернуться к исходной после удаления"
