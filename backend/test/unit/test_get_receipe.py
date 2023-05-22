import pytest
import random
import unittest.mock as mock
import pymongo.errors
import sys
from src.controllers.receipecontroller import ReceipeController
from src.util.dao import DAO
from src.static.diets import Diet
from src.util.calculator import calculate_readiness


# add your test case implementation here
@pytest.fixture
def mock_calculate_readiness(random_float):
    if random_float > 0.1:
        result = random_float
    result = None
    mockCalcultor = mock.MagicMock()
    mockCalcultor.calculate_readiness.return_value = result
    return result


@pytest.mark.unit
def test_get_receipe_readiness_return_readiness():

    mockedDietcontroller = mock.MagicMock()
    diet = 'normal'
    receipe = {
        "name": "Pancakes",
        "diets": [
            "normal", "vegetarian"
        ],
        "ingredients": {
            "Egg": 3,
            "Milk": 100,
            "Yoghurt": 200,
            "Flour": 150,
            "Baking Powder": 1,
            "Salt": 5,
            "Sugar": 25
        }
    }

    if diet.name.lower() not in receipe['diets']:
        assert None


    mockedDietcontroller.load_receipes.return_value = receipe


    sut = mock_calculate_readiness(0.5)
    readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == readiness



@pytest.mark.unit
def test_get_receipe_readiness_return_None():

    mockedDietcontroller = mock.MagicMock()
    diet = 'normal'
    receipe = {
        "name": "Pancakes",
        "diets": [
            "normal", "vegetarian"
        ],
        "ingredients": {
            "Egg": 3,
            "Milk": 100,
            "Yoghurt": 200,
            "Flour": 150,
            "Baking Powder": 1,
            "Salt": 5,
            "Sugar": 25
        }
    }

    if diet.name.lower() not in receipe['diets']:
        assert None


    mockedDietcontroller.load_receipes.return_value = receipe
    sut = mock_calculate_readiness(0.5)
    readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == None

