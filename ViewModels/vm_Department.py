from pydantic import BaseModel, EmailStr, Field,ConfigDict
from typing import Optional, Annotated,List

class SubDeparementResponse(BaseModel):
    subdepartmentid: Annotated[int, Field(...)]
    subdeparment_name: Annotated[str, Field(...)]

    model_config = ConfigDict(from_attributes=True)

class DepartmentBase(BaseModel):
    department_name:Annotated[str,Field(...)]

    model_config = ConfigDict(from_attributes=True)



class DepartmentResponse(DepartmentBase):
    department_id:Annotated[int,Field(...)]
    subdepartment: List[SubDeparementResponse] = Field(
    default_factory=list
)
