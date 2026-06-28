import math

def calculate_guaranteed_bounds(value: float):
    """
    入力された値に対して、簡易的に丸め誤差を考慮した下限・上限（区間）を計算する
    """
    try:
        # 本来は丸め方向を制御しますが、ここではデモとして
        # 機械イプシロン（floatの限界誤差）を考慮した区間を出力します
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