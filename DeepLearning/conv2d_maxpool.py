import torch
import torch.nn as nn

# 단일 conv2d 레이어
conv = nn.Conv2d(
  in_channels=1, # 입력
  out_channels=32, # 출력
  kernel_size=3,
  stride=1,
  padding=1
)

x = torch.randn(1, 1, 28, 28) # 배치1, 채널1, 28 x 28

out = conv(x) # 입력 x를 합성곱층 conv 통과시켜 out 얻기
print(f"입력: {x.shape}") # [1, 1, 28, 28]
print(f"출력: {out.shape}") # [1, 32, 28, 28] : 배치1, 채널32, 28 x 28
print(f"파라미터: {sum(p.numel() for p in conv.parameters())}")


# Conv + ReLU + MaxPool 조합
block = nn.Sequential(
    nn.Conv2d(1, 32, 3, padding=1), # [1,28,28] -> [32,28,28]]
    nn.ReLU(),
    nn.MaxPool2d(2, 2), # [32,28,28] -> [32,14,14]
    nn.Conv2d(32, 64, 3, padding=1), # [32,14,14] -> [64,14,14]
    nn.ReLU(),
    nn.MaxPool2d(2, 2) # [64,14,14] -> [64,7,7]
)

out2 = block(x)
print(f"\n2-layer 출력: {out2.shape}") # [1, 64, 7, 7]

total = 0
for name, module in block.named_modules():
  if hasattr(module, 'weight') and module.weight is not None:
    p = module.weight.numel() + module.bias.numel()
    total += p 
    print(f"{name}: {module} -> {p}개 파라미터")

print(f"총 파라미터 수: {total}")