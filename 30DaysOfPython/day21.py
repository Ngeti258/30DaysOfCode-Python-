import statistics
class Statistics:
    def __init__(self,data) :
        self.data=data
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def min(self):
        smallest=sorted(self.data)
        return smallest[0]
    def max(self):
        largest=sorted(self.data)
        return largest[-1]
    def range(self):
        return self.max()-self.min()
    def mean(self):
        return statistics.mean(self.data)
    def median(self):
        return statistics.median(self.data)
    def mode(self):
        return statistics.mode(self.data)
    def std(self):
        return statistics.stdev(self.data)
    def var(self):
        return statistics.variance(self.data)
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

test=Statistics(ages)
print('Count: ',test.count())
print('Sum: ', test.sum()) 
print('Min: ', test.min()) 
print('Max: ', test.max()) 
print('Range: ', test.range()) 
print('Mean: ', test.mean()) 
print('Median: ', test.median())
print('Mode: ', test.mode())
print('Standard Deviation: ', test.std()) 
print('Variance: ', test.var())


class PersonAccount:
    def __init__(self,first_name,last_name,incomes,expenses,properties):
        self.first_name=first_name
        self.last_name=last_name
        self.incomes=incomes
        self.expenses=expenses
        self.properties=properties
    def total_income(self):
        return sum(self.incomes)
    def total_expenses(self):
        return sum(self.expenses)
    def account_info(self):
        return f'''Name:{self.first_name} {self.last_name}
        Total income:{self.total_income()}
        Total expenses:{self.total_expenses()}
        '''
    def add_income(self,extra_income):
        self.extra_income=extra_income
        return self.total_income()+self.extra_income

    def add_expense(self,extra_expenses):
        self.extra_expenses=extra_expenses
        return self.total_expenses()+self.extra_expenses
    
    def account_balance(self):
        return self.total_income()-self.total_expenses()

one=PersonAccount('Gabriel','Ngeti',[520000,70000,80000,],[35000,10000,5000,5000],2000000)
print(one.account_balance())
