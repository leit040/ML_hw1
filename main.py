import numpy as np
import pandas as pd


def printRes(arr, desc):
    print("<<<<!!!{}!!!>>>>>".format(desc))
    print(arr)


# Створіть масив NumPy із 10 випадкових цілих чисел. Виконайте наступні операції:
#
#     Знайдіть середнє, медіану та стандартне відхилення масиву.
#     Замініть всі парні числа у масиві на 0.

array = np.random.randint(1, 100, size=10)

print("Mean {}: ".format(array.mean()))
print("Median {}: ".format(np.median(array)))
print("STD: {} ".format(np.std(array)))

mask = array % 2 == 0
array[mask] = 0
printRes(array,"Array after")

#Створіть 2D масив NumPy (матрицю) розміром (3, 3) із випадковими цілими числами.
array2 = np.random.randint(1, 100, (3, 3))

printRes(array2, "Array")

#Виведіть перший рядок матриці.
printRes(array2[0],"First row")

#Виведіть останній стовпець матриці.
printRes(array2[:, -1],"Last column")

#Виведіть діагональні елементи матриці.
printRes(np.diag(array2),"Main Diag")
printRes(np.diag(np.fliplr(array2)),"Addishional diag")

# 3 Створіть 2D масив NumPy розміром (3, 3) та 1D масив розміром (3,).
# Використайте broadcasting для додавання 1D масиву до кожного рядка 2D масиву.

array = np.random.randint(1, 100, (3, 3))
array2 = np.random.randint(1, 100, 3)
printRes(array2+array, "broadcasting")

#4 Створіть 2D масив NumPy розміром (5, 5) з випадковими цілими числами.
array = np.random.randint(1, 100, (5, 5))

#Знайдіть та виведіть всі унікальні елементи у масиві.

printRes(np.unique(array), "Unique values")

#виведіть всі рядки, сума елементів у яких більша
# за певне значення. (значення оберіть самі)

printRes(array[np.sum(array, axis=1) > 200], "Row sum more then 300")

# 5 Створіть 1D масив NumPy, що містить цілі числа від 1 до 20 (включно).
#     Використайте оператор shape, щоб перетворити 1D масив у 2D масив розміром (4, 5).
#     Переконайтеся, що отриманий перетворений масив має бажаний розмір.

array = np.arange(1,21)
printRes(array.reshape(4, 5), "ReShape")

# pandas
#
#     Створіть DataFrame Pandas із щонайменше 5 рядками та 3 стовпцями. Стовпці можуть представляти різні атрибути (наприклад, Ім'я, Вік, Місто).

df = pd.DataFrame({
    'name': ["John Smith", "Jane Doe", "Alice Johnson", "Bob Brown", "Charlie Green"],
    'emails':  ['Oliver_Brown@gmail.com', 'Jack_Murphy@yahoo.com', 'Harry_Williams@hotmail.com', 'Jacob_Jones@protonmail.com', 'Charlie_Davies@gmail.com'],
    'city':  ['New York', 'Washington', 'Tokio','Odesa', 'Telavi']
})

printRes(df, "DataFrame")

#Додайте новий стовпець до DataFrame, який представляє числове значення.
df['age'] = [27, 45, 23, 56, 35]

printRes(df, "DataFrame")

#Відфільтруйте DataFrame, щоб показати лише рядки, де числове значення більше певного порогу (ви можете визначити поріг).
printRes(df[df.age > 30][['name', 'age', 'city']], "DataFrame")

#Завантажте набір даних за допомогою Pandas (ви можете використовувати будь-який набір даних у форматі CSV або wine.csv).

df = pd.read_csv('wine.csv', header=None, sep=',')
printRes(df, "DataFrame")

#Відобразіть перші 5 рядків набору даних.

printRes(df.head(6), "DataFrame")

#Розрахуйте та виведіть загальну статистику для числових стовпців у наборі даних.

printRes(df.sum(), "DataFrame")

#Знайдіть та виведіть унікальні значення у категорійному стовпці.

printRes(df[0].unique(), "DataFrame")
