class PayrollDeduction:

    def __init__(self, descrip, date, chargeAmount, empID):
        self.__descrip = descrip
        self.__date = date
        self.__chargeAmount = chargeAmount
        self.__empID = empID

    def get_descrip(self):
        return self.__descrip

    def get_date(self):
        return self.__date
    
    def get_chargeAmount(self):
        return self.__chargeAmount

    def get_empID(self):
        return self.__empID