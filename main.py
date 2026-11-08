class ArrayApp:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.array = None


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

    
    def run(self):
        print("Программа запущена")


if __name__ == "__main__":
    ArrayApp().run()
