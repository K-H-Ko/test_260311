import uvicorn
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# pip install 
import jwt


app = FastAPI()
cors_config = {
    "allow_origins":"http://localhost:3000/",
    "allow_credentials":True,
    "allow_methods":["*"],
    "allow_headers":["*"]
}
app.add_middleware(
    CORSMiddleware, 
    **cors_config
    # **: 언패킹 -> 딕셔너리 키 값을 옵션명 value 값을 옵션값
    # allow_origins = http://localhost:3000/
) 

from sqlalchemy import create_engine, text

user_id = "root"
db_password = "test"
host = "localhost:3307"
db_name = "ex260310"
db_info = f"mysql+pymysql://{user_id}:{db_password}@{host}/{db_name}"
print(db_info)
engine = create_engine(
    db_info, connect_args={})
print(engine)

@app.post("/login")
def login(
        token = Body(...,embed=True)
    ):
    print(token)
    decoded = jwt.decode(token, options={
        "verify_signature":False})
    print(decoded)
    
    query = text("""
    SELECT count(*) as n FROM users
    WHERE email = :email & name = :name
    """)
    
    email = decoded["email"] 
    name = decoded["name"] 
    with engine.connect() as conn:
        row = conn.execute(
            query, {"email":email,
                    "name":name}
        ).fetchone()
    print(row[0])
    if row[0]==0:
        return JSONResponse(
          status_code = status.HTTP_400_BAD_REQUEST,
          content = {"massage":"로그인 실패"}
        )
        
    return JSONResponse(
        status_code= status.HTTP_200_OK,
        content={"message":"로그인 성공"}
    ) 

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host = "0.0.0.0",
        port = 5000, reload = True
    )
    
