from models import *


if __name__ == '__main__':
    a = Flower('rose', 'red', 25)
    b = Bouquet('roses')
    c = Flower('pie', 'blue', 40)

    b.add_flower(a)
    b.add_flower(c)
    b.delete_flower(a)




