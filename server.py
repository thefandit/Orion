from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic
from utils.authenticator import Authenticator

security = HTTPBasic()
app = FastAPI(dependencies=[Depends(security)])
auth = Authenticator()

@app.get("/name/{name}")
async def search(name: str, Verifcation = Depends(auth.verification)):
    if Verifcation:
        #Insert Code Here
        return {"Hello":name}
    
