class BankAccount:
    def __init__(self, balance):
        self.__balance= balance#Приватная переменная
    def deposit(self,amount):#Эта функция добавляет деньги на карту
        if amount > 0:
            self.__balance+=amount
    def withdraw(self,amount):#Эта функция добавляет списания с карты
        if 0 < amount <= self.__balance:
            self.__balance-=amount
        else:
            print('Недостаточно средств')#Если на карте меньше средств,чем нужно списать,то код печатает эту надпись

    def get_balance(self):#пишем баланс карты
        return self.__balance
account = BankAccount(1000)#Баланс карты
account.deposit(500)#прибыль
account.withdraw(100)#списание
print(account.get_balance())#пишется эта строка,потому что при обычном принте приватной перменной возникла бы ошибка
#в этом коде нужна приватная переменная,чтобы пользователь что-то случайно не испортил