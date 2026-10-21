from sqlalchemy.orm import Session
from DBLayer.DBModels.model_department import DepartmentModel, SubDepartmentModel
from ViewModels.vm_Department import DepartmentResponse

from DBLayer import DBConnection

def GetAllDepartment(db: Session):
    return db.query(DepartmentModel).all()


def GetSingle(db:Session, dptID:int):
    data= db.query(DepartmentModel).filter(DepartmentModel.department_id==dptID).first()
    print(data.department_name)

    for d in data.subdepartment:
        print(d.subdeparment_name)
    return data

def Update(db:Session, inputData:DepartmentResponse):
    data=GetSingle(db,inputData.department_id)

    update_data=inputData.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(data, key, value)

    db.commit()
    db.refresh(data)
    return data


def Delete(db:Session,depID:int):

    data=GetSingle(db,depID)
    if data is not None:
        db.delete(data)
        db.commit()
    else:
        raise ValueError(
            f"No department found with ID {depID}"
        )