import torch
import torch.nn as nn

class Bottleneck(nn.Module):
  """ResNet Bottleneck: 1×1→3×3→1×1 + Skip"""
  expansion = 4  # 출력 채널 = out_channels × 4

  def __init__(self, in_channels, out_channels, stride=1, downsample=None):
    super().__init__()
    self.conv1 = nn.Conv2d(in_channels, out_channels, 1, bias=False)  # 축소
    self.bn1 = nn.BatchNorm2d(out_channels)
    self.conv2 = nn.Conv2d(out_channels, out_channels, 3,
                            stride=stride, padding=1, bias=False)       # 핵심
    self.bn2 = nn.BatchNorm2d(out_channels)
    self.conv3 = nn.Conv2d(out_channels, out_channels * 4, 1, bias=False) # 복원
    self.bn3 = nn.BatchNorm2d(out_channels * 4)
    self.relu = nn.ReLU(inplace=True)
    self.downsample = downsample

  def forward(self, x):
    identity = x
    out = self.relu(self.bn1(self.conv1(x)))   # 256→64
    out = self.relu(self.bn2(self.conv2(out)))  # 64→64 (3×3)
    out = self.bn3(self.conv3(out))             # 64→256
    if self.downsample: identity = self.downsample(x)
    out += identity  # F(x) + x
    return self.relu(out)

class ResNet(nn.Module):
  def __init__(self, block, layers, num_classes=1000):
    super().__init__()
    self.in_channels = 64
    # Stem: 7×7 Conv + MaxPool
    self.conv1 = nn.Conv2d(3, 64, 7, stride=2, padding=3, bias=False)
    self.bn1 = nn.BatchNorm2d(64)
    self.relu = nn.ReLU(inplace=True)
    self.maxpool = nn.MaxPool2d(3, stride=2, padding=1)
    # 4개 Stage
    self.layer1 = self._make_layer(block, 64,  layers[0])
    self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
    self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
    self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
    # Head
    self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
    self.fc = nn.Linear(512 * block.expansion, num_classes)

  def _make_layer(self, block, out_ch, num_blocks, stride=1):
    downsample = None
    if stride != 1 or self.in_channels != out_ch * block.expansion:
        downsample = nn.Sequential(
            nn.Conv2d(self.in_channels, out_ch * block.expansion,
                      1, stride=stride, bias=False),
            nn.BatchNorm2d(out_ch * block.expansion))
    layers = [block(self.in_channels, out_ch, stride, downsample)]
    self.in_channels = out_ch * block.expansion
    for _ in range(1, num_blocks):
        layers.append(block(self.in_channels, out_ch))
    return nn.Sequential(*layers)

  def forward(self, x):
    x = self.maxpool(self.relu(self.bn1(self.conv1(x))))  # [B,64,56,56]
    x = self.layer1(x)   # [B, 256, 56, 56]  (ResNet-50)
    x = self.layer2(x)   # [B, 512, 28, 28]
    x = self.layer3(x)   # [B, 1024, 14, 14]
    x = self.layer4(x)   # [B, 2048, 7, 7]
    x = self.avgpool(x)  # [B, 2048, 1, 1]
    return self.fc(torch.flatten(x, 1))

# 모델 생성
resnet50 = ResNet(Bottleneck, [3, 4, 6, 3])   # ResNet-50
resnet101 = ResNet(Bottleneck, [3, 4, 23, 3])  # ResNet-101
resnet18 = ResNet(BasicBlock, [2, 2, 2, 2])    # ResNet-18