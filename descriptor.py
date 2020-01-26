class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return self.name  # 使用描述符的存储空间，而不是CardHolder的

        def __set__(self, instance, value):  # 在这里你可以使用instance，但是要注意将属性名改成_name，否则会循环
            value = value.lower().replace(' ', '-')
            self.name = value

    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value

    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:  # 在这里使用了instance的属性
                raise TypeError('invald acct number')
            else:
                self.acct = value

    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age  # 使用instance.age会触发Age.__get__

        def __set__(self, instance, value):
            raise TypeError('cannot set remain')

    remain = Remain()


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
