def write_biodata_to_file(file, name, cnic, age, salary):
    try:
        # write the biodata in the txt file
        with open(file, 'w') as f:
            f.write(f"Name: {name}\n")
            f.write(f"CNIC Number: {cnic}\n")
            f.write(f"Age: {age}\n")
            f.write(f"Salary: {salary}\n")
        print(f"Biodata has been written to '{file}'.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while writing biodata: {e}")

def append_contact_number_to_file(file, contact_number):
    try:
        # add the contact number to the biodata
        with open(file, 'a') as f:
            f.write(f"Contact Number: {contact_number}\n")
        print(f"Contact number has been appended to '{file}'.")
    except PermissionError:
        print("Error: You do not have permission to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending contact number: {e}")

def read_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

file = "employee_biodata.txt"

try:
    name = input("Enter Name: ")
    cnic = input("Enter CNIC Number: ")
    age = input("Enter Age: ")
    salary = input("Enter Salary: ")
        
    if not age.isdigit():
        raise ValueError("Age must be a number.")
    if not salary.replace('.', '', 1).isdigit():
        raise ValueError("Salary must be a number.")
        
    write_biodata_to_file(file, name, cnic, age, salary)
        
    contact_number = input("Enter Contact Number: ")
    append_contact_number_to_file(file, contact_number)
        
    read_file(file)
        
except ValueError as v:
    print(v)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
