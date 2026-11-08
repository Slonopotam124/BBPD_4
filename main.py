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


    # 4. Выполнение функций
    def functions_menu(self):
        if self.array is None:
            print("Массив ещё не создан.")
            return
        while True:
            print("\n--- Функции ---")
            print("1. Сумма элементов каждой строки и столбца")
            print("2. Поменять местами первый и последний столбец")
            print("3. Сумма элементов на главной диагонали")
            print("4. Заменить все элементы < суммы элементов первой строки на эту сумму")
            print("5. Сумма положительных элементов в строках без нулей")
            print("6. Назад")
            choice = input("Выбор: ").strip()
            if choice == "1":
                self._func_1()
            elif choice == "2":
                self._func_2()
            elif choice == "3":
                self._func_3()
            elif choice == "4":
                self._func_4()
            elif choice == "5":
                self._func_5()
            elif choice == "6":
                return
            else:
                print("Неверный выбор.")
                continue
            input("\nНажмите Enter для возврата...")


    def _func_1(self):
        print("\nСуммы строк:")
        for i, row in enumerate(self.array):
            print(f"  Строка {i}: {sum(row)}")
        print("Суммы столбцов:")
        for j in range(self.cols):
            col_sum = sum(self.array[i][j] for i in range(self.rows))
            print(f"  Столбец {j}: {col_sum}")


    def _func_3(self):
        n = min(self.rows, self.cols)
        diag_sum = sum(self.array[i][i] for i in range(n))
        print(f"Сумма главной диагонали: {diag_sum}")


    def _func_2(self):
        if self.cols < 2:
            print("Нужно минимум 2 столбца для обмена.")
            return
        for i in range(self.rows):
            self.array[i][0], self.array[i][-1] = self.array[i][-1], self.array[i][0]
        print("Первый и последний столбцы поменяны местами.")
        self.view_array()


    def _func_4(self):
        first_row_sum = sum(self.array[0])
        print(f"Сумма первой строки: {first_row_sum}")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] < first_row_sum:
                    self.array[i][j] = first_row_sum
        print("Элементы, меньшие суммы первой строки, заменены.")
        self.view_array()


    def _func_5(self):
        total = 0
        found = False
        for i, row in enumerate(self.array):
            if 0 not in row:
                found = True
                total += sum(x for x in row if x > 0)
        if found:
            print(f"Сумма положительных элементов в строках без нулей: {total}")
        else:
            print("Все строки содержат нули (или подходящих нет). Результат: 0")


    # 5. Главное меню и выход
    def run(self):
        while True:
            print("\n========== ГЛАВНОЕ МЕНЮ ==========")
            print("a. Ввод размера массива")
            print("b. Создание массива")
            print("c. Просмотр массива")
            print("d. Выполнение функций")
            print("e. Выход")
            choice = input("Выбор: ")
            if choice == "a":
                self.input_size()
            elif choice == "b":
                self.create_array()
            elif choice == "c":
                self.view_array()
            elif choice == "d":
                self.functions_menu()
            elif choice == "e":
                print("До свидания!")
                break
            else:
                print("Неверный выбор.")


if __name__ == "__main__":
    ArrayApp().run()
