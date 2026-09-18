import torch
import torch.nn as nn
from torchvision import models
from torchvision.models import ResNet50_Weights

# 1. 사전학습 모델 로드
model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)

# 2. 모델 구조 확인
# ResNet50의 마지막 층 확인
print(model.fc)
# 출력: Linear(in_features=2048, out_features=1000, bias=True)


# 3. 분류기 교체
NUM_CLASSES = 10

# 방법 1: 단순 교체
model.fc = nn.Linear(2048, NUM_CLASSES)

# 방법 2: 더 강력한 분류기 (Dropout + 2-layer)
model.fc = nn.Sequential(
  nn.Dropout(0.3), # 입력 feature 일부를 랜덤하게 꺼서 과적합 완화
  nn.Linear(2048, 512), # 2048 차원 feature -> 512 차원
  nn.ReLU(), # 비선형성 추가
  nn.Dropout(0.2),
  nn.Linear(512, NUM_CLASSES) # 512 차원 -> 최종 클래스 수
)

# --4. EfficientNet 사용 시 --
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights

eff_model = efficientnet_b0(weights=EfficientNet_B0_Weights.IMAGENET1K_V1)
print(eff_model.classifier) # Efficie
# 출력: Sequential(Dropout, Linear(1280, 1000))

# EfficientNet 분류기 교체
eff_model.classifier = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(1280, NUM_CLASSES)
)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

print(f"전체 파라미터: {sum(p.numel() for p in model.parameters()):,}")
print(f"학습 파라미터: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")