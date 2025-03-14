# Индивидуальные занятия по Python 

Занятия нацелены на изучение Python и связанных с ним технологий.

## Описание папок:
- lessons - уроки
- tasks - задания
- solutions - решения

## Запуск на локальном компьютере
Для запуска на вашем компьютере желательно заранее создать виртуальное окружение venv.

Чтобы создать виртуальное окружение (venv) на Windows, выполните следующие шаги:

1. **Откройте командную строку**:
   - Нажмите `Win + R`, введите `cmd` и нажмите `Enter`.

2. **Перейдите в директорию, где вы хотите создать виртуальное окружение**:
   - Используйте команду `cd`, чтобы перейти в нужную папку. Например:
     ```
     cd путь\к\вашей\папке
     ```

3. **Создайте виртуальное окружение**:
   - Введите следующую команду:
     ```
     python -m venv venv
     ```

4. **Активируйте виртуальное окружение**:
   - Для активации окружения выполните следующую команду:
     ```
     venv\Scripts\activate
     ```
   - После активации вы увидите имя вашего окружения в начале строки командной строки.

5. **Установите необходимые пакеты** (по желанию):
   - Теперь вы можете устанавливать пакеты с помощью `pip`, например:
     ```
     pip install package_name
     ```

6. **Деактивируйте виртуальное окружение** (когда закончите):
   - Чтобы выйти из виртуального окружения, просто введите:
     ```
     deactivate
     ```
