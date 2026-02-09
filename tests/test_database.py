import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_database_init():
    
    db = Database()
    assert len(db.buns) > 0, "В базе данных должно быть хотя бы одна булочка"
    assert len(db.ingredients) > 0, "В базе данных должен быть хотя бы один ингредиент"



