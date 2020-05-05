import discord
import random
from discord.ext import commands

client = commands.Bot( command_prefix='.')

@client.event
async def on_ready():
	print('connected')

'''

async def vr(ctx):
	await ctx.send('35')
'''
@client.command( pass_context = True)

@client.event

async def winrate(ctx, cg, wr, fwr):



	cg = int(cg)
	wr = float(wr)
	fwr = float(fwr)

	w = int(cg * wr / 100)
	l = cg - w
	i = 0

	while wr < fwr:
		w += 1
		cg += 1
		wr = round ( (100 * (w / cg)), 2)
		i += 1
	await ctx.send('Тебе ещё нужно выиграть {} игр'.format(i))

@client.command()

async def help_winrate(ctx):
	await ctx.send('Ты вызвал помощь по команде winrate: \n 1. Нужно ввести количество игр, которые ты сыграл \n 2. Нужно ввести текущий винрейт \n 3. Нужно ввести винрейт который ты хочешь \n Всё вводишь в таком формате .winrate <количество игр> <текущий винрейт> <винрейт, который хочешь>')



y = ['орёл', 'решка']
mokortu = 0
@client.command()


async def monetka(ctx, c):
	monetka = random.randint(0,1)
	c = c.lower()
	#await ctx.send(c)

	if c == 'орёл'or c == 'орел' or c== 'решка':
		#await ctx.send('После команды введи либо орёл, либо решка! Ничего другого!')
		mokortu = 1

	if c == 'орёл'or c == 'орел':
		orrekof= 1
	elif c== 'решка':
		orrekof = 0
	else:
		await ctx.send('После команды введи либо орёл, либо решка! Ничего другого!')

		#orel = 1
		#reshla = 0

	if monetka == 1 and mokortu == 1 and orrekof == 1:
		await ctx.send('Выпал ОРЁЛ. Победа!')
	if monetka == 1 and mokortu == 1 and orrekof == 0:
		await ctx.send('Выпал ОРЁЛ. Поражение...')
	if monetka == 0 and mokortu == 1 and orrekof ==0:
		await ctx.send('Выпала РЕШКА. Победа!')
	if monetka == 0 and mokortu == 1 and orrekof ==1:
		await ctx.send('Выпала РЕШКА. Поражение...')


#HERO = open('HERO.txt').readline()
HERO = ['Мия', 'Бальмонд', 'Сабер', 'Нана', 'Тигрил', 'Алукард', 'Акай', 'Бэйн', 'Бруно', 'Клинт', 'Рафаель', 'Эйдора', 'Зилонг', 'Фанни', 'Лейла', 'Лолита', 'Хаябуса', 'Фрея', 'Горд', 'Наталья', 'Ли-Сун Син', 'Москов', 'Кэрри', 'Грок', 'Одетта', 'Фаша', 'Ханаби', 'Селена', 'Клауд', 'Люнокс', 'Кимми', 'Харит', 'Фарамис', 'Хуфра', 'Грейнджер', 
		'Эсмеральда', 'Теризла', 'Маша', 'Ван-Ван', 'Сильвана', 'Пополь и Купа', 'Алиса', 'Хилос', 'Ангела', 'Госсен', 'Валир', 'Карина', 'Минотавр', 'Кагура', 'Чу', 'Сан', 'Альфа', 'Руби', 'Джонсон', 'Циклоп', 'Эстес', 'Хильда', 'Аврора', 'Лапу-Лапу', 'Вексана', 'Роджер', 'Гатоткача', 'Харли', 'Иритель', 'Аргус', 'Дигги', 'Заск', 'Хелкарт', 'Лесли', 'Кусака', 'Мартис',
		'Уранус', 'Чан Э', 'Кая', 'Алдос', 'Вейл', 'Леоморд', 'Ханзо', 'Белерик', 'Тамуз', 'Минситар', 'Кадита', 'Баданг', 'Гвиневра', 'Икс. Борг', 'Линг', 'Дариус', 'Лилия', 'Баксий', 'Сисилион', 'Кармилла', 'Атлас']
maybe = [',возможно', ',должно быть', ',скорее всего', ',как будто', ',что ли', ',если хотите ', ',по возможности', ',судя по всему ', ',если хочешь', ',как видно', ',вроде бы', ',как мне кажется', ',по всей видимости', ',наверное', ',по всей вероятности', ',но я могу ошибаться', ',пожалуй', ',очевидно', ',вероятно', ',надо полагать', ',по-видимому', ',реально', ',как мне видится', ',по ходу', ',наверняка']

@client.command()

async def question(ctx):

	rfoq = random.randint(0,len(HERO)-1)
	rfoq2 = random.randint(0,len(maybe)-1)
	await ctx.send(HERO[rfoq]+  maybe[rfoq2])


filerespects = 'respects.txt'


@client.command()

async def f(ctx):
	countrespects = int(open(filerespects).readline())
	laxzkaknazvat = open(filerespects, 'w')
	await ctx.send('Спасибо! Стараюсь!')
	print(countrespects)
	laxzkaknazvat.write(str(countrespects+1))
	await ctx.send(f'На данный момент респектов получено {countrespects+1} :partying_face:' )





#fail code
'''	if c=='орёл' or c=='решка':
		if y[monetka] == c and c=='орёл':
			await ctx.send('Выпал ОРЁЛ! Да... Тебя удача не обделила')
		elif y[monetka]== c and c=='решка':
			await ctx.send('Выпала РЕШКА! Да... Удача не обошла тебя стороной')
		elif y[monetka]!= c and c=='решка':
			await ctx.send('Выпала РЕШКА. Обязательно повезет в следущий раз')
		elif y[monetka]!=c and c=='орёл':
			await ctx.send('Выпал ОРЁЛ! Повезёт в следущий раз')'''


token = open('token.txt').readline()
client.run(token)

