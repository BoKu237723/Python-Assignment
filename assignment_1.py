import sys
class MiniBank:

    main_userInfo:dict = {}

    def firstOption(self):
        while True:
            try:
                print("Press 1 to log in \nPress 2 to register\nPress 3 to exit")
                option =int(input("Enter :")) #
                if(option==1):
                    self.login()
                elif(option == 2):
                    self.register()
                elif(option == 3):
                    sys.exit()
                else:
                    print("Invalid input\n")
            except ValueError:   ####
                print("Invalid input\n")

    def returnID(self, transferUsername):
        for user_id, user_data in self.main_userInfo.items():
            if user_data['r_username'] == transferUsername:
                return user_id
        return None

    def menu(self, loginID):
        while True:
            try:
                menu_input = int(input("\nPress 1 to transfer \nPress 2 to withdraw \nPress 3 to update user data \nPress 4 to check profile\nPress 5 to exit \nYour input: "))
                if menu_input == 1:
                    return self.tra(loginID)
                elif menu_input == 2:
                    return self.wid(loginID)
                elif menu_input == 3:
                    return self.upd(loginID)
                elif menu_input == 4:
                    return self.profile(loginID)
                elif menu_input == 5:
                    print("Exiting... Thank you!\n")
                    break
                else:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input.")

    def profile(self, loginID):
        user_data = self.main_userInfo[loginID]
        print("\n--- User Profile ---")
        print(f"Username: {user_data['r_username']}")
        print(f"Password: {user_data['r_passcode']}")
        print(f"Amount: {user_data['Amount']}")
        print("---------------------")
        self.menu(loginID) 
        
    def tra(self, loginID):
        transferUsername = input("Enter user name to transfer : ")
        transfer_id = self.returnID(transferUsername)    
        if transfer_id in self.main_userInfo:
            if transfer_id == loginID:
                print("You cannot transfer money to yourself.")
                return self.tra(loginID)
            print('We get to transfer id : ', transfer_id)
            print('My id ', loginID)
    
            amount = int(input("Enter amount to transfer : "))
            if amount > self.main_userInfo[loginID]["Amount"]:
                print("Not enough money.")
                print('Your Amount is : ', self.main_userInfo[loginID]["Amount"])
                return self.tra(loginID)
            elif amount <= 0:
                print("Invalid input.")
                return self.tra(loginID)
            else:
                print("Successfully transferred.")
                self.main_userInfo[loginID]["Amount"] -= amount
                self.main_userInfo[transfer_id]["Amount"] += amount
                print("Your amount in your bank is now ", self.main_userInfo[loginID]["Amount"])
                return self.menu(loginID)
        else:
            print("User name not found.")
            return self.menu(loginID)

    def wid(self,loginID):
        widMoney=int(input("Enter the amount to withdraw : "))
        if widMoney > self.main_userInfo[loginID]["Amount"]:
            print("Not enough money, Your current amount is ",self.main_userInfo[loginID]["Amount"])
            return self.menu(loginID)
        elif widMoney <= 0:
            print("Invalid input")
            return self.wid(loginID)
        else:
            self.main_userInfo[loginID]["Amount"] -= widMoney
            print("Success in withdraw")
            print("Your current amount is ",self.main_userInfo[loginID]["Amount"])
            return self.menu(loginID)

    def upd(self, loginID):
        while True:  # Loop 
            print("\n--------------Update--------------\n")
            print("Press 1 to update Username")
            print("Press 2 to update Password")
            print("Press 3 to update Amount")
            print("Press 4 to return Menu")
            print("Press others to go to menu")
        
            try:
                updInput = int(input("Enter: "))
                if updInput == 1:
                    new_name = input("\nEnter your new name: ")
                    if any(user_data["r_username"] == new_name for user_data in self.main_userInfo.values()):
                        print("Username already exists")
                    else:
                        self.main_userInfo[loginID]["r_username"] = new_name
                        print(f"Username changed successfully to ({new_name})")
                        return self.upd(loginID)
                elif updInput == 2:
                    new_pass = input("Enter your new password: ")
                    if any(user_data["r_passcode"] == new_pass for user_data in self.main_userInfo.values()):
                        print("Password already exists")
                    else:
                        self.main_userInfo[loginID]["r_passcode"] = new_pass
                        print("Password changed successfully")
                        return self.upd(loginID)
                elif updInput == 3:
                    try:
                        new_input = int(input("Enter the amount to add: "))
                        if new_input <= 0:
                            print("Invalid input")
                        else:
                            self.main_userInfo[loginID]["Amount"] += new_input
                            print("Added successfully")
                            print(f"This is your current amount: {self.main_userInfo[loginID]['Amount']}")
                            return self.menu(loginID)
                    except ValueError:
                        print("Invalid input")
                        return self.upd(loginID)
                elif updInput == 4:
                    return self.menu(loginID)
                else:
                    break #exit
            except ValueError:
                print("Invalid input.")


    def login(self):
        print("\n_________This is from Login_________\n")
        l_username : str = input("Enter User Name to login : ")
        l_userpasscode : int = input("Enter Passcode to login : ")
        (exitUser)= self.exitUsername(l_username,l_userpasscode)
        if((exitUser)):
            print("_________Login Successful_________")
            loginID : int = self.returnID(l_username)
            self.menu(loginID)
        else:
            print("You can't login")

    def exitUsername(self, l_username, l_passcode):
        for user_id, user_data in self.main_userInfo.items():
            if user_data["r_username"] == l_username and user_data["r_passcode"] == l_passcode:
                return True
        return False

    def register(self):
        print("\n_________This is from register_________\n")
        r_username: str = input("Enter User Name to register: ")
        for user_data in self.main_userInfo.values():
            if user_data["r_username"] == r_username:
                print("Username already exists.")
                return self.register() 
        r_passcode_1: int = input("Enter Passcode to register: ")
        if any(data["r_passcode"] == r_passcode_1 for data in self.main_userInfo.values()):
            print("Password already exists. ")
            return self.register() 
        else:
            r_passcode_2: int = input("Enter passcode again: ")
        if r_passcode_1 == r_passcode_2:
            if r_passcode_1 == r_passcode_2:
                r_amount = None
                while r_amount is None:
                    try:
                        r_amount = int(input('Enter amount: '))
                        if r_amount <= 0:
                            print("Invalid input")
                            r_amount = None  #looping
                    except ValueError:
                        print("Invalid input.")
            id: int = self.checkingUserCount()
            userInfoForm: dict = {id: {"r_username": r_username, "r_passcode": r_passcode_2, "Amount": r_amount}}
            self.main_userInfo.update(userInfoForm)
            print("#### Success! Registered! ####\n\n")
            print(self.main_userInfo)  
        else:  
            print("Passcodes do not match. Please try again.")
            return self.register()
    
    def checkingUserCount(self):
        count = len(self.main_userInfo)
        return count+1

if __name__ == "__main__":
    miniBank : MiniBank= MiniBank()
    while True:
        miniBank.firstOption()
