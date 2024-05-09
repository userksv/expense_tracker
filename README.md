# **Добро пожаловать!**

## Тестовое задание: Разработка консольного приложения "Личный финансовый кошелек"

### Цель: Создать приложение для учета личных доходов и расходов.

## Основные возможности:
1. **Вывод баланса:** Показать текущий баланс, а также отдельно доходы и расходы.
2. **Добавление записи:** Возможность добавления новой записи о доходе или расходе.
3. **Редактирование записи:** Изменение существующих записей о доходах и расходах.
4. **Поиск по записям:** Поиск записей по категории, дате или сумме.
5. **Просмотреть все записи:** Просмотр всех записей.


### Запуск приложения 

    python3 main.py

### Тесты
> тестами покрыты основные методы 

    python3 tests.py

Приложение стартует показом основного меню и предложением сделать выбор комманды путем ввода номера команды:

    Главное меню
    1. Текущий баланс
    2. Добавить запись
    3. Редактировать запись
    4. Поиск
    5. Просмотреть все записи
    0. Выход
    Выберите команду: 

*У каждой опции есть подменю*

### При выборе (1. Текущий баланс) отоброжается подменю и в зависимости от выбора на экран выводится выбранный тип баланса

    1. Общий баланс
    2. Расходы
    3. Доходы

Пример вывода общего баланса:

    Выберите команду: 1

    Общий баланс: 3000
    -------------------------

### При выборе (2. Добавить запись) отоброжается подменю с предложением ввести данные для записи:

    Введите дату(Год-Месяц-День): 2024-05-05
    Введите категорию(Доход/Расход): Доход
    Введите сумму(Целое число): 5000
    Введите описание: Зарплата
    Запись добавлена.

### При выборе (3. Редактировать запись) отоброжается подменю с предложением ввести номер записи,
#### если запись найдена отоброжается подменю с предложением ввести данные для редактирования записи,
#### в противном случае выводится *'Запись не найдена'*:

    Введите номер записи для редактирования: 1
        Изменение записи: 
        Введите дату(Год-Месяц-День): 2024-10-10
        Введите категорию(Доход/Расход): Доход
        Введите сумму(Целое число): 3000
        Введите описание: Бонус
        Изменения сохранены!

### При выборе (4. Поиск) отоброжается подменю c вариантами поиска по параметрам
    
    1. Поиск по дате
    2. Поиск по категории
    3. Поиск по сумме
    Выберите команду: 3

#### Пример поиска по сумме:

        Введите сумму(Целое число): 3000
            Найденые записи:
            -------------------------
            Номер записи: 1
            Дата: 2024-10-10
            Категория: Доход
            Сумма: 3000
            Описание: Бонус
            -------------------------
            Номер записи: 5
            Дата: 2024-05-01
            Категория: Расход
            Сумма: 3000
            Описание: Food

### При выборе ( 5. Просмотреть все записи) на экран выводятся все записи если существуют

### При выборе ( 0. Выход) завершение приложения

## Каждый ввод пользователем проходит проверку на корректность формата введенных данных Если не верный формат данных, выводятся обшибки на экран и переход в 'Главное меню' 
#### Пример вывода ошибок при не корректном вводе:

    Главное меню
    1. Текущий баланс
    2. Добавить запись
    3. Редактировать запись
    4. Поиск
    5. Просмотреть все записи
    0. Выход
    -------------------------
    Выберите команду: 2

    Введите дату(Год-Месяц-День): test
    Введите категорию(Доход/Расход): test
    Введите сумму(Целое число): test
    Введите описание: test
    -------------------------
    Ошибки при вводе данных.
    -------------------------
    Недопустимое значение `суммы`, пример (Целое число)
    Неверный формат `категория`, пример (Доход/Расход)
    Недопустимый формат `даты`, пример (Год-Месяц-День)

    Главное меню
    1. Текущий баланс
    2. Добавить запись
    3. Редактировать запись
    4. Поиск
    5. Просмотреть все записи
    0. Выход
    -------------------------
    Выберите команду: 

