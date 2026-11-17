class Company:
    class Employee:
        def __init__(self, employee_name: str, role: str):
            self.employee_name = employee_name
            self.role = role

        def show_info(self) -> str:
            return f"{self.employee_name} {self.role}"  # FIX 1: self.name → self.employee_name

    def __init__(self, company_name: str) -> None:
        self.company_name = company_name
        self.employees: list[Employee] = []

    def add_employee(self, name: str, role: str) -> None:
        new_employee: Company.Employee = self.Employee(name, role)
        self.employees.append(new_employee)

    def list_employee(self) -> list[str]:  # FIX 2: str → list[str]
        return [employee.show_info() for employee in self.employees]


def main() -> None:
    company1 = Company("Krusty Krab")

    company1.add_employee("Eugene", "Manager")
    company1.add_employee("Spongebob", "Cook")
    company1.add_employee("Squidward", "Cashier")

    for employee in company1.list_employee():
        print(employee)


if __name__ == "__main__":
    main()