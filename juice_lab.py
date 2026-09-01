# 飲料設計師實驗室 — Python 版（果汁配方最佳化）
# 資料來源：Navarrete-González et al. (2026) Sustainable Food Technol., 4, 947-960 (CC-BY 4.0)
# 執行環境：Google Colab 或本機 Python（需要 numpy, scipy）

import numpy as np
from scipy.optimize import minimize

# ---------- 論文式 9：總多酚 (mg GAE/mL) ----------
def total_phenolics(x):
    a, g, c = x  # 蘋果、葡萄、蔓越莓的質量分率
    return (224.62*a + 606.16*g + 600.54*c
            + 33.90*a*g + 197.52*g*c - 241.47*c*a)

# ---------- Table 6：黏度 (cP，百分比尺度) ----------
def viscosity(x):
    A, G, C = np.array(x) * 100
    return (0.1685*A + 0.0059*G + 0.2709*C
            + 0.0093*A*G - 0.0044*A*C + 0.0026*G*C)

# ---------- 式 6 + Table S3：密度 (g/mL) ----------
def density(x):
    a, g, c = x
    return 1 / (a/1.024 + g/1.053 + c/1.024)

# ========== 第一步：無限制最佳化（只守質量守恆） ==========
res = minimize(lambda x: -total_phenolics(x),
               x0=[1/3, 1/3, 1/3],
               bounds=[(0, 1)]*3,
               constraints={'type': 'eq', 'fun': lambda x: sum(x) - 1})
a, g, c = res.x
print("── 無限制最佳解 ──")
print(f"蘋果 {a:.1%}、葡萄 {g:.1%}、蔓越莓 {c:.1%} → TP = {total_phenolics(res.x):.1f}")
print(f"黏度 {viscosity(res.x):.1f} cP、密度 {density(res.x):.3f} g/mL")
print("→ 檢查看看：這個配方通過黏度 20–26、密度 1.00–1.04 的限制嗎？\n")

# ========== 第二步：加上真實世界的限制（約束最佳化） ==========
cons = [
    {'type': 'eq',   'fun': lambda x: sum(x) - 1},
    {'type': 'ineq', 'fun': lambda x: viscosity(x) - 20},    # 黏度 > 20
    {'type': 'ineq', 'fun': lambda x: 26 - viscosity(x)},    # 黏度 < 26
    {'type': 'ineq', 'fun': lambda x: density(x) - 1.00},    # 密度 > 1.00
    {'type': 'ineq', 'fun': lambda x: 1.04 - density(x)},    # 密度 < 1.04
]
res2 = minimize(lambda x: -total_phenolics(x),
                x0=[1/3, 1/3, 1/3], bounds=[(0, 1)]*3, constraints=cons)
a, g, c = res2.x
print("── 有限制最佳解（真實的食品設計） ──")
print(f"蘋果 {a:.1%}、葡萄 {g:.1%}、蔓越莓 {c:.1%} → TP = {total_phenolics(res2.x):.1f}")
print(f"黏度 {viscosity(res2.x):.1f} cP、密度 {density(res2.x):.3f} g/mL")
print("→ 論文的理論最佳解是 14% / 44% / 42% → TP = 564.5，比較看看！")
