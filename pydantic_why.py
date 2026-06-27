from pydantic import BaseModel



# problem datatype error becouse python is dynamtic lang,
# def insert_data(name: str, age: int):  #python datatype not throw the errors

#     print(name)
#     print(age)
#     print('added to database')

# data = insert_data('nikhil', '26') # it allows age str this is problem 

# 2nd problem adding a data validation is messi or write more code 
# pydatic solve this main 2 problem to datatype and data validation

class Patient(BaseModel):
    name:str
    age: int

def insert_data(patient):  #basemodel call

    print(patient.name)
    print(patient.age)
    print('added to database')

patient_info ={'name' : 'nikhil', 'age' : 'two'}

patient1 = Patient(**patient_info)

insert_data(patient1)







