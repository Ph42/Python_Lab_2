#Лаб 2 - Логические выражения
import random

a = random.uniform(0, 300)
b = random.uniform(0, 150)
c = random.uniform(0, 100)
x = random.uniform(0, 300)
y = random.uniform(0, 200)

def compare(a, b, x, y):
	yes = False
	if (a <= x) and (b<=y) or (b <= x) and (a <= y):
		yes = True
	return yes	
if compare(a,b,x,y) or compare(a,c,x,y) or compare(b,c,x,y):
	print('Кирпич размерами {:.2f} x {:.2f} x {:.2f} ПРОЙДЁТ в отверстие размерами {:.2f} x {:.2f}'.format(a,b,c,x,y))
else:
	print('Кирпич размерами {:.2f} x {:.2f} x {:.2f} НЕ ПРОЙДЁТ в отверстие размерами {:.2f} x {:.2f}'.format(a,b,c,x,y))
input()