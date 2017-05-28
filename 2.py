#Лаб 2 - Логические выражения

stage = float(input('Введите количество лет стажа числом\n\tстаж =  '))
bonus = 0
if (stage >= 5):
	if (stage < 10):
		bonus =0.02
	elif (stage < 20):
		bonus = 0.1
print('Надбавка: {}%'.format(bonus*100))
input()
