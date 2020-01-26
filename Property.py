class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '-')
        self.__name = value

    name = property(getName, setName)  # 对name属性：转化为__name,将字符转为小写，并且将空格转换成'-'

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value

    age = property(getAge, setAge)  # 对age：判断是否处于0-150之间

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)  # 对acct：将'-'去除，规定acct长度为8，输出时将后三位转为 ***

    def remainGet(self):
        return self.retireage - self.age

    remain = property(remainGet)


if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')

    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')

    try:
        sue.age = 200
    except:
        print('Bad age for Sue')
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')
