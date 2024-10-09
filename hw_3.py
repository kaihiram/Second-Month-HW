class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры
    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    # Сеттеры
    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory

    # Метод для вычислений
    def make_computations(self):
        return f"Результат вычислений с CPU {self.__cpu} и памятью {self.__memory}: {self.__cpu + self.__memory}"

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Computer: CPU={self.__cpu}, Memory={self.__memory}"

    # Магические методы сравнения по атрибуту memory
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттер
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    # Сеттер
    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Метод звонка
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неправильный номер сим-карты")

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Phone: SIM-карты={self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод GPS
    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    # Переопределение магического метода __str__
    def __str__(self):
        return f"SmartPhone: CPU={self.get_cpu()}, Memory={self.get_memory()}, SIM-карты={self.get_sim_cards_list()}"


# Создание объектов
computer = Computer(3.5, 16)
phone = Phone(["Beeline", "Megacom"])
smartphone1 = SmartPhone(2.8, 8, ["O!", "Megacom"])
smartphone2 = SmartPhone(3.0, 12, ["Beeline", "O!"])

# Распечатка информации о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Запуск
print(computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.call(2, "+996 555 55 55 55")
smartphone1.use_gps("Центр города")

# Сравнение объектов по атрибуту
print(computer == smartphone1)
print(computer > smartphone2)
print(smartphone1 < smartphone2)
