from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated



# problem datatype error becouse python is dynamtic lang,
# def insert_data(name: str, age: int):  #python datatype not throw the errors

#     print(name)
#     print(age)
#     print('added to database')

# data = insert_data('nikhil', '26') # it allows age str this is problem 

# 2nd problem adding a data validation is messi or write more code 
# pydatic solve this main 2 problem to datatype and data validation

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50, title='enter Name', description='Enter the name of patient' )]
    email: EmailStr # normal data validation
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0 , strict=True)] # strict ture means stctly validate data "30" = error 30= correct
    married: bool = False # False is defoult value
    allergies:  Annotated[Optional[List[str]],Field(default=None , max_length=5)] #none is required and its defoult value 
    contact_details: Dict[str,str]


def insert_data(patient):  #basemodel call

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print('added to database')

patient_info ={'name' : 'nikhil','email': 'nik@gmail.com', 'age' : '26', 'weight':60, 'married':True,'allergies':['pollen', 'Dust'], 'contact_details':{'phone':'12345678'}}

patient1 = Patient(**patient_info)

insert_data(patient1)







