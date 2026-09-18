import torch
import torch.nn as nn

class InceptionModule(nn.Module):
  """Inception Module with 1x1 bottleneck (GoogleNet style)"""

  def __init__(self, in_channels, 
              ch1x1,           # 경로1: 1x1 출력 채널
              ch3x3_reduce,    # 경로2: 1x1 보틀넥 채널
              ch3x3,           # 경로2: 3x3 출력 채널
              ch5x5_reduce,    # 경로2: 1x1 보틀넥 채널
              ch5x5,           # 경로3: 5x5 출력 채널
              pool_proj):      # 경로4: Pool 후 1x1 채널
    super().__init__()

# 경로 1: 1x1 Conv
    self.branch1 = nn.Sequential(
      nn.Covn2d(in_channels, ch1x1, kernel_size=1),
      nn.BatchNorm2d(ch1x1),
      nn.ReLU(inplace=True)
    )

# 경로 2: 1x1 -> 3x3 (중간 패턴)
    self.branch2 = nn.Sequential(
      nn.Conv2d(in_channels, ch3x3_reduce, kernel_size=1),
      nn.BatchNorm2d(ch3x3_reduce),
      nn.ReLU(inplace=True),
      nn.Conv2d(ch3x3_reduce, ch3x3, kernel_size=3, padding=1),
      nn.BatchNorm2d(ch3x3),
      nn.ReLU(inplace=True)
    )

# 경로 3: 1x1 -> 5x5 (넓은 패턴))
    self.branch3 = nn.Sequential(
      nn.Conv2d(in_channels, ch5x5_reduce, kernel_size=1),
      nn.BatchNorm2d(ch5x5_reduce),
      nn.ReLU(inplace=True),
      nn.Conv2d(ch5x5_reduce, ch5x5, kernel_size=5, padding=2), # 패딩=2로 5x5 후에도 크기 유지
      nn.BatchNorm2d(ch5x5),
      nn.ReLU(inplace=True)
    )

# 경로 4: MaxPool -> 1x1 (압축 패턴)
    self.branch4 = nn.Sequential(
      nn.MaxPool2d(kernel_size=3, stride=1, padding=1),
      nn.Conv2d(in_channels, pool_proj, kernel_size=1),
      nn.BatchNorm2d(pool_proj),
      nn.ReLU(inplace=True)
    )

  def forward(self, x):
    b1 = self.branch1(x)
    b2 = self.branch2(x)
    b3 = self.branch3(x)
    b4 = self.branch4(x)
    return torch.cat([b1, b2, b3, b4], dim=1) # 채널 방향으로 합치기


module = InceptionModule(
  in_channels=192,
  ch1x1=64,
  ch3x3_reduce=96,
  ch3x3=128,
  ch5x5_reduce=16,
  ch5x5=32,
  pool_proj=32
)

x = torch.randn(1, 192, 28, 28) # 배치1, 채널192, 28x28
out = module(x)
print(f"입력: {x.shape} -> 출력: {out.shape}")
# 입력: torch.Size([1, 192, 28, 28]) -> 출력