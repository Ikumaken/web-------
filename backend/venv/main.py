from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# フロントエンドからの通信（CORS）を許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発中なので一旦すべて許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 最初のAPI（ルートパスにアクセスしたらメッセージを返す）
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}