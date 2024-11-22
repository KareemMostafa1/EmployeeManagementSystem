import pandas as pd
import re
class Employee:
    __company_name="AMIT"
    def __init__(self , ID , Name , Age , Position , Salary , Email ):
        self.__ID=ID
        self.__Name=Name
        self.__Position=Position
        self.__Email=Email
        self.__Age=Age
        self.__Salary=Salary
    
############# Setters and Getters for Employee data ############################

    @property
    def _ID(self):
        return self.__ID

    @_ID.setter
    def _ID(self, value):
        self.__ID = value

    @property
    def _Name(self):
        return self.__Name

    @_Name.setter
    def _Name(self, value):
        self.__Name = value

    @property
    def _Position(self):
        return self.__Position

    @_Position.setter
    def _Position(self, value):
        self.__Position = value

    @property
    def _Email(self):
        return self.__Email

    @_Email.setter
    def _Email(self, value):
        self.__Email = value

    @property
    def _Age(self):
        return self.__Age

    @_Age.setter
    def _Age(self, value):
        self.__Age = value

    @property
    def _Salary(self):
        return self.__Salary

    @_Salary.setter
    def _Salary(self, value):
        self.__Salary = value
    
#employee=Employee("kareem",22,"man",111,"sss","kkkk")    
#####################################################################################################

class EmployeeManager:
    def __init__(self):
        self.Employees={}  # Dictionary to save the data of each employee in it to be able to communiicate with the csv file 
        self.first_employee=0
        self.ID_list=[]
    def Add_new_Employee(self):
        print("\nPlease enter the Data of the new Employee .... \n")

        input_name=input("Employee name is : ")
        if bool(re.fullmatch(r"[A-Za-z\s]+", input_name)): 
            valid_name=input_name
        else:
            print("please enter a valid name")
            while(not input_name.isalpha()):
                input_name=input("Employee name is : ")   #keep asking untill input is valid
            valid_name=input_name

        input_age=input("Employee age is : ")
        if input_age.isdigit():
            valid_age=input_age
        else:
            print("please enter a valid age")
            while(not input_age.isdigit()):
                input_age=input("Employee age is : ")   #keep asking untill input is valid
            valid_age=int(input_age)

        input_ID=input("Employee ID is :")
        while input_ID in self.ID_list:     # make sure that all ids are unique
            input_ID=input("this id is already taken please enter a different one :")
        valid_ID=input_ID
        self.ID_list.append(valid_ID) #add the new id to the list of ids

        
        input_position=input("Employee position is : ")
        if input_position.isalpha():
            valid_position=input_position
        else:
            print("please enter a valid position")
            while(not input_position.isalpha()):
                input_position=input("Employee position is : ")   #keep asking untill input is valid
            valid_position=input_position


        input_salary=input("Employee salary in dollars is : ")
        if input_salary.isdigit():
            valid_salary=int(input_salary)
        else:
            print("please enter a valid salary")
            while(not input_salary.isdigit()):
                input_salary=input("Employee salary is : ")   #keep asking untill input is valid
            valid_salary=input_salary

        input_email=input("Employee GMail  is : ")
        if "@gmail.com" in  input_email:
            valid_email=input_email
        else:
            while(not "@gmail.com"  in  input_email):
                input_email=input("Employee Gmail is : ")   #keep asking untill input is valid
            valid_email=input_email

        new_employee=Employee(valid_name,valid_ID,valid_age,valid_position,valid_salary,valid_email)    #create the employee object using the input data
        
        self.Employees[valid_ID]=[valid_name,new_employee._Age,new_employee._Position,new_employee._Salary,new_employee._Email]  #add the new employee's data to the dictionary
        
        df=pd.DataFrame.from_dict(self.Employees,orient="index",columns=["Name", "Age", "Position", "Salary", "Email"])   #convert the data dictionary into a pandas data frame to save it into the csv file
        df.to_csv("C:\python\Employeedata.csv",mode="a")   # append the new added emplyee to the csv file
        

    def delete_employee(self):
        id_to_delete=input("Enter the id of employee to delete :")
        if(id_to_delete in self.ID_list):
            del self.Employees[id_to_delete]
            df=pd.DataFrame.from_dict(self.Employees,orient="index",columns=["Name", "Age", "Position", "Salary", "Email"])   #convert the data dictionary into a pandas data frame to save it into the csv file
            df.to_csv("C:\python\Employeedata.csv",mode="w")  #update the csv file agter deletion
        else:
            print("this ID does not exist")
        ##print(pd.DataFrame(self.Employees).transpose())
    def edit_employee_data(self):
        id_to_edit=input("Enter the id of employee to edit :")
        if(len(self.ID_list)==0):
            print("There is no Employees added yet")
            return
        if(id_to_edit in self.ID_list):
            field_to_edit=input("please select which data field that you want to edit \n1) Name\n2) Age\n3) Position\n4) Salary\n5) Email\n")
            if int(field_to_edit)>0 and int( field_to_edit)<6:
                new_value=input("please enter the new value")
                if(int(field_to_edit)==2 or int(field_to_edit)==4):
                    self.Employees[id_to_edit][int(field_to_edit)-1]=int(new_value)
                else:
                    self.Employees[id_to_edit][int(field_to_edit)-1]=new_value
                df=pd.DataFrame.from_dict(self.Employees,orient="index",columns=["Name", "Age", "Position", "Salary", "Email"])   #convert the data dictionary into a pandas data frame to save it into the csv file
                df.to_csv("C:\python\Employeedata.csv",mode="w") #apply edited information to the csv file
            else:
                print("inalid input") 
        else:
            print("The user you are trying to access do not exist")
    def view_all_employees(self):
        if(len(self.ID_list)==0):
            print("There is no Employees added")
        else:
            df=pd.DataFrame.from_dict(self.Employees,orient="index",columns=["Name", "Age", "Position", "Salary", "Email"])
            print(df)
            
            

    
    
Employee_Manager1=EmployeeManager()
Exit = 0
while not Exit:  # Creating the user menu interface
    print("\t Welcome to our Employee Management System\n")
    user_choice = input(
        "-> Please choose what you want to do from the following:\n"
        "1)Add New Employee.\n"
        "2)Delete an Employee by ID.\n"
        "3)Edit an Employee's Data.\n"
        "4)Show All Employees.\n"
        "5)Exit\n").strip()
    if user_choice == '1':
        Employee_Manager1.Add_new_Employee()
    elif user_choice == '2':
        Employee_Manager1.delete_employee()
    elif user_choice == '3':
        Employee_Manager1.edit_employee_data()
    elif user_choice == '4':
        Employee_Manager1.view_all_employees()
    elif user_choice == '5':
        Exit = 1
        print("Exiting....................Thank you ENg.Baraa<3")
    else:
        print("Invalid option. Please choose a number between 1 and 5.")

        

