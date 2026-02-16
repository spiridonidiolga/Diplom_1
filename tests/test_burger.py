import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun

def test_get_price():
    bun = Bun(name="Булочка", price=100)
    burger = Burger(bun)
    
    ingredient1 = Ingredient(name="Помидор", ingredient_type="овощ", price=20)
    ingredient2 = Ingredient(name="Сыр", ingredient_type="молочный", price=50)

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    expected_price = 100 * 2 + 20 + 50
    assert burger.get_price() == expected_price, f"Неверная итоговая цена бургера. Ожидали {expected_price}, получили {burger.get_price()}"

def test_add_ingredient():
    bun = Bun(name="Булочка", price=100)
    burger = Burger(bun)
    
    ingredient = Ingredient(name="Салат", ingredient_type="зелень", price=15)
    burger.add_ingredient(ingredient)

    assert len(burger.ingredients) == 1, "Длина ingredients должна быть 1 после добавления"
    assert ingredient in burger.ingredients, "Ингредиент должен быть в ingredients"
    assert burger.get_price() == 215, "Цена бургера должна увеличиться на цену ингредиента"

def test_remove_ingredient():
    bun = Bun(name="Булочка", price=100)
    burger = Burger(bun)
    
    ingredient = Ingredient(name="Огурец", ingredient_type="овощ", price=10)
    burger.add_ingredient(ingredient)

    burger.remove_ingredient(0)  

    assert len(burger.ingredients) == 0, "ingredients должен быть пуст после удаления"
    assert burger.get_price() == 200, "Цена должна вернуться к исходной после удаления"

def test_move_ingredient():
    bun = Bun(name="Булочка", price=100)
    burger = Burger(bun)
    
    ing1 = Ingredient(name="Котлета", ingredient_type="мясо", price=80)
    ing2 = Ingredient(name="Лук", ingredient_type="овощ", price=5)
    ing3 = Ingredient(name="Томат", ingredient_type="овощ", price=15)
    
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)

    burger.move_ingredient(0, 2)  

    assert burger.ingredients[0] == ing2, "Первый ингредиент должен быть 'Лук'"
    assert burger.ingredients[1] == ing3, "Второй ингредиент должен быть 'Томат'"
    assert burger.ingredients[2] == ing1, "Третий ингредиент должен быть 'Котлета'"

def test_get_receipt():
    bun = Bun(name="Булочка классическая", price=100)
    burger = Burger(bun)
    
    ingredient1 = Ingredient(name="Котлета", ingredient_type="мясо", price=80)
    ingredient2 = Ingredient(name="Салат", ingredient_type="зелень", price=15)
    
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    receipt = burger.get_receipt()
    lines = [line.rstrip() for line in receipt.strip().split('\n') if line.strip()]  
    
    assert lines[0] == '(==== Булочка классическая ====)', "Некорректный заголовок чека"
    assert lines[-2] == '(==== Булочка классическая ====)', "Некорректный нижний заголовок чека"
    assert lines[-1].startswith('Price:'), "Строка с ценой должна начинаться с 'Price:'"
    
    assert f'= мясо Котлета =' in lines, "Котлета не найдена в чеке"
    assert f'= зелень Салат =' in lines, "Салат не найден в чеке"

