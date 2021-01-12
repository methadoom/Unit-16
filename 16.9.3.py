class Client:
    def __init__(self, firstname, lastname, balance):
        self.firstnam = firstname
        self.lastname = lastname
        self.balance = balance

    def printInformation(self):
        print('Клиент "{} {}", Баланс: {} руб.'.format(self.firstnam, self.lastname, self.balance))

client_1 = Client ("Иван", "Петров", "50")
client_1.printInformation()