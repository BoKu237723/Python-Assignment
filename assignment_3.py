import pymongo
import sys
from datetime import datetime


try:
    connection = pymongo.MongoClient("localhost", 27017)
    dataBase = connection["myDB"]
    collection = dataBase["Assignment3"]
    print("\n________Connection Successful________\n")
except Exception as error:
    print("Connection Error:", error)
    exit()

class Expense:
    def userInput(self):
        userID = self.next_id()
        expenseName = input("\nEnter Expense name : ")
        
        while True:
            try:
                cost = int(input("Enter the cost : "))
                if cost < 1:
                    print("Cost must be a positive number")
                    continue
                break
            except ValueError:
                print("Invalid input, please enter a valid number")

        date = input("Enter the date (dd/mm/yy) : ")
        if not self.checking_tdate(date):
            print("Invalid date format or date in the future")
            return

        data = {
            "_id": userID,
            "Expense_Name": expenseName,
            "cost": cost,
            "Date": date
        }
        try:
            collection.insert_one(data)
            print("Data inserted successfully")
            print("The Expense Name is ", expenseName)
            print("The cost is ", cost)
            print("Date is ", date)
        except Exception as error:
            print("Insert Error:", error)

    def checking_tdate(self, date):
        try:
            date_obj = datetime.strptime(date, '%d/%m/%Y')
            if date_obj > datetime.now():
                print("Date cannot be in the future")
                return False
            return True
        except ValueError:
            print("Date format should be dd/mm/yyyy (e.g., 03/09/2024)")
            return False

    def next_id(self):
        maxID = collection.find_one(sort=[("_id", -1)])
        return 1 if maxID is None else maxID["_id"] + 1

class ExpenseTracker: ##############
    def menu(self):
        while True:
            try:
                menuInput = int(input("\nPress 1 to delete the info\nPress 2 to view info\nPress 3 to view total expenses\nPress 4 to exit \nUser input : "))
                if menuInput == 1:
                    self.deleteInfo()
                elif menuInput == 2:
                    self.viewInfos()
                elif menuInput == 3:
                    self.viewTotal()
                elif menuInput == 4:
                    return 
                else:
                    print("Invalid input, Try again")
            except ValueError:
                print("Enter valid number")

    def deleteInfo(self):
        print("\n")
        while True:
            data = collection.find()
            for d in data:
                print(d)
            userInput = input("Enter the ID you want to delete or press 'e' to exit: ")
            if userInput == 'e':
                print("__________Exiting__________")
                return
            try:
                theID = int(userInput)
                result = collection.delete_one({"_id": theID})
                if result.deleted_count > 0:
                    print("Deletion successful")
                    print("\n")
                else:
                    print("ID not found")
            except ValueError:
                print("Invalid ID format")
            except Exception as err:
                print("Delete Error:", err)

    def viewInfos(self):
        data = collection.find()
        print("\n")
        for d in data:
            
            print(d)

    def viewTotal(self):
        try:
            tCost = sum(expense.get('cost', 0) for expense in collection.find())
            print('Total cost is ', tCost)
        except Exception as err:
            print("Error calculating total:", err)

def controller():
    while True:
        
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d")
        print(formatted_now)
        try:
            choice = int(input("Press 1 to add\nPress 2 to access other functions\nPress 3 to exit\nUser Input : "))
            if choice == 1:
                Expense().userInput()
            elif choice == 2:
                ExpenseTracker().menu()
            elif choice == 3:
                sys.exit() #exit
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    controller()
