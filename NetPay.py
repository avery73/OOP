def main():
    
    from prettytable import PrettyTable
    import EmployeeClass as EC
    import PayrollDeductionClass as PDC

    person = EC.Employee("Jimmy Smith", "58475", "Information Systems", "Developer", 6800.00)

    myTable = PrettyTable()
    myTable.field_names = ["Name", "ID Number", "Department", "Job Title", "Monthly Salary"]

    myTable.add_row([person.get_name(), person.get_IDNum(), person.get_dept(), person.get_jobTitle(), person.get_monthSalary()])

    print(myTable)

    transaction1 = PDC.PayrollDeduction("Food Court", "8/14/2022", 22.50, "39119")
    transaction2 = PDC.PayrollDeduction("Gift Constribution", "8/12/2022", 25.00, "58475")
    transaction3 = PDC.PayrollDeduction("Food Court", "8/17/2022", 15.25, "21547")
    transaction4 = PDC.PayrollDeduction("Vending Machine", "8/22/2022", 3.00, "58475")
    transaction5 = PDC.PayrollDeduction("Vending Machine", "8/5/2022", 2.75, "58475")

    myTable = PrettyTable()
    myTable.field_names = ["Description", "Date", "Charge", "EmployeeID"]

    myTable.add_row([transaction1.get_descrip(), transaction1.get_date(), transaction1.get_chargeAmount(), transaction1.get_empID()])
    myTable.add_row([transaction2.get_descrip(), transaction2.get_date(), transaction2.get_chargeAmount(), transaction2.get_empID()])
    myTable.add_row([transaction3.get_descrip(), transaction3.get_date(), transaction3.get_chargeAmount(), transaction3.get_empID()])
    myTable.add_row([transaction4.get_descrip(), transaction4.get_date(), transaction4.get_chargeAmount(), transaction4.get_empID()])
    myTable.add_row([transaction5.get_descrip(), transaction5.get_date(), transaction5.get_chargeAmount(), transaction5.get_empID()])

    print(myTable)

    if person.get_IDNum() == transaction2.get_empID() == transaction4.get_empID() == transaction5.get_empID():
      math = person.get_monthSalary() - transaction2.get_chargeAmount() - transaction4.get_chargeAmount() - transaction5.get_chargeAmount()

    print("*** Employee Pay ***")
    print("Name:", person.get_name())
    print("ID Number:", person.get_IDNum())
    print("Department:", person.get_dept())
    print("Gross Pay: $" + str(person.get_monthSalary()))
    print("Net Pay: $" + str(math))
    
main()