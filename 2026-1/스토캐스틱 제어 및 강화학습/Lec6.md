
$\sum_{t=0}r^t|r(s_t,a_t)| < M/{1-r}$  6pg bounded 관련 설명
$P^\pi = [P(1|1,\pi(1)), P(n | 1, \pi(1)), P(1|n, \pi(n)), P(n| n, \pi(n))]$ -> matrix

## Recap: Extension to Continuous Control
- System model: 
		$S_{t+1} = f(s_t, a_t, w_t),$
		where the prob. distribution of $w_t$ is know $(p_w(\cdot))$
		- noise $w_t$가 어떤 확률분포를 따르는지는 알고 있다고 가정한다.
		- ex) $w_t$가 작은 값일 확
- The problem:
	$$max_{\pi} \mathbb E^\pi \left[ \sum_{t=0}^{T-1}r(s_t,a_t)+r(s_T) \right]$$
	- policy $\pi$를 잘 골라서, 0부터 $T-1$까지 받는 reward와 마지막 terminal reward의 기대값을 최대화하라.
	Q) How can we solve this problem?
		- 뒤에서 앞으로 dynamic programming 하기!

## Infinite-Horizon Discounted MDP
![[discounted_MDP.png|525]]
discounted MDP는 다섯 가지 요소로 구성된다.
-  $S$: State space
	- 가능한 state들의 집합
- $A$: Action space
	- 가능한 action들의 집합
