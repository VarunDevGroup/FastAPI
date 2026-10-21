
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from BusinessLayer.departmentBLL import GetAllDepartment,GetSingle, Delete, Update
from ViewModels.vm_Department import DepartmentResponse
from typing import List
from CommonLayer.genericmethods import get_db


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

app=FastAPI()

@router.get("/GetAll", response_model=List[DepartmentResponse])
def departmentList(db:Session=Depends(get_db)):
    try:
        data= GetAllDepartment(db)
        return data
    except Exception as e:
        raise HTTPException(status_code=401,detail=str(e))


@router.get("/detail/{department_id}", response_model=DepartmentResponse)
def GetDepartmentDetails(department_id : int,db:Session=Depends(get_db)):
    try:
        data= GetSingle(db,department_id)
        
        if data is None:
            raise HTTPException(status_code=401,detail=f'No record found with matching ID {department_id}')    

        return data
    
    except Exception as e:
        raise HTTPException(status_code=401,detail=str(e))

@router.patch("/update", response_model=DepartmentResponse)
def UpdateData(inputData: DepartmentResponse, db:Session=Depends(get_db)):
    return Update(db,inputData)


@router.delete("/delete/{department_id}")
def DeleteDepartment(deparment_id:int, db:Session= Depends(get_db)):
    try:
        Delete(db,deparment_id)
        return JSONResponse(status_code=200,content='OK')

    except Exception as e:
        raise HTTPException(status_code=401,detail=str(e))


