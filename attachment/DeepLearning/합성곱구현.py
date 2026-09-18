import torch
import torch.nn.functional as F

def conv2d_manual(x, kernel):
  """x: (H, W), kernel: (kH, kW) -> out: (H-kH+1, W-kW+1)"""

  H, W = x.shape
  kH, kW = kernel.shape

  oH, oW = H - kH + 1, W - kW + 1
  output = torch.zeros(oH, oW)

  for i in range(oH):
    for j in range(oW):
      # 입력 해당 영역과 커널의 원소별 곱 -> 합산
      patch = x[i:i+kH, j:j+kW]
      output[i, j] = (patch * kernel).sum()
  
  return output

x = torch.tensor([
    [1., 0., 1., 0., 1.],
    [0., 1., 0., 1., 0.],
    [1., 1., 1., 0., 0.],
    [0., 0., 1., 1., 1.],
    [1., 0., 0., 1., 0.]
])

kernel = torch.tensor([
    [ 1.,  2.,  1.],
    [ 0.,  0.,  0.],
    [-1., -2., -1.]
])

out_manual = conv2d_manual(x, kernel)
print("수동 합성곱 결과:\n", out_manual)

# 원래 x는 그냥 2차원 (5,5)
# 첫 번째 unsquueze(0) : 배치 차원 추가
# 두 번째 unsqueeze(0) : 채널 차원 추가
x_rd = x.unsqueeze(0).unsqueeze(0) # (1, 1, 5, 5)
k_4d = kernel.unsqueeze(0).unsqueeze(0) # (1, 1, 3, 3)
out_torch = F.conv2d(x_rd, k_4d).squeeze()

print("\nF.conv2d 결과:")
print(out_torch)
print(f"\n차이: {(out_manual - out_torch).abs().max().item()}")

import time
big_x = torch.randn(1, 1, 224, 224)
big_k = torch.randn(1, 1, 3, 3)

t0 = time.time()
_ = F.conv2d(big_x, big_k)
t_torch = time.time() - t0
print(f"\nF.conv2d 속도: {t_torch*1000:.2f}ms")