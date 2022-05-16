import random, sys
from colorama import Fore, Back, Style
from colorama import init

# инициализация библиотеки colorama
init(autoreset=True)

logo = '''
==================================================
||| КОМПЬЮТЕРНАЯ ИГРА: КАМЕНЬ, НОЖНИЦЫ, БУМАГА |||
==================================================
'''

print(Style.BRIGHT + Fore.CYAN + logo)

wins = 0
losses = 0
ties = 0
totalGames = 0

while True:
	print(f'''победа = {wins}\nпоражение = {losses}\nничья = {ties}\nвсего сыграно игр = {totalGames}\n''')
	
	while True:
		print('Выберите: камень(r), нижницы(s), бумагу(p) или выход из игры(q)')
		stepPlayer = input('Ваш выбор: ')
		if stepPlayer == 'q':
			sys.exit()
		if stepPlayer == 'r' or stepPlayer == 's' or stepPlayer == 'p':
			break
		print('Выберите правильное значение: (r),(s),(p) или (q)')
	
	# шаг игрока
	if stepPlayer == 'r':
		print('Игрок выбрал: КАМЕНЬ')
	elif stepPlayer == 's':
		print('Игрок выбрал НОЖНИЦЫ')
	elif stepPlayer == 'p':
		print('Игрок выбрал БУМАГУ')
	
	# шаг программы
	stepComputer = random.randint(1,3)
	if stepComputer == 1:
		stepComputer = 'r'
		print(f'Компьютер выбрал КАМЕНЬ\n')
	elif stepComputer == 2:
		stepComputer = 'p'
		print(f'Компьютер выбрал БУМАГУ\n')
	elif stepComputer == 3:
		stepComputer = 's'
		print(f'Компьютер выбрал НОЖНИЦЫ\n')

	# результат игры и статистика игр
	if stepPlayer == stepComputer:
		print(Style.BRIGHT + Fore.YELLOW + f'НИЧЬЯ ;)\n')
		ties = ties + 1
		totalGames = totalGames + 1
	elif stepPlayer == 'r' and stepComputer =='s':
		print(Style.BRIGHT + Fore.GREEN + f'ПОБЕДА !!!\n')
		wins = wins + 1
		totalGames = totalGames + 1
	elif stepPlayer == 'p' and stepComputer =='r':
		print(Style.BRIGHT + Fore.GREEN + f'ПОБЕДА !!!\n')
		wins = wins + 1
		totalGames = totalGames + 1
	elif stepPlayer == 's' and stepComputer =='p':
		print(Style.BRIGHT + Fore.GREEN + f'ПОБЕДА !!!\n')
		wins = wins + 1
		totalGames = totalGames + 1
	elif stepPlayer == 'r' and stepComputer =='p':
		print(Style.BRIGHT + Fore.RED + f'ПОРАЖЕНИЕ (-;\n')
		losses = losses + 1
		totalGames = totalGames + 1
	elif stepPlayer == 'p' and stepComputer =='s':
		print(Style.BRIGHT + Fore.RED + f'ПОРАЖЕНИЕ (-;\n')
		losses = losses + 1
		totalGames = totalGames + 1
	elif stepPlayer == 's' and stepComputer =='r':
		print(Style.BRIGHT + Fore.RED + f'ПОРАЖЕНИЕ (-;\n')
		losses = losses + 1
		totalGames = totalGames + 1