import tkinter as tk


class Update:
    def __init__(self, root, label, cat_images):
        self.root = root
        self.label = label
        self.current_image_index = 0  # Индекс текущего изображения
        self.cat_images = cat_images

    def update_image(self):
        # Используем локальный атрибут current_image_index, а не глобальную переменную
        self.current_image_index = (self.current_image_index + 1) % len(self.cat_images)

        # Загружаем текущее изображение
        current_image = tk.PhotoImage(file=self.cat_images[self.current_image_index])

        # Обновляем изображение на лейбле
        self.label.config(image=current_image)
        self.label.image = current_image  # Сохраняем ссылку на фото, чтобы оно не было собрано сборщиком мусора

        # Повторный вызов функции через определенный интервал времени
        self.root.after(125, self.update_image)  # Время в миллисекундах (здесь 150 мс)


class Cat(Update):
    def __init__(self):
        self.cat_images = [
            "cat1.png", "cat2.png", "cat3.png", "cat4.png", "cat5.png",
            "cat6.png", "cat7.png", "cat8.png", "cat9.png", "cat10.png",
            "cat11.png", "cat12.png"
        ]


# Инициализация главного окна
root = tk.Tk()
root.title("Анимация")

# Создание Canvas размера 500x500 пикселей
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Создание лейбла для отображения изображений
label = tk.Label(canvas)
label.place(x=250, y=250, anchor='center')  # Размещаем лейбл по центру Canvas

# Инициализация объекта Cat
cat = Cat()

# Инициализация объекта Update и запуск анимации
updater = Update(root, label, cat.cat_images)
updater.update_image()  # Вызов первой итерации обновления изображения

# Основной цикл программы
root.mainloop()