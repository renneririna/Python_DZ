'''
Максимальная households
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" 
в зоне минимального значения переменной min_population 
и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
'''

# Эталонное решение автотеста

import pandas as pd

df = pd.read_csv('california_housing_train.csv')
# Найти минимальное значение 'population'
min_population = df['population'].min()

# Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
max_households_in_min_population = df[df['population'] == min_population]['households'].max()

