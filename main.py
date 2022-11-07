def A(func):
	def wrapper():
		func()
		print('A')
	return wrapper

def B(deco):
	def wrapper():
		deco()
		print('B')
	return wrapper


def A():
	print('welcome') #добро пожаловать



def B():
	print('calculator') #калькулятор

A()
B()




def ask_age():
    num1 = sign = num2 =''
    while num1 == '' or sign == '' or num2 == '':
      try:
        num1 = int(input('Input your number 1: '))	
        num2 = int(input('Input your number 2: '))
        sign = input('Input your sign:')
        if sign == '+' or sign == '-' or sign == '*' or sign == '/':
          print(num1,sign,num2)
        else:
          sign = ''
          raise ValueError
      except ValueError:
        print('You need to write normal evaluation')
    if sign == '+':
        print(num1,sign,num2,'=',num1+num2)
    elif sign == '/':
        print(num1,sign,num2,'=',num1/num2)
    if sign == '-':
      print(num1,sign,num2,'=',num1-num2)
    elif sign == '*':
          try:
            print(num1,sign,num2,'=',num1*num2)
          except:
              print('This is division by zero!!!')
          print('The end of program')
def ask_age2():
    age = ''
    while age =='':
      age = int(input('Input your age: '))
      print('Your age is', age)
    print('The end of program')
ask_age()


