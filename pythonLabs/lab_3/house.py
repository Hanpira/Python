# Kласс House:
# id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица,
# Тип здания, Срок эксплуатации.
# Функции-члены реализуют запись и считывание полей
# (проверка корректности), расчета возраста задания (необходимость в кап. ремонте).
# Создать список объектов. Вывести:
# a) список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже,
# который находится в заданном промежутке;

from datetime import datetime


class House:
    _id__autoincrement = 1

    def __init__(self, flat_num, square, floor, qty_rooms, street, build_type, years_of_usage):
        self.__id = House._id__autoincrement
        House._id__autoincrement += 1
        self.__flat_num = flat_num
        self.__square = square
        self.__floor = floor
        self.__qty_rooms = qty_rooms
        self.__street = street
        self.__build_type = build_type
        self.__years_of_usage = years_of_usage

    # Methods get
    def get_flat_num(self):
        return self.__flat_num

    def get_square(self):
        return self.__square

    def get_qty_rooms(self):
        return self.__qty_rooms

    def get_street(self):
        return self.__street

    def get_build_type(self):
        return self.__build_type

    def get_years_of_usage(self):
        return self.__years_of_usage

    # Methods set
    def set_flat_num(self, flat_num):
        self.__flat_num = flat_num

    def set_square(self, square):
        self.__square = square

    def set_qty_rooms(self, qty_rooms):
        self.__qty_rooms = qty_rooms

    def set_street(self, street):
        self.__street = street

    def set_build_type(self, build_type):
        self.__build_type = build_type

    def set_years_of_usage(self, years_of_usage):
        self.__years_of_usage = years_of_usage

    @staticmethod
    def is_renovation_needed(years_of_usage):
        if years_of_usage >= 30:
            return years_of_usage
        else:
            print("The building is OK")

    @staticmethod
    def display_info_house(house):
        print(f"ID: {house.__id}. "
              f"Номер квартиры: {house.__flat_num}. "
              f"Площадь,м2: {house.__square}.\n"
              f"Этаж: {house.__floor}. "
              f"Количество комнат: {house.__qty_rooms}. "
              f"Улица: {house.__street}.\n"
              f"Тип дома: {house.__build_type}. "
              f"Срок эксплуатации: {house.__years_of_usage}.")

    @classmethod
    def display_houses_by_room_qty(cls, all_houses, rooms_count):
        rooms_qty = [house for house in all_houses if house.__qty_rooms == rooms_count]
        if rooms_qty:
            for house in rooms_qty:
                print("***")
                House.display_info_house(house)
        else:
            print(f"Квартир с таким количеством комнат ({rooms_count}) не найдено.")
        print("*****")

    @classmethod
    def display_flats_by_floor_and_qty_rooms(cls, all_houses, rooms_count, min_floor, max_floor):
        floor = [house for house in all_houses if
                 house.__qty_rooms == rooms_count and house.__floor >= min_floor and house.__floor <= max_floor]
        if floor:
            for house in floor:
                House.display_info_house(house)
        else:
            print(f"Квартир не найдено.")
        print("*****")


all_houses = [
    House(24, 80, 2, 2, "ул. Плеханова", "панельный", 15),
    House(4, 75, 1, 3, "ул. Плеханова", "панельный", 15),
    House(56, 75, 5, 3, "ул. Плеханова", "панельный", 10),
    House(36, 72, 4, 5, "ул. Захарова", "кирпичный", 3),
    House(36, 72, 4, 3, "ул. Плеханова", "панельный", 40),
    House(32, 35, 9, 1, "ул. Плеханова", "кирпичный", 29),
    House(32, 54, 4, 2, "ул. Плеханова", "кирпичный", 9),
    House(16, 90, 7, 4, "ул. Маркса", "кирпичный", 10),
    House(76, 72, 5, 3, "ул. Маркса", "монолит", 3)
]

rooms_count = int(input("Введите количество комнат: "))
House.display_houses_by_room_qty(all_houses, rooms_count)

min_floor = int(input("Введите минимально допустимый этаж: "))
max_floor = int(input("Введите минимально допустимый этаж: "))
House.display_flats_by_floor_and_qty_rooms(all_houses, rooms_count, min_floor, max_floor)
