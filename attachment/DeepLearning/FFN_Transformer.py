import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# MultiHeadAttention
from so10 import MultiHeadAttention

# --- Feed Forward Network (FFN) ---
class FFN(nn.Module):
  def __init__(self, d_model=512, d_ff=2048, dropout=0.1):
    super().__init__()
    self.net = nn.Sequential(
      nn.Linear(d_model, d_ff),
      nn.ReLU(),
      nn.Dropout(dropout),
      nn.Linear(d_ff, d_model),
      nn.Dropout(dropout)
    )
  def forward(self, x):
    return self.net(x)
  

# --- Transformer Block (Pre Norm) ---
class TransformerBlock(nn.Module):
  def __init__(self, d_model=512, n_heads=8, d_ff=2048, dropout=0.1):
    super().__init__()
    self.attn = MultiHeadAttention(d_model, n_heads)
    self.ffn = FFN(d_model, d_ff, dropout)
    self.norm1 = nn.LayerNorm(d_model)
    self.norm2 = nn.LayerNorm(d_model)
    self.drop = nn.Dropout(dropout)

  def forward(self, x, mask=None):
    x = x + self.drop(self.attn(self.norm1(x), mask))
    x = x + self.ffn(self.norm2(x))
    return x
  

block = TransformerBlock(d_model=512, n_heads=8, d_ff=2048)
x = torch.randn(2, 10, 512)
out = block(x)
print(out.shape) # [2, 10, 512]
print(x.shape) # [2, 10, 512] (입력과 동일)

