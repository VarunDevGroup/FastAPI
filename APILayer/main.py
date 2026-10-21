
from fastapi import FastAPI
from APILayer.DepartmentAPI import router as department_router
from DBLayer.DBConnection import Base,engine

Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(department_router)




