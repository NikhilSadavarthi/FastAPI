from pydantic import BaseModel
from typing import List,Dict,Optional



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
    weight: float
    married: bool = False # False is defoult value
    allergies: Optional[List[str]] = None #none is required and its defoult value 
    contact_details: Dict[str,str]


def insert_data(patient):  #basemodel call

    print(patient.name)
    print(patient.age)
    print('added to database')

patient_info ={'name' : 'nikhil', 'age' : '26', 'weight':'60', 'married':True, 'allergies':['pollen', 'Dust'],'contact_details':{'email': 'nik@gmail.com', 'phone':'12345678'}}

patient1 = Patient(**patient_info)

insert_data(patient1)







