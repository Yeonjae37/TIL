
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
	- 각 state에서 policy $\pi$가 만드는 expected immediate reward.
	- When $\pi$ is deterministic, it's simplified to
	- $R^\pi := (r(1, \pi(1)), ..., r(n, \pi(n))) \in \mathbb{R}^n$
- Transition probability matrix: 