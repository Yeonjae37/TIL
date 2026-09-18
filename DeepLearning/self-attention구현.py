import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SelfAttention(nn.Module):
  """Scaled Dot-Product Self-Attention"""

  def __init__(self, d_model, d_k):
    super().__init__()
    self.d_k = d_k
    self.W_Q = nn.Linear(d_model, d_k, bias=False)
    self.W_K = nn.Linear(d_model, d_k, bias=False)
    self.W_V = nn.Linear(d_model, d_k, bias=False)

  def forward(self, x, mask=None):
    Q = self.W_Q(x)  # (batch, n, d_k)
    K = self.W_K(x)  # (batch, n, d_k)
    V = self.W_V(x)

    # Step 1: Q·Kᵀ / √d_k
    scores = torch.bmm(Q, K.transpose(1, 2)) / math.sqrt(self.d_k)

    # scores: (batch, n, n)
    # Step 2: Causal mask (optional)
    if mask is not None:
      scores = scores.masked_fill(mask == 0, float('-inf'))

    # Step 3: Softmax → attention weights
    weights = F.softmax(scores, dim=-1)

    output = torch.bmm(weights, V)
    return output, weights

attn = SelfAttention(d_model=64, d_k=32)
x = torch.randn(2, 10, 64)
out, w = attn(x)
print(f"입력: {x.shape}")
print(f"출력: {out.shape}")
print(f"어텐션 가중치: {w.shape}")
print(f"행 합: {w.sum(-1)[0,:3]}")

n = 10
causal_mask = torch.tril(torch.ones(n, n)).unsqueeze(0)
out_causal, w_causal = attn(x, mask=causal_mask)
print(f"\nCausal mak 후 미래 가중치:")
print(f)