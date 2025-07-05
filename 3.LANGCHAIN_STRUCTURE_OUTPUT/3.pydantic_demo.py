from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student') #Field: Adds constraints and metadata to a field (e.g., range for CGPA).


new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student)
# same as Student(age="32", email="abc@gmail.com")

# convert object to dict
student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)