- $p$ : state transition probability
	- $p(s'|s,a)$
	- 현재 state가 $s$이고 action $a$를 했을 때, 다음 state가 $s'$가 될 확률
- $r$ : reward function
	- 현재 state $s_t$와 action $a_t$가 주어지면 그때 받는 reward를 반환
	- $r(s,a)$ = state $s$에서 action $a$를 했을 때 즉시 받는 reward
- $\gamma$ : discount factor
	- $0 \le \gamma \le 1$
	- 미래 reward를 현재보다 조금 낮게 평가하는 계수
왜 discounted가 필요한가?
- finite horizon에서는 reward를 $T$까지만 더했다.
- 그런데 infinite horizon에서는 끝이 없다. 계속 더하면 reward가 양수일 때 무한대로 발산할 수 있다.
## Assumptions
- Stationary rewards and transition probabilities:
	- $r(s,a)$ and $p(s'|s,a)$ do not vary over time
		- reward function과 transition probability 가 시간에 따라 변하지 않는다.
		- finite horizon에서는 $r_t(s,a), p_t(s'|s,a)$처럼 시간 $t$에 따라 달라질 수 있었다.
		- 하지만 infinite horizon discounted MDP에서는 보통 시간 index $t$가 없다. 
		- 즉 같은 state $s$, 같은 action $a$라면, 지금이 $t = 0$이든 $t=100$이든 reward와 transition probability가 같다. 이걸 stationary라고 한다.
- Finite state and action sets:
	- Thus, the reward $r(s,a)$ is bounded, i.e., there exists a constant $M$ such that
	- $|r(s,a)|<M \qquad \forall s\in S,\ \forall a\in A$
		- state와 action의 개수가 유한하며, 모든 state와 action에 대해 reward의 절댓값이 어떤 상수 $M$보다 작다. (reward가 무한히 커지거나 작아지지 않는다)
- Discounting: $0 \le \gamma < 1$
## Policy Evaluation
- Let's first consider a simple problem of evaluating$$\mathbb E^\pi \left[ \sum_{t=0}^{\infty}\gamma^t r(s_t,a_t) \right]$$
	- 어떤 policy $\pi$가 주어졌을 때, 이 policy를 따르면 expected discounted return이 얼마인가?
	- $r(s_0,a_0) + \gamma r(s_1,a_1) + \gamma^2 r(s_2,a_2) + \gamma^3 r(s_3,a_3) + \cdots$의 기대값을 계산하는 것
- A key concept for the policy evaluation is the value function.
![[policy_evaluation.png|525]]
	- 시간 $t$에 state $s$에서 시작해서 policy $\pi$를 계속 따르면 받을 expected discounted return
## Stationary Policies
- In principle, a policy is given by
		$\pi := (\pi_0, \pi_1, \pi_2, ...)$
	- $\pi_t$는 time $t$에서 사용하는 decision rule이다.
- The policy is said to be stationary if
		$\pi_i = \pi_j \qquad \forall i, j.$
	- 모든 시간에서 같은 decision rule을 쓰는 policy
- We just consider a stationary policy as a decision rule, i.e.,
	- $\pi(s_t) = a_t$ (deterministic stationary)
	- or $\pi(a_t|s_t)$ (stochastic stationary)
## Policy Evaluation
Idea:
- Decompose the value function into
	($i$) immediate reward; plus
	($ii$) discounted value of next state:
$$v^\pi(s) = \mathbb E^\pi \left[ r(s_t,a_t) + \gamma v^\pi(s_{t+1}) \mid s_t=s \right] $$
$$v^\pi(s) = \sum_{a\in A} \pi(a|s) \left( r(s,a) + \gamma \sum_{s'\in S} p(s'|s,a)v^\pi(s') \right)$$
## Proof
증명하려는 식:
$$ v^\pi(s) = \sum_{a\in A}\pi(a|s) \left[ r(s,a) + \gamma \sum_{s'\in S}p(s'|s,a)v^\pi(s') \right]$$
1. Value function의 정의
	원래 value function은 : $$v^\pi(s) = \mathbb E^\pi \left[ \sum_{\tau=t}^{\infty} \gamma^{\tau-t}r(s_\tau,a_\tau) \mid s_t=s \right]$$
	첫 reward와 나머지 future reward로 나누면, 안쪽 sum의 지수가 $\gamma^{r-t-1}$가 된다.
	$$v^\pi(s) = \mathbb E^\pi \left[ r(s_t,a_t) + \gamma \sum_{\tau=t+1}^{\infty} \gamma^{\tau-t-1}r(s_\tau,a_\tau) \mid s_t=s \right]$$
2. $s_{t+1}$을 조건부기댓값으로 넣기$$= \mathbb E^\pi \left[ r(s_t,a_t) + \gamma \mathbb E^\pi \left[ \sum_{\tau=t+1}^{\infty} \gamma^{\tau-t-1}r(s_\tau,a_\tau) \mid s_{t+1} \right] \mid s_t=s \right]$$
	tower rule을 쓴 것. "미래 reward의 기대값을 바로 계산하지 말고, 먼저 다음 state $s_{t+1}$가 무엇인지 알고 있다고 생각한 뒤 계산하고, 다시 $s_{t+1}$에 대해 평균낸다"
3. 안쪽 기대값이 $v^\pi(s_t+1)$가 됨$$= \mathbb E^\pi \left[ r(s_t,a_t) + \gamma v^\pi(s_{t+1}) \mid s_t=s \right]$$
4. expectation을 sum으로 풀기$$= \sum_{a\in A} \pi(a|s) \left[ r(s,a) + \gamma \sum_{s'\in S} p(s'|s,a)v^\pi(s') \right]$$
	여기서 랜덤성이 두 개 존재. 
	- 첫 번째 랜덤성은 action. 현재 state가 $s$일 때, policy $\pi$가 action $a$를 선택할 확률은: $\pi(a|s)$, action에 대해 평균내면: $\sum_{a\in A}\pi(a|s)(\cdots)$
	- 두 번째 랜덤성은 next state. 현재 state $s$에서 action $a$를 했을 때 다음 state $s'$가 될 확률은: $p(s'|s,a)$
	- 그래서 next state value의 기대값은 $\sum_{s'\in S}p(s'|s,a)v^\pi(s')$

## Vector Form
방금 식을 모든 state에 대해 한꺼번에 써보자.
Let $S := {1, ... , n}$ and $A := {1, ..., m}$ 이라고 하면, 
We often use the following notation:
- $v^\pi := (v^\pi(1),\ldots,v^\pi(n)) \in \mathbb R^n$
	- 각 state의 value를 세로로 모은 벡터
- $R^\pi := \left( \sum_{a\in A}\pi(a|1)r(1,a), \ldots, \sum_{a\in A}\pi(a|n)r(n,a) \right) \in \mathbb R^n$
	각 state에서 policy $\pi$가 만드는 expected immediate reward.
	When $\pi$ is deterministic, it's simplified to
	$R^\pi := (r(1, \pi(1)), ..., r(n, \pi(n))) \in \mathbb{R}^n$
- Transition probability matrix: $$P^\pi := \begin{bmatrix} \sum_{a\in A}\pi(a|1)p(1|1,a) & \cdots & \sum_{a\in A}\pi(a|1)p(n|1,a) \\ \vdots & \ddots & \vdots \\ \sum_{a\in A}\pi(a|n)p(1|n,a) & \cdots & \sum_{a\in A}\pi(a|n)p(n|n,a) \end{bmatrix} \in \mathbb{R}^{n\times n}$$
	- 복잡해보이지만 $P^\pi(i,j) = \sum_{a\in A}\pi(a|i)p(j|i,a)$ 라고 보면 된다. 
	- 현재 state가 $i$일 때, policy $\pi$를 따라 action을 고르면, 다음 state가 $j$가 될 전체 확률
- Then, the policy evaluation equation can be expressed as
	$v^\pi = R^\pi + \gamma P^\pi v^\pi$
	- 왜? 
	- scalar form은: $$v^\pi(s) = \sum_{a\in A}\pi(a|s) \left[ r(s,a) + \gamma \sum_{s'\in S}p(s'|s,a)v^\pi(s') \right]$$ 이었다. 이걸 각 state $s$ = 1, ..., n 에 대해 모두 쓰면 : $$v^\pi(1)=R^\pi(1)+\gamma\sum_{s'}P^\pi(1,s')v^\pi(s')$$ $$v^\pi(2)=R^\pi(2)+\gamma\sum_{s'}P^\pi(2,s')v^\pi(s')$$ $$v^\pi(n)=R^\pi(n)+\gamma\sum_{s'}P^\pi(n,s')v^\pi(s')$$
	- 이걸 행렬식으로 한 번에 쓰면 : $v^\pi = R^\pi + \gamma P^\pi v^\pi$

## Properties
$v^\pi = R^\pi+\gamma P^\pi v^\pi$ 이 방정식이 왜 잘 풀리는가
- The eigenvalues of $P^\pi$ are less than or equal to 1. Q) Why?
	- $P^\pi$는 transition probability matrix임. 각 row는 현재 state 하나를 의미하고, 그 row의 원소들은 다음 state로 갈 확률들이다. 확률 transition matrix는 벡터를 곱했을 때 값을 무한히 폭발시키는 행렬이 아님. 그래서 eigenvalue의 크기가 1 이하가 된다.
- The linear equation $v = R^\pi + \gamma P^\pi v$ has a unique solution. Q) Why?
	- $v^\pi = R^\pi+\gamma P^\pi v^\pi$ 를 $v$에 대해 정리하면 $v-\gamma P^\pi v=R^\pi$ , $(I-\gamma P^\pi)v=R^\pi$ 
	- 따라서 $v=(I-\gamma P^\pi)^{-1}R^\pi$가 된다. 여기서 중요한 건 $I - \gamma P^\pi$가 invertible(역행렬이 존재)이어야 한다는 것이다. 왜 invertible이냐? $P^\pi$의 eigenvalue 크기는 1 이하이다. $|\lambda (P^\pi)| \le 1$ 그리고 $0 \le \gamma < 1$ 이니까 $|\gamma \lambda(P^\pi)| < 1$ 이 됌.
	- 즉 $\lambda P^\pi$의 eigenvalue들은 모두 크기가 1보다 작다. 그러면 $I - \lambda P^\pi$는 0 eigen value를 갖지 않는다. 그래서 inverse가 존재한다. 따라서 solution이 하나로 정해진다. 이게 unique solution
- The unique solution is given by $$v^\pi = (I-\gamma P^\pi)^{-1}R^\pi = \sum_{t=0}^{\infty}(\gamma P^\pi)^tR^\pi$$
- This method is inefficient for large-scale problems.
	- state 수 $n$이 크면 $P^\pi$는 $n \times n$ matrix이다. 예를 들어 state가 1,000,000개면 행렬의 inverse를 직접 구하는 건 거의 불가능하거나 매우 비효율적이다. 그래서 실제 큰 문제에서는 inverse를 직접 계산하지 않고 value iteration 같은 반복 알고리즘을 사용한다.

## Operator Form
- Let $T^\pi:\mathbb R^n\to \mathbb R^n$ be defined by
$$T^\pi v := R^\pi+\gamma P^\pi v$$
어떤 임의의 vector $v$를 넣으면, $R^\pi + \gamma P^\pi v$ 를 계산해서 새로운 vector를 반환한다.
- Thus, $$(T^\pi v)(s) = \sum_{a\in A}\pi(a|s) \left[ r(s,a) + \gamma \sum_{s'\in S}p(s'|s,a)v(s') \right]$$
- The policy evaluation equation can be expressed as $$v^\pi=T^\pi v^\pi$$
 or $$v^\pi(s)=(T^\pi v^\pi)(s)$$
 which is a fixed point problem.
	 - Fixed point problem이란?
	 -  어떤 함수 $F$가 있을 때, $x = F(x)$를 만족하는 $x$를 fixed point라고 함. $x$를 넣어도 값이 변하지 않기 때문
	 - 우리 문제에서는 함수가 $T^\pi$이고 찾는 값은 $v^\pi$이다. 즉 $v^\pi = T^\pi v^\pi$를 만족하는 value vector를 찾는 문제
	 - $T^\pi$로 한 번 업데이트해도 변하지 않는 value vector가 $v^\pi$다.

## Contraction Property
- $T^\pi$는 value vector들을 점점 서로 가깝게 만드는 함수이다.
![[contraction_property.png|525]]
- 두 벡터 $v, v'$가 있을 때, $T$를 한 번 적용하면 두 벡터 사이의 거리가 줄어든다. 이런 함수를 contraction이라고 한다.
- $T^\pi$를 한 번 적용하면 value vector들 사이의 거리가 $\gamma$배 이하로 줄어든다.
- 어떤 stationary policy $\pi$에 대해서도, operator $T^\pi$는 $||\cdot||_\infty$ 기준으로 $\gamma - contraction$이다.
	-  $\gamma - contraction$ : 다음 부등식 $\|T^\pi v-T^\pi v'\|_\infty \le \gamma \|v-v'\|_\infty$을 만족한다는 뜻
	- $\|v\|_\infty$ 는 vector 안의 값들 중 절대값이 가장 큰 값
	- $T^\pi$라는 업데이트 함수는, value vector들 사이의 거리를 $||\cdot||_\infty$라는 방식으로 측정했을 때, 그 거리를 최대 $\gamma$배로 줄이는 함수다.

Q) Why?

## Banach Fixed Point Theorem
![[fixed_point.png|525]]

어떤 operator $T$가 contraction이면, fixed point가 딱 하나 존재하고, 아무 초기값에서 시작해서 $T$를 반복 적용하면 그 fixed point로 수렴한다.
$v^* = Tv^*$를 만족하는 $v^*$가 유일하게 존재하고, $v_(k+1) = T_{v_k}$로 반복하면 $v_k \rightarrow v^*$ 가 된다는 말
$v^\pi$는 이미 policy $\pi$의 정확한 value이기 때문에, Bellman update를 한 번 더 해도 변하지 않는다.
Remark:
- Our policy evaluation equation has a unique solution.
- $v^\pi$ can be obtained by value iteration.

## Value Iteration Algorithm for Policy Evaluation
Input: stationary policy $\pi$
- Initialize $v_0$ as an arbitary vector in $\mathbb{R}^n;$
- Repeat until convergence
	$v_k+1 := T^\pi_{v_k};$ 
	