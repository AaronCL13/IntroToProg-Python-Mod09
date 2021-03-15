# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ALanphear,3.13.21,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

from DataClasses import Employee as Emp
from IOClasses import EmployeeIO as Eio
from ProcessingClasses import FileProcessor as Fp

# Main Body of Script  ---------------------------------------------------- #


def main():
    file_name = "EmployeeData.txt"
    list_table = []
    choice = None
    # Load data from file into a list of employee objects when script starts
    file_data = Fp.read_data_from_file(file_name)
    for line in file_data:
        list_table.append(Emp(line[0], line[1], line[2].strip()))
    while choice != "4":
        # Show user a menu of options
        Eio.print_menu_items()
        # Get user's menu option choice
        choice = Eio.input_menu_options()
        # Show user current data in the list of employee objects
        if choice == "1" and list_table == []:
            print("...There is no current list to display...")
            print("...You must first add an employee to your list...")
        elif choice == "1":
            Eio.print_current_list_items(list_table)
        # Let user add data to the list of employee objects
        elif choice == "2":
            emp = Eio.input_employee_data()
            emp_id = emp.employee_id
            emp_fn = emp.first_name
            emp_ln = emp.last_name
            if emp_id == "" or emp_fn == "" or emp_ln == "":
                print("One of your values is blank. Please try again.")
            elif emp_id.isalpha() and (emp_fn.isnumeric() or emp_ln.isnumeric()):
                print("Please check your data!\n"
                      "ID must be a number.\n"
                      "Names must NOT be a number.")
            elif emp_id.isalpha():
                print("Employee ID must be a number! Please try again.")
            elif emp_fn.isnumeric() or emp_ln.isnumeric():
                print("A name must not be a number! Please try again.")
            else:
                list_table.append(emp)
                print("Employee added to your list!")
        # let user save current data to file
        elif choice == "3":
            Fp.save_data_to_file(file_name, list_table)
            print("List saved to file!\n")
        # Let user exit program
        elif choice == "4":
            print("Goodbye!")
        else:
            print("'" + choice + "'", "is not an available option. Please try again!")

# Main Body of Script  ---------------------------------------------------- #

# Run Program ------------------------------------------------------------- #


main()
input("\nPress [Enter] to exit.")


