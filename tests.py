import unittest
from models import Flower, Bouquet


class TestFlower(unittest.TestCase):

    def test_flower_creation(self):  # тесирование создания объекта
        new_name = 'Rose'
        new_color = 'red'
        new_price = 80
        new_flower = Flower(new_name, new_color, new_price)
        self.assertIsInstance(new_flower, Flower, 'Должно быть Flower')

    def test_flower_change_price(self):  # тесирование изменения цены
        new_price = 80
        new_flower = Flower('rose', 'red', new_price)
        res_price = new_flower.get_price()
        self.assertEqual(new_price, res_price, 'Должно быть 80')

        price_for_change = 85
        new_flower.set_price(price_for_change)

        res_price_2 = new_flower.get_price()
        self.assertNotEqual(res_price, res_price_2, '80 != 85')
        self.assertEqual(price_for_change, res_price_2, 'Цена должна быть 85')


class TestBouquet(unittest.TestCase):
    def setUp(self) -> None:  # объекты необходимые для проверки
        self.bouquet = Bouquet('Fantasy')
        self.flower1 = Flower('rose', 'red', 70)
        self.flower2 = Flower('alstroemeria', 'pink', 55)
        self.flower3 = Flower('eustoma', 'violet', 50)
        self.bouquet.add_flower(self.flower1)

    def test_adding_flower(self):  # при добавлении объектов другого класса будет AttributeError
        self.bouquet.add_flower(self.flower1)
        self.assertIn(self.flower1.get_name(), self.bouquet.get_flowers_names(), 'ok!!)) flower in')

    def test_delete_flower(self):  # проверка удаления объектов
        self.bouquet.add_flower(self.flower1)
        self.bouquet.add_flower(self.flower2)
        self.bouquet.delete_flower(self.flower2)
        self.bouquet.add_flower(self.flower3)

        self.assertNotIn(self.flower2.get_name(), self.bouquet.get_flowers_names(), 'Цветок не должен быть в букете')
        self.assertIn(self.flower1.get_name(), self.bouquet.get_flowers_names(), 'Цветок должен быть в букете')
        self.assertIn(self.flower3.get_name(), self.bouquet.get_flowers_names(), 'Цветок должен быть в букете')

    def test_bouquet_change_price(self):  # проверка изменения цены
        new_bouquet = Bouquet('Fantasy')
        bouquet_price = new_bouquet.get_price()

        price_for_change = 585
        new_bouquet.set_price(price_for_change)

        res_price = new_bouquet.get_price()
        self.assertNotEqual(bouquet_price, res_price, '480 != 585')
        self.assertEqual(price_for_change, res_price, 'Цена должна быть 585')

    def test_bouquet_change_name(self):  # проверка изменения названия
        new_name = 'Tenderness'
        new_bouquet = Bouquet(new_name)
        res_name = new_bouquet.get_name_b()
        self.assertEqual(new_name, res_name, 'Должно быть Tenderness')

        name_for_change = 'Fire'
        new_bouquet.set_name(name_for_change)

        res_name_2 = new_bouquet.get_name_b()
        self.assertNotEqual(res_name, res_name_2, 'Tenderness != Fire')
        self.assertEqual(name_for_change, res_name_2, 'Название должно быть Fire')


if __name__ == '__main__':
    unittest.main()
