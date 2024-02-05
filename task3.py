import cv2
import numpy as np


def open_image(file_path, image_title, image):
    """
    Открывает и отображает изображение на экране.

    Параметры:
    file_path (str) : Путь к изображению.
    image_title (str) : Название, которое будет отображаться в заголовке окна.
    image (numpy.ndarray) : Изображение для отображения.
    """
    cv2.imshow(image_title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def info_image(file_path, image):
    """
    Выводит информацию об изображении, включая его разрешение и количество каналов.

    Параметры:
    file_path (str) : Путь к изображению.
    image (numpy.ndarray) : Изображение, информацию о котором нужно отобразить.
    """
    print("Разрешение: ", image.shape[1], "x", image.shape[0])
    print("Количество каналов:", image.shape[2])


def rotate_image(file_path, image_title, image, degree_of_rotation):
    """
    Поворачивает изображение на указанное количество градусов и отображает его.

    Параметры:
    file_path (str) : Путь к изображению.
    image_title (str) : Название, которое будет отображаться в заголовке окна после поворота.
    image (numpy.ndarray) : Изображение для поворота.
    degree_of_rotation (float) : Количество градусов для поворота изображения.
    """
    (height, width) = image.shape[:2]
    (centerX, centerY) = (width // 2, height // 2)
    M = cv2.getRotationMatrix2D((centerX, centerY), degree_of_rotation, 1.0)
    rotated_image = cv2.warpAffine(image, M, (width, height))
    open_image(file_path, image_title, rotated_image)


def main():
    file_path = "data\images\pcb.jpg"
    image = cv2.imread(file_path)
    open_image(file_path, 'image', image)
    info_image(file_path, image)
    # изменение разрешения изображения
    new_resolution = (1920, 1020)
    resized_img = cv2.resize(image, new_resolution)
    open_image(file_path, 'image with the new resolution', resized_img)
    info_image(file_path, resized_img)
    # создание копии изображения
    image_first_copy = image.copy()
    # поворот изображения на 45, 90, 180 градусов
    rotate_image(file_path, 'the image is rotated by 45 degrees',
                 image_first_copy, 45)
    rotate_image(file_path, 'the image is rotated by 90 degrees',
                 image_first_copy, 90)
    rotate_image(file_path, 'the image is rotated by 180 degrees',
                 image_first_copy, 180)
    # отражение изображения по вертикали и горизонтали
    image_second_copy = image.copy()
    flipped_horizontal = cv2.flip(image_second_copy, 1)
    open_image(file_path, 'Flipped Horizontal Image', flipped_horizontal)
    flipped_vertical = cv2.flip(image_second_copy, 0)
    open_image(file_path, 'Flipped Vertical Image', flipped_vertical)
    # вырезание из изображения области размером 100x100 пикселей
    cropped_image = image[0:100, 0:100]
    open_image(file_path, 'cropped image', cropped_image)
    cv2.imwrite("data\images\cropped_pcb.jpg", cropped_image)
    new_file_path = "data\images\cropped_pcb.jpg"
    new_image = cv2.imread(new_file_path)
    (height, width) = new_image.shape[:2]
    # Проверка на четность размеров изображения
    if height % 2 == 0 and width % 2 == 0:
        # Если размеры четные, берем 4 центральных пикселя
        center_pixels = [
            new_image[height//2 - 1, width//2 - 1],
            new_image[height//2 - 1, width//2],
            new_image[height//2, width//2 - 1],
            new_image[height//2, width//2]
        ]
    else:
        # Если размеры нечетные, берем центральный пиксель
        center_pixels = [new_image[height//2, width//2]]
    # вывод значений центральных пикселей, замена их значений на (0, 0, 255)
    for i, pixel in enumerate(center_pixels):
        print(f'Центральный пиксель {i + 1}: {pixel}')
        new_image[height//2 - 1 + i//2, width//2 - 1 + i % 2] = (0, 0, 255)
        print(f'Пиксель изменен {i + 1} на (0, 0, 255)')
    open_image(new_file_path, 'new image', new_image)
    # Изменение значений группы пикселей на произвольный цвет (в данном случае синий)
    for i in range(height//2 - 10, height//2 + 10):
        for j in range(width//2 - 10, width//2 + 10):
            new_image[i, j] = (255, 0, 0)
    open_image(new_file_path,
               'The values of the pixel group have been changed to blue', new_image)
    # Отрисовка красного прямоугольника вокруг области пикселей
    cv2.rectangle(new_image, (width//2 - 10, height//2 - 10),
                  (width//2 + 10, height//2 + 10), (0, 0, 255), 2)
    open_image(new_file_path,
               'Drawing a rectangle around a pixel area', new_image)
    # Добавление текста над прямоугольником
    cv2.putText(new_image, 'rect', (width//2 - 15, height//2 - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    open_image(new_file_path,
               'image with the inscription rect', new_image)
    # Сохранение изображения в папку
    cv2.imwrite('data\save\image_with_rendered_elements.jpg', new_image)


if __name__ == "__main__":
    main()
