import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge, Lasso
from sklearn.pipeline import make_pipeline

np.random.seed(42)
n = 200
X = np.random.randn(n, 5)


# 실제로는 x0, x1만 중요함. x2~x4는 노이즈
y = 3 * X[:, 0] + 1.5 * X[:, 1] + 0 * X[:, 2] + 0 * X[:, 3] + 0 * X[:, 4] +  np.random.randn(n) * 0.5

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

alphas = np.logspace(-3, 3, 50) # 0.001 ~ 1000
feature_names = ['x0 (중요)', 'x1 (중요)', 'x2 (노이즈)', 'x3 (노이즈)', 'x4 (노이즈)']

print("=== Ridge 회귀 (L2 정규화) ===") 
print(f"{'alpha':>10}  " + "  ".join(f"{n:>10}" for n in feature_names))
