"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType):
        self.name = name
        self.contractType = contractType
        self.monthlySal = 0
        self.hoursWorked = 0
        self.hourlyWage = 0
        self.commissionType = ""
        self.fixedCommission = 0
        self.numOfContracts = 0
        self.commissionPerCon = 0

    def get_pay(self):
        if self.contractType == "monthly salary":
            pay = self.monthlySal + self.fixedCommission + (self.numOfContracts)*(self.commissionPerCon)
            return(pay)
        elif self.contractType == "hourly":
            pay = self.hoursWorked*self.hourlyWage + self.fixedCommission + (self.numOfContracts)*(self.commissionPerCon)
            return(pay)

    def get_contract_info(self):
        if self.contractType == "monthly salary":
            message = (f" works on a monthly salary of {self.monthlySal}")
            return(message)
        elif self.contractType == "hourly":
            message = (f" works on a contract of {self.hoursWorked} hours at {self.hourlyWage}/hour")
            return(message)
        else:
            return(" has no contract")

    def get_commission_info(self):
        if self.commissionType == "contract":
            message = (f" and recives a commission for {self.numOfContracts} contract(s) at {self.commissionPerCon}/contract")
            return(message)
        elif self.commissionType == "fixed":
            message = (f" and recives a bonus commission of {self.fixedCommission}")
            return(message)
        else:
            return("")

    def __str__(self):
        return(f"{self.name}{self.get_contract_info()}{self.get_commission_info()}. Their total pay is {self.get_pay()}.")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly salary")
billie.monthlySal = 4000
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly")
charlie.hoursWorked = 100
charlie.hourlyWage = 25
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly salary")
renee.monthlySal = 3000
renee.commissionType = "contract"
renee.numOfContracts = 4
renee.commissionPerCon = 200
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly")
jan.hoursWorked = 150
jan.hourlyWage = 25
jan.commissionType = "contract"
jan.numOfContracts = 3
jan.commissionPerCon = 220
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly salary")
robbie.monthlySal = 2000
robbie.commissionType = "fixed"
robbie.fixedCommission = 1500
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly")
ariel.hoursWorked = 120
ariel.hourlyWage = 30
ariel.commissionType = "fixed"
ariel.fixedCommission = 600
print(str(ariel))
