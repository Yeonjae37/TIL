import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models
from torchvision.models import ResNet50_Weights

# 1. 모델 준비
model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)

NUM_CLASSES = 10

# 2. Backbone 동결 (Feature Extraction)
for param in model.parameters():
  param.requires_grad = False

# 분류기 교체 (새 층은 자동으로 requires_grad=True)
model.fc = nn.Sequential(
  nn.Dropout(0.3),
  nn.Linear(2048, 512),
  nn.ReLU(),
  nn.Linear(512, NUM_CLASSES)
) 

# Discriminative Learning Rate 설정
def unfreeze_and_get_params(model): 
  # layer4만 풀기
  for param in model.layer4.parameters():
    param.requires_grad = True

  param_groups = [
    {'params': model.layer4.parameters(), 'lr': 1e-4}, # 후반 층 : 작은 lr
    {'params': model.fc.parameters(), 'lr': 1e-2} # 분류기 : 큰 lr
  ]
  return param_groups

# Phase 1: Feature Extraction
optimizer = optim.Adam(model.fc.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# 학습 루프
def train_epoch(model, loader, optimizer, criterion, device):
  model.train()
  total_loss, correct, total = 0, 0, 0
  for images, labels in loader:
    images, labels = images.to(device), labels.to(device)
    optimizer.zero_grad()
    outputs = model(images)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()

    total_loss += loss.item()
    correct += (outputs.argmax(1) == labels).sum().item()
    total += labels.size(0)
    return total_loss / len(loader), correct / total
  
# Phase 1: Feature Extraction (5 epochs)
for epoch in range(5):
  loss, acc = train_epoch(model, train_loader, optimizer, criterion, device)
  