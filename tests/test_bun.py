class Bun:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.ingredients = []

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def add_ingredient(self, ingredient):
        if not hasattr(ingredient, 'price'):
            raise ValueError("Ингредиент должен иметь атрибут price")
        self.ingredients.append(ingredient)
        self.price += ingredient.price

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            self.price -= ingredient.price
