import math
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # CORS用に追加

app = FastAPI()

# JavaScript（フロントエンド）からの通信を許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発・テスト用にすべてを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 元々あった計算ロジック
def calculate_guaranteed_bounds(value: float):
    """
    入力された値に対して、簡易的に丸め誤差を考慮した下限・上限（区間）を計算する
    """
    try:
        epsilon = math.ulp(value) if value != 0 else 5e-324
        
        lower_bound = value - epsilon
        upper_bound = value + epsilon
        
        return {
            "status": "success",
            "input_value": value,
            "lower_bound": f"{lower_bound:.20f}",
            "upper_bound": f"{upper_bound:.20f}",
            "width": f"{upper_bound - lower_bound:.20e}"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 【追加】JavaScriptから送られてくる /calc?number=◯◯ を受け取る設定
@app.get("/calc")
def calc_endpoint(number: float):
    # JavaScriptから送られてきた「number」を、上の計算関数に引き渡して結果を返す
    result = calculate_guaranteed_bounds(number)
    return result