from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from DBLayer.DBConnection import Base

class DepartmentModel(Base):
    __tablename__='tblDepartment'
    department_id=Column(Integer, primary_key=True, index=True)
    department_name=Column(String, unique=True, index=True)

    subdepartment= Relationship("SubDepartmentModel", back_populates="department")

class SubDepartmentModel(Base):
    __tablename__='tblSubDepartment'
    subdepartmentid=Column(Integer,primary_key=True)
    subdeparment_name=Column(String,unique=True,nullable=False)
    department_id=Column(Integer, ForeignKey("tblDepartment.department_id"),nullable=False)

    department=Relationship("DepartmentModel",back_populates="subdepartment")
