# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   ### WRITE SOLUTION CODE HERE
   dep_employee = list(map(mod, employee_list))
   return dep_employee

def generate_usernames(mod_list):
   
   ### WRITE SOLUTION CODE HERE
   list_employee = [employee.replace(" ", "_") for employee in mod_list]

   return list_employee


def map_id_to_initial(employee_list):
   
   ### WRITE SOLUTION CODE HERE
    dic_employee = {employee['name'][0]:employee['id'] for employee in employee_list}

    return dic_employee
   





mod_emp_list = to_mod_list(employee_list)
print("Modified employee list: " + str(mod_emp_list) + "\n")

print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

print(f"Initials and ids: {map_id_to_initial(employee_list)}")


