import torch
import torch.nn as nn

class BasicBlock(nn.Module):
  """ResNet BasicBlock: 3x3 Conv 2개 + Skip Connection"""
  expansion = 1 # 출력 채널 = 입력 채널 x expansion

  def __init__(self, in_channels, out_channels, stride=1, downsample=None):
    super().__init__()
    self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride=stride, padidng=1, bias=False)
    self.bn1 = nn.BatchNorm2d(out_channels)
    self.relu = nn.ReLU(inplace=True)
    self.conv2 = nn.Conv2d(out_channels, out_channels, 3, stride=1, padding=1, bias=False)
    self.bn2 = nn.BatchNorm2d(out_channels)

    # 차원이 다를 때 projection shortcut
    self.downsample = downsample

    def forward(self, x):
      identity = x # shortcut connection용 입력 저장
      # 입력 x를 identity라는 변수에 저장해두고 나중에 잔차랑 더하는거임
      out = self.conv1(x)
      out = self.bn1(out)
      out = self.relu(out)
      out = self.conv2(out)
      out = self.bn2(out)

      if self.downsample is not None:
        identity = self.downsample(x)

      out += identity
      out = self.relu(out)
      return out
      
block = BasicBlock(64, 64)
x = torch.randn(2, 64, 56, 56)
y = block(x)
print(f"입력: {x.shape} -> 출력: {y.shape}")
# 입력: torch.Size([2, 64, 56, 56]) -> 출력: torch.Size([2, 64, 56, 56])
downsample = nn.Sequential(nn.Conv2d(64, 128, 1, stride=2, bias=False), nn.BatchNorm2d(128))
block_down = BasicBlock(64, 128, stride=2, downsample=downsample)
y2 = block_down(x)
print(f"입력: {x.shape} -> 출력: {y2.shape}")