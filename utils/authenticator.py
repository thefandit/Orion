from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .jsonHandler import JSONHandler, get_jason_filepath
from .encryptor import Encryptor

security = HTTPBasic()

class Authenticator:
    def __init__(self):
        self.users_handler = JSONHandler(get_jason_filepath("users.json"), custom_name="Auth")
        print(self.users_handler.load_json())
        self.app = FastAPI(dependencies=[Depends(security)])
        self.users = self.users_handler.data
        self.encryptor = Encryptor().encryptor = Encryptor()
    
    def verification(self, creds: HTTPBasicCredentials = Depends(security)):
        username = creds.username
        password = creds.password
        if username in self.users and self.encryptor.encrypt(password) == self.users[username]["password"]:
            print("User Validated")
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
