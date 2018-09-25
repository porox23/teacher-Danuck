import sys

def mult_2(m):  # multiplication on 2
    rezult = m * 2
    return rezult


def mult_3(m):
    rezult = mult_2(m) * 3
    return rezult


def mult_4(m):
    rezult = mult_3(m) * 4
    return rezult

def fact_recurs(m):
        if m == 0:
            return 1
        elif m > 0:
            return fact_recurs(m-1)*m
        else:
            print(' Не шали, давай число больше нуля')
            return 0

def fact_generator(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res

class mult():
    def __init__(self, name):
        self.name = name
        self.mult_on3 = 0
        self.mult_on4 = 0
        self.fact_rec = 0
        self.gen = 0


    def mult_o3(self, m):
        self.mult_on3 = mult_3(m)

    def mult_o4(self, m):
        self.mult_on4 = mult_4(m)

    def fact_recurs(self, m):
        self.fact_rec = fact_recurs(m)


    def show_mult(self):
        discrip = (self.name + '\n Do you want to know what Look: ' + str(self.mult_on4) +
                   ' \n if only by 3... Look:  ' + str(self.mult_on3) + '\n Факториал получлся: ' + str(self.fact_rec))
        print(discrip)



# _____________________________________________ begin modul ___________________________________________________________
k = 0
x = len(sys.argv)
if x > 3:
    print("Сергій, одного ім'я та цифри достатньо решта зайве ")
    name_sys = str(sys.argv[1])
    numeral = float(sys.argv[2])
    print(x, str(sys.argv) )
elif x == 3:
    name_sys = str(sys.argv[1])
    numeral = float(sys.argv[2])
else:
    print('Серый ты должен ввести: \n 1:Имя!!!!!!!  2:цыфру !!!!!!!!!! \n ...в командной строке после .py ! \n ')
    name_sys = 'Sergei'
    numeral = 4

mu = mult(name_sys)
mu.mult_o3(numeral)
mu.mult_o4(numeral)
mu.fact_recurs(numeral)

mu.show_mult()
print('___________________________________________ \n')

yie = fact_generator(numeral)
print( 'Крок 1-ий по итерації :', next(yie))
print( 'Крок 2-ий по итерації :', next(yie))
print( 'Крок 3-ий по итерації :', next(yie))