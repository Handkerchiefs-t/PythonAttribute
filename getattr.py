class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, item):
        if item == 'acct':  # 请求acct，注意在__setattr__中，保存的内容为 _acct
            return self._acct[:-3] + '***'
        elif item == 'remain':
            return self.retireage - self.age
        else:  # 其它未定义的属性将会抛出异常
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.lower().replace(' ', '-')
        elif key == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif key == 'acct':  # 注意这里将key 改成了 _acct，否则__getattr__将无法捕捉acct
            key = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif key == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[key] = value  # 将属性保存，不要使用self.key = value 这种代码，会引起循环


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
