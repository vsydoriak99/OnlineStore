import random

from faker import Faker

from entities.base_entity import BaseEntity


class Product(BaseEntity):

    def __init__(self, name: str, color: str, price: float, category: str, gender: str,
                 brand: str, barcode: str):
        self.barcode = barcode
        self.brand = brand
        self.gender = gender
        self.category = category
        self.price = price
        self.color = color
        self.name = name

    @staticmethod
    def generateRandom():
        fake = Faker()

        brand_list = [
            'Nike',
            'Louis Vuitton',
            'Adidas',
            'Hermes',
            'Gucci', 'Tiffany & Co.', "Zara",
            " H & M ",
            "Cartier",
            "Lululemon",
            "Moncler",
            "Chanel",
            "Rolex",
            "Patek Philippe ",
            "Prada",
            "Uniqlo"]

        all_categories = {'men': ["suit", "shirt ", "tie", "coat", "jacket", "t-shirt",
                                "trousers", "jeans", "shorts",
                                "pullover", "cardigan", "sweatshirt", "jumper"],
                        'women': ["dress", "blouse", "skirt",
                                  "tanktop", "coat", "jacket", "t-shirt",
                                  "trousers", "jeans", "shorts",
                                  "pullover", "cardigan", "sweatshirt",
                                  "jumper"],
                        'baby': ['romper suit', "nappy"]}

        fake_gender = random.choice(list(all_categories.keys()))
        fake_category = random.choice(all_categories[fake_gender])
        fake_color = fake.color_name()
        return Product(
            price=fake.pyfloat(positive=True),
            barcode=fake.ean(length=13),
            brand=random.choice(brand_list),
            category=fake_category,
            color=fake_color,
            name=f'{fake_color} {fake_gender} {fake_category}',
            gender=fake_gender
        )
