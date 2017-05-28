#Лаб 2 - Логические выражения
import random

x = random.uniform(0, 80)
y = random.uniform(0, 80)
R = random.uniform(0, 100)

if (x**2 + y**2 < R**2):
	print('Точка ({:.2f}, {:.2f}) лежит ВНУТРИ окружности с радиусом {:.2f}'.format(x,y,R))
else:
	print('Точка ({:.2f}, {:.2f}) лежит СНАРУЖИ либо НА ГРАНИЦЕ окружности с радиусом {:.2f}'.format(x,y,R))
input()