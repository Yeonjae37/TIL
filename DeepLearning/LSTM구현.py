import torch
import torch.nn as nn

class LSTMCellManual(nn.Module):
  def __init__(self, input_size, hidden_size):
    super().__init__()
    self.hidden_size = hidden_size

    # 핵심: 4개 게이트를 하나의 큰 행렬로 결합 (재매개변수화)
    # [forget, input, output, cell_candidate] 순서

    self.W = nn.Linear(input_size + hidden_size, 4 * hidden_size)
    # LSTM에서는 각 시점마다 현재 입력 x_t와 이전 hidden h_t-1을 같이 보고 계산해야 함.
    # 그래서 입력 차원은 input_size + hidden_size가 됨.
    # 출력은 gate가 4개니까 4 * hidden_size가 됨.

  def forward(self, x_t, state):
    h_prev, c_prev = state # 이전 은닉 상태, 이전 셀 상태

    # 1) 입력과 이전 은닉 상태 결합
    combined = torch.cat([h_prev, x_t], dim=1)

    # 2) 하나의 행렬 곱으로 4개 게이트 계산
    gates = self.W(combined)

    # 3) 4등분하여 각 게이트 분리
    f, i, o, g = gates.chunk(4, dim=1)

    # 4) 활성화 함수 적용
    f = torch.sigmoid(f) # Forget gate: 0~1
    i = torch.sigmoid(i) # Input gate: 0~1
    o = torch.sigmoid(o) # Output gate: 0~1
    g = torch.tanh(g) # Cell candidate: -1~1

    # 5) 셀 상태 업데이트: 삭제 + 추가
    c_new = f * c_prev + i * g
    # 6) 은닉 상태 출력
    h_new = o * torch.tanh(c_new)
    return h_new, c_new
  

cell = LSTMCellManual(input_size=32, hidden_size=64)
x = torch.randn(8, 32) # (batch=8, input=32)
h = torch.zeros(8, 64) # 초기 은닉 상태
c = torch.zeros(8, 64) # 초기 셀 상태
h_new, c_new = cell(x, (h, c))
print(f"h_new: {h_new.shape}, c_new: {c_new.shape}")
# h_new: torch.Size([8, 64]), c_new: torch.Size([8, 64])