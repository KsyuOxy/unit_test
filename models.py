class Flower:    # класс Цветок для тестирования
    def __init__(self, name: str, color: str, price: int):
        self._name = name
        self._color = color
        self._price = price

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price
        return self._price


class Bouquet:    # класс Букет для тестирования
    def __init__(self, name: str):
        self._name = name
        self._flowers_names = []
        self._price = 0
        self._colors = []
        self._flowers = []

    def add_flower(self, flower: Flower):
        if flower in self._flowers:
            answer = input('Такой цветок уже есть в букете. Хотите добавить ещё? (y/n) - ')
            if answer == 'y':
                self._flowers.append(flower)
                self._price += flower.get_price()
            else:
                print('Ну и ладно. Баба з возу - кобыле легче))')
        else:
            self._flowers.append(flower)

    def delete_flower(self, flower: Flower):
        if flower in self._flowers:
            self._flowers.remove(flower)
            self._price -= flower.get_price()
        else:
            print('А этого цветка итак нет.')

    def get_name_b(self):
        return self._name

    def get_price(self):
        return self._price

    def get_flowers_names(self):
        for f in self._flowers:
            print(f)
            self._flowers_names.append(f.get_name())
        return self._flowers_names

    def get_colors(self):
        if len(self._flowers) == 0:
            print('Букет абсолютно прозрачен) В нём отсутствуют цветы.')
        elif len(self._flowers) == len(self._colors):
            return self._colors
        else:
            for f in self._flowers:
                self._colors.append(f.get_color())
            return self._colors

    def set_name(self, new_name):
        self._name = new_name
        return self._name

    def set_price(self, new_price):
        self._price = new_price
        return self._price

