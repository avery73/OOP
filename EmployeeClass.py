class Employee:

    def __init__(self, name, IDNum, dept, jobTitle, monthSalary):
        self.__name = name
        self.__IDNum = IDNum
        self.__dept = dept
        self.__jobTitle = jobTitle
        self.__monthSalary = monthSalary 

    def get_name(self):
        return self.__name

    def get_IDNum(self):
        return self.__IDNum

    def get_dept(self):
        return self.__dept

    def get_jobTitle(self):
        return self.__jobTitle

    def get_monthSalary(self):
        return self.__monthSalary