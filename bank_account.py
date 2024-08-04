# CLASSE PARA CADASTRO DE USUARIOS DO BANCO NOMEADO COMO "PESSOA_FISICA" E A CLASSE
# COM DADOS DO BANCO DESSE USUARIO


class Pessoa_Fisica():
    def __init__(self,name,age,cpf,phone,email):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.phone = phone
        self.email = email
        
    def show_datas(self):
        print('-'*30,f'\nName: {self.name}\nAge: {self.age}\nCPF: {self.cpf}\nPhone: {self.phone}\nE-mail: {self.email}\n','-'*30,'\n')


class Bank_account(Pessoa_Fisica):
    def __init__(self, name, age, cpf, phone, email, digit, name_bank, balance):
        Pessoa_Fisica.__init__(self, name, age, cpf, phone, email)
        self.digit = digit
        self.name_bank = name_bank
        self.balance = balance

    def show_data_account(self):
        Pessoa_Fisica.show_datas(self)
        print(f'Hey Sr.{self.name}, your balance is {self.balance} in the bank {self.name_bank}\n')


datas_bank_account = Bank_account('Raphael Sampaio',20,1113335552,'+55 1199999-9999','raphael.tst@email.com','1555-6', 'Nubank', 54000) # Change the datas that you want
datas_bank_account.show_data_account()