class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.tax = 2.0
    
    def get_data(self):
        self.name = input("Enter employee name: ")
        self.salary = float(input("Enter monthly salary: "))
        self.tax = float(input("Enter tax percentage: "))

    def salary_after_tax(self):
        self.tax = 2.0
        return (100 - self.tax) / 100 * self.salary

    def update_tax_percentage(self, new_tax):
        self.tax = new_tax
        return (100 - self.tax) / 100 * self.salary


employee = Employee()
employee.get_data()

# Print salary after 2% tax
print(f"Salary after 2% tax: {employee.salary_after_tax()}")

# Update tax percentage
new_tax = float(input("Enter new percentage of tax: "))

# Print updated salary after tax
print(f"Salary after tax with updated percentage: {employee.update_tax_percentage(new_tax)}")
    