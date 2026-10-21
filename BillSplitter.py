from abc import ABC,abstractmethod

class BillSplitter:

    bill_item: list = []

    print("====================================")
    print("   Welcome to Bill Splitter!") 
    print("====================================")

    running: bool = True

    while running:
        print("\n--- Main Menu ---")
        print("1. Add Item")
        print("2. Calculate Bill")
        print("3. View Current Items")
        print("4. Exit")

        choice: str = input("Choose an option: ")

        match choice:
            case "1":
                name: str = input("Enter item name: ")
                if not name:
                    print("Item name can not be empty")
                    break

                price: float = -1
                while price < 0:
                    print("Enter price: $")
                    try:
                        price = float(input())
                        if price < 0:
                            print("Price can not be negative")
                    except Exception:
                        print("Please enter a valid number")
                print("Item type: ")
                print(" 1. Shared Item")
                print(" 2. Individual Item")

                type_choice: str = input("Choose type (1/2): ")
                type_name:str = ""

                if type_choice == "1":
                    type_name = "Shared Item"
                else:
                    type_name = "Individual Item"



class Taxable:

    @abstractmethod
    def apply_tax(subtotal: float) -> float:
        pass



class Tax_Calculator(Taxable):

    def apply_tax(subtotal: float) -> float:
        return subtotal + (subtotal * 0.05)



class BillItem:

    def __init__(self,name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self, price):
        return price

    @abstractmethod
    def calculate_cost_per_person(total_person: int) -> float:
        pass



class SharedAppetizer(BillItem):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_cost_per_person(total_person: int) -> float:
        return super().get_price / total_person



class IndividualItem(BillItem):

    def __init__(self, name: str, price: float):
        super().name
    