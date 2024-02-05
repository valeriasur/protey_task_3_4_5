# Задание 3
Код производит базовые операции с изображениями из разряда: чтение, сохранение изображения, ротация, отзеркаливание, изменение размера, выделение части изображения, изменение пикселя или группы пикселей, отриовка различных элементов.
# Техногии
- Python
# Использование
Для запуска программы необходимо установить все библиотеки из файла requirements.txt при помощи команды: 
```
pip install -r requirements.txt
```
Также необходимо добавить в рабочую область изображение при помощи команды:
```
name_image = cv2.imread(file_path)
```
# Окна с разными изменениями изображений
- Было выведено изображение pcb.jpg.\
![1](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/72163dee-ad95-47cc-a100-ecb64f6d8ffb)
- Было выведено изображение с новым разрешением (1920, 1020).
![2](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/7180641a-8bd7-4ce7-875d-4f9d3a81a022)
- Изображение было повернуто на 45, 90, 180 градусов.
![3](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/0cacd7ca-ee32-40c6-aac4-3a46efd81bb8)
![4](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/28ade060-5f80-43ea-adeb-562d77cb9858)
![5](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/a27d2d69-5397-4941-b26c-a19f52bc957a)
- Изображение было отражено по горизонтали и вертикали.
![6](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/b80cbc1b-92a7-4447-80d8-0fbff666b087)
![7](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/c7c99b7e-e835-45c1-924c-b69bf96547b9)
- Из изображения была вырезана область 100x100 пикселей.\
![8](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/79931d5a-47ca-48c2-b3be-68a9401419ff)
- Размеры изобржения четные, поэтому центральных пикселей 4, их значения изменены на (0, 0, 255).\
![9](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/e850ddc7-3ddd-40dc-a3b2-b13fb759b12f)
- Значение группы пикселей было изменено на синий цвет.\
![10](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/69174f7f-1201-4d4b-8c7a-6b7378253e33)
- Был отрисован красный прямоугольник вокруг области пикселей, значение которых было изменено.\
![11](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/751617b6-0333-4319-8ea9-964ca1ca7500)
- Над синим прямоугольником был добавлен текст.\
![12](https://github.com/valeriasur/protey_task_3_4_5/assets/103844758/38575e33-ed67-4f44-8ce7-a394c904a9a9)

