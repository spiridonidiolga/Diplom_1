from typing import List
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class Burger:
    def __init__(self, bun: Bun = None):
        self.bun = bun
        self.ingredients: List[Ingredient] = []

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        if 0 <= index < len(self.ingredients):
            del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        if self.bun is None:
            raise ValueError("Булочка не задана")
        price = self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self) -> str:
        if self.bun is None:
            raise ValueError("Булочка не задана")
        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']
        for ingredient in self.ingredients:
            receipt.append(f'= {ingredient.get_type().lower()} {ingredient.get_name()} =')
        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')
        return '\n'.join(receipt)
