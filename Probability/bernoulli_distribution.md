# Bernoulli Distribution
결과가 딱 2개 있는 실험

ex. 동전 던지기 앞면/뒷면
Y = 1 : 앞면  
Y = 0 : 뒷면  

y = 1 -> $\theta$  
y = 0 -> $1 - \theta$

베르누이 시행에는 3가지 조건이 있다.
- 각 실험에서 발생하는 조건은 단 2가지이며, 성공 또는 실패로만 나뉜다.
- 각 시행이 모두 독립적으로 수행되며, 서로 연관이 없어야 한다.
- 모든 시험에서 시행의 확률은 동일해야 한다.

성공하는 베르누이 시행(1)이 일어날 가능성을 p라고 하면, 실패하는 베르누이 시행(0)이 일어날 가능성은 1-p로 정해진다.

$X =
\begin{cases}
1 & \text{with probability } p \\
0 & \text{with probability } 1-p
\end{cases}$  
$\to P(X=1) = P(X=success) = p$  
$\to P(X=0) = P(X=fail) = 1-p$

그렇다면 성공확률이 p인 베르누이 확률질량함수(PDF)는 아래와 같이 구해진다.  

$f(x) = P(X=x) = p^x (1-p)^{1-x}$

#### 베르누이분포의 평균
$E(x) = 1 \times p + 0 \times (1-p) = p$

#### 베르누이분포의 분산
$Var(x) = E(x)^2 - [E(x)]^2 = p - p^2 = p(1-p)$

#### 베르누이분포의 표준편차
$SD_{Berniulli} = \sqrt{p(1-p)}$