#salary schedule and annual increase python
# Computer Tutor Programming_12 April 2021

salary = float(input("Input The Starting Salary: £ "))
annual_Inc = (float(input("Input The Annual % Increase:"))/100)
years = int(input("Input The Number of Years: "))
print("Year\tSalary")
print("---------------")

for year in range(1,years + 1):
    salary = salary +salary*annual_Inc
    print(year,"\t",format(salary, ".2f"))

