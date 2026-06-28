from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from solver import calculate_guaranteed_bounds  # 作ったロジックを読み込む

app = FastAPI()

# フロントエンドからの通信（CORS）を許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. 動作確認用のAPI（さっき試したもの）
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

# 2. 【新規】精度保証計算を実行するAPI
# 例: http://127.0.0.1:8000/calc?number=0.1 形式でデータを受け取る
@app.get("/calc")
def run_calculation(number: float):
    result = calculate_guaranteed_bounds(number)
    return result