import random


class ArrayApp:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.array = None


    # 1. Ввод размера массива
    def input_size(self):
        try:
            self.rows = int(input("Введите количество строк: "))
            self.cols = int(input("Введите количество столбцов: "))
            if self.rows <= 0 or self.cols <= 0:
                print("Размер должен быть положительным.")
                return
            self.array = None
            print(f"Размер установлен: {self.rows} x {self.cols}")
        except ValueError:
            print("Некорректный ввод. Введите целые числа.")


    #  2. Создание массива 
    def create_array(self):
        if not self.rows or not self.cols:
            print("Сначала задайте размер (пункт меню 1).")
            return

        while True:
            print("\n--- Создание массива ---")
            print("1. Вручную")
            print("2. Автоматически (случайные 0..100)")
            print("3. Назад")
            choice = input("Выбор: ")

            if choice == "1":
                return self._create_manual()
            if choice == "2":
                return self._create_auto()
            if choice == "3":
                return
            print("Неверный выбор.")

    def _ask_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Введите целое число.")

    def _create_manual(self):
        self.array = [[self._ask_int(f"Элемент [{i}][{j}]: ") for j in range(self.cols)] for i in range(self.rows)]
        print("Массив создан вручную.")

    def _create_auto(self):
        self.array = [[random.randint(0, 100) for _ in range(self.cols)] for _ in range(self.rows)]
        print("Массив создан автоматически.")

    
    # 3. Просмотр массива 
    def view_array(self):
        if self.array is None:
            print("Массив ещё не создан.")
            return
        print("\n--- Текущий массив ---")
        for row in self.array:
            print(" ".join(f"{x:4d}" for x in row))

    
    def run(self):
        self.input_size()
        self.create_array()
        self.view_array()


if __name__ == "__main__":
    ArrayApp().run()
