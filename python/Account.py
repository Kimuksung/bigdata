class Account:
    name = ""
    balance = 0
    accountnumber = ""
    def __init__(self):
        pass

    def setAccount(self, a,b,c):
        self.name = a
        self.balance = b
        self.accountnumber = c

    def getAccount(self):
        return f"{self.name }: {self.balance}원, 계좌번호{self.accountnumber}"


tmp1 = Account()
tmp1.setAccount('김욱성',1000000,'123-456-789')
print(tmp1.getAccount())