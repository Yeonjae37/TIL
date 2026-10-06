# Finite Horizon Markov Decision Processes I
## Example: Stochastic Inventory Control
- State: $s_t$ inventory level at stage $t$ (시간 t에서의 재고량)
- Action: $a_t$ # of units ordered at stage $t$ (시간 t에서 몇 개를 주문할지)
- $D_t$ : random demand at stage $t$ with $p_j := P(D_t = j)$ (시간 t에서의 랜덤 수요)
	- $p_j$ = 수요가 j개일 확률
System equation:
		$s_{t+1} = max\{s_t + a_t - D_t, 0\}$ excess demand is lost
		다음 재고 = 현재 재고 + 주문량 - 수요
Setting
- State set : $S = \{0, 1, ..., M\}$ ($M$: storage capacity)
- Action set : $A_s = {0, 1, ..., M - s}$
	- 가능한 action이 현재 state $s$에 따라 달라진다. 
	- 현재 재고가 $s$개 있을 때, 최대 용량이 $M$이므로 주문 후 재고 $s+a$는 $M$을 넘으면 안 됌.
- Reward function : $r_t(s, a) = F(s + a) - O(a) - h(s+a)$
	- 현재 state $s$에서 $a$개 주문했을 때의 reward
	- $F(s + a)$는 주문 후 보유 재고 $s+a$에 따른 판매 수익 revenue
	- $O(a)$는 $a$개를 주문하는 데 드는 주문 비용 ordering cost
	- $h(s+a)$는 $s+a$개를 보관하는 데 드는 재고 보관 비용 holding cost
	- 너무 많이 주문하면 수요를 놓칠 확률은 줄지만, 주문 비용과 보관 비용이 커진다. 너무 적게 주문하면 비용은 줄지만, 수요가 많을 때 팔 물건이 부족해서 수익을 놓친다.
- Transition probabilities: 
	- $p(s'|s,a) = 0$ if $s + a < s'\le M$
		- 현재 주문 후 재고가 $s+a$개 인데, 다음 재고 $s'$가 그보다 클 수는 없다. 그래서 $s' > s+a$인 경우 확률은 0이다.
	- $p(s'|s,a) = p_{s+a-s'}$  if  $0 < s' \le s + a$
		- 다음 재고가 양수로 남는 경우
		- System equation에서 $s'>0$이면 $s'=s+a-D_t$ 따라서 $D_t=s+a-s'$가 됌.
		- 수요가 $j$일 확률을 $p_j=P(D_t=j)$라고 했으니까, $P(s_{t+1}=s') =P(D_t=s+a-s')=p_{s+a-s'}$
	- $p(s'|s,a) = \Sigma_{j \ge s+a}p_j$ if $s' = 0$
		- 다음 재고가 0이 되는 경우
		- 재고가 0이 되려면 수요가 현재 보유량 $s+a$ 이상이면 됌.

## Value Function
- Let's first consider a simpler problem of evaluating
$$\mathbb E^\pi \left[ \sum_{t=0}^{T-1} r_t(s_t,a_t) + r_T(s_T) \right]$$
given a policy $\pi := (\pi_0, ..., \pi_{T-1})$ (Policy evaluation).
	- $t=0$부터 $T-1$까지 action을 선택하면서 reward를 받고, 마지막 시점 $T$에서는 terminal reward $r_T(s_T)$ 를 받는다.
	- $r_T(s_T)$는 action에 대한 reward가 아니라 마지막 state에 대한 reward이다.
	- 예를 들어 재고 문제라면 $T$일이 끝났을 때 남은 재고에 대한 salvage value나 penalty일 수 있다.
	- finite horizon 에서는 시간마다 다른 decision rule을 쓸 수 있다. finite horizon에서는 남은 시간이 중요하다. 예를 들어 재고 관리 문제에서 오늘이 첫날이면 안정적 운영을 위해 적당히 주문할 수 있고, 마지막 날 직전이면 재고를 남기면 안되므로 주문을 훨씬 적게 할 수 있다.
- A key concept for the policy evaluation is the value function.

![[value_function_finite.jpeg|508]]

: 시간 $t$에 state가 $s$라고 주어졌을 때, policy $\pi$를 따라 $t$부터 $T$까지 행동하면 받을 것으로 기대되는 총 reward.
"$v_t^\pi(s) = \text{time } t$에서 state $s$로 시작했을 때 남은 기간 동안의 expected return"
finite horizon에서는 같은 state $s$라도 현재 시간이 언제냐에 따라 가치가 달라진다. 그래서 시간 $t$를 명시함.

Q) What is $v_T^\pi(s)$?
$t=T$를 넣으면, 
$\sum_{\tau=T}^{T-1}$ 시작 인덱스가 끝보다 크기 때문에 0이 된다. 따라서 남는 건 $v_T^\pi(s) = \mathbb E^\pi \left[ r_T(s_T) \mid s_T=s \right]$ 
그런데 $s_T=s$라고 조건을 걸었기 때문에 $r_T(s_T) = r_T(s)$ 가 된다.
따라서 $v_T^\pi(s)=r_T(s)$ 가 된다. 
의미는: 마지막 시간 $T$에서는 더 이상 action을 선택하지 않고, terminal reward만 받는다.

## Optimal Policies
- Seek a policy $\pi^*$ with the largest expected total reward, i.e.,
$$v_0^{\pi^*}(s) \ge v_0^\pi(s) \qquad \forall s,\ \forall \pi$$
	Such a policy is called an optimal policy.
	
: 모든 state $s$에 대해, 그리고 모든 가능한 policy $\pi$에 대해, optimal policy $\pi^*$를 따랐을 때의 value는 임의의 policy $\pi$를 따랐을 때의 value보다 크거나 같다.

- In some models an optimal policy may not exist, so instead we seek an $\epsilon$-optimal policy $\pi^*_\epsilon$, i.e., for an $\epsilon > 0$, 
$$ v_0^{\pi_\epsilon^*}(s)+\epsilon > v_0^\pi(s) \qquad \forall s,\forall \pi $$
: 어떤 모델에서는 정확히 최적인 policy가 존재하지 않을 수 있고, 대신 거의 최적인 policy를 찾는다. 즉 $\pi^*_\epsilon$는 따른 어떤 policy보다 최대 $\epsilon$ 정도만 손해 보는 policy이다. 완전히 최적은 아닐 수 있지만, 최적 성능에 $\epsilon$ 이내로 가까운 policy

## Optimal Value Function
![[optimal_value_function.jpeg]]

- $v^*_t(s)$ = time $t$부터 남은 기간 동안 최적으로 행동했을 때의 최대 기대 보상
- $v^*_0$ specifies the best possible performance in the MDP
- By definition, we have 
		$v_0^{\pi^*} = v^*_0$.
	- 최적 policy $\pi^*$을 따르면, 모든 초기 state에서 optimal value를 달성한다.

## Finite-Horizon Policy Evaluation
: optimal policy를 찾는 게 아니라 이미 policy $\pi$가 주어졌을 때, 그 policy가 얼마나 좋은지 계산하는 단계
Idea: 
- Decompose the value function into
	($i$) immediate reward; plus
	($ii$) expected value of next state:
	-> 현재 value = immediate reward + expected value of next state
	$$ v_t^\pi(s) = \mathbb E^\pi \left[ r_t(s_t,a_t) + v_{t+1}^\pi(s_{t+1}) \mid s_t=s \right]$$
	**deterministic policy: **$$v_t^\pi(s) = r_t(s,\pi_t(s)) + \sum_{s'\in S} p(s'|s,\pi_t(s))v_{t+1}^\pi(s')$$
	- action은 확정, next state는 확률적
	
	**stochastic policy:**$$ v_t^\pi(s) = \sum_{a\in A} \pi_t(a|s) \left( r_t(s,a) + \sum_{s'\in S} p(s'|s,a)v_{t+1}^\pi(s') \right)$$
	: state $s$에서 policy $\pi_t$가 선택할 수 있는 모든 action $a$에 대해, 그 action을 선택할 확률 $\pi_t(a|s)$로 평균낸다. 각 action의 가치는 지금 reward와 next state value의 기대값이다.
	- stochastic policy에서는 두 번 평균을 낸다. action 선택의 랜덤성에 대한 평균, environment transition의 랜덤성에 대한 평균
## Finite-Horizon Policy Evaluation Algorithm
Algorithm:
- Initialize $$ v_T^\pi(s):=r_T(s) \qquad \forall s$$
	마지막 시간 $T$ 에서는 더 이상 action을 고르지 않는다. 그냥 terminal reward만 받음.
	
- For $t = T - 1 : -1 : 0$, set $$ v_t^\pi(s) := \sum_{a\in A} \pi_t(a|s) \left( r_t(s,a) + \sum_{s'\in S} p(s'|s,a)v_{t+1}^\pi(s') \right) \qquad \forall s $$
	이걸 모든 state $s$에 대해 계산한다.

## Bellman Equation
- Let's go back to the original MDP problem.
- Consider the following equation, called the Bellman equation:$$v_t(s) = \max_{a\in A} \left( r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}(s') \right) \forall s\in S $$
	with $v_T(s) = r_T(s).$ $\rightarrow$ 이 부분이 시작점
	: 시간 $t$, state $s$에서의 최적 value는 가능한 action $a$들 중에서 "지금 reward + 다음 state value의 기대값"이 가장 큰 action을 골랐을 때의 값이다.

- Useful properties:
	- Solutions to the Bellman equations are the optimal value functions for each $t$.
	- It provides a method for verifying whether a policy is optimal.
	- It provides an efficient procedure for computing optimal value functions and policies.
	- It may be used to identify structural properties of optimal polices and value functions.

## Principle of Optimality
![[principle_op_optimality.jpeg|501]]
- Bellman equation의 철학을 나타내는 부분
- "어떤 최적 정책의 나머지 부분은, 첫 action 이후 도달한 state에서 다시 최적이어야 한다."
- 핵심은 다음 state의 value가 그냥 $v_{t+1}$이 아니라 $v^*_{t+1}$이라는 것이다. 즉 다음 state에 도착한 뒤에는 다시 최적으로 행동한다는 뜻이다.
## Proof
: finite-horizon Bellman equation이 왜 성립하는지 증명하고, 그 결과로 optimal policy를 어떻게 만드는지 보여주는 부분
1. 증명 하고 싶은 것 $$v_t^*(s) = \max_{a\in A} \left[ r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}^*(s') \right]$$
	: 시간 $t$, state $s$에서의 optimal value는 지금 action $a$를 하나 고르고, 지금 reward를 받고, 다음 state $s'$부터는 다시 optimal value를 따른다고 생각했을 때, 그 값이 최대가 되는 action을 고른 결과다.
	
	이걸 보이기 위해서는 보통 두 방향을 보여야 한다. $$v_t^*(s) \le \max_a(\cdots)$$ 그리고 $$v_t^*(s) \ge \max_a(\cdots)$$
	이 두 개를 모두 보이면 결국 등호가 된다.

2. 현재 reward와 미래 reward를 나눈다. $$v_t^*(s) = \max_\pi \mathbb E^\pi \left[ r_t(s_t,a_t) + \sum_{\tau=t+1}^{T-1}r_\tau(s_\tau,a_\tau) + r_T(s_T) \mid s_t=s \right]$$
	: time $t$, state $s$에서 시작해서, 가능한 모든 policy 중 expected total reward가 가장 큰 값
	
3. Tower rule이란?$$= \max_\pi\mathbb E^\pi \left[ r_t(s_t,a_t) + \mathbb E^\pi \left[ \sum_{\tau=t+1}^{T-1}r_\tau(s_\tau,a_\tau)+r_T(s_T) \mid s_{t+1} \right] \mid s_t=s \right]$$
	: 직관적으로는 전체 미래 reward의 기대값을 바로 계산하지 말고, 먼저 다음 state $s_{t+1}$가 정해졌다고 생각하고 그 이후의 기대값을 계산한 다음, 그 결과를 다시 $s_{t+1}$의 확률에 대해 평균낸다.
	즉, $\mathbb E[X] = \mathbb E[\mathbb E[X|Y]]$ 원리임.
		원래는 : $$\mathbb E^\pi \left[ r_t + r_{t+1} + r_{t+2} +\cdots +r_T \mid s_t=s \right]$$
		Tower rule을 쓰면 : $$\mathbb E^\pi \left[ r_t + \mathbb E^\pi [ r_{t+1}+r_{t+2}+\cdots+r_T \mid s_{t+1} ] \mid s_t=s \right]$$
		여기서 안쪽 기대값 : $$ \mathbb E^\pi [ r_{t+1}+r_{t+2}+\cdots+r_T \mid s_{t+1} ]$$ 이 바로 $v_{t+1}^{\pi}(s_{t+1})$ 이다. 즉 tower rule 덕분에 "미래 reward 전체 $\rightarrow$ 다음 state의 value"로 바꿀 수 있게 된다.
		
4. 왜 $v_{t+1}^*(s_{t+1})$로 upper bound 할 수 있나? $$\le \max_\pi \mathbb E^\pi \left[ r_t(s_t,a_t) + v_{t+1}^*(s_{t+1}) \mid s_t=s \right]$$
	왜 $\le$ 가 되냐면, $v_{t+1}^{\pi}(s_{t+1})$ 는 time $t + 1$, state $s_{t+1}$에서 시작했을 때 가능한 모든 policy 중 최대 value가 된다. 
	반면 안쪽의 $$\mathbb E^\pi \left[ \sum_{\tau=t+1}^{T-1}r_\tau(s_\tau,a_\tau)+r_T(s_T) \mid s_{t+1} \right]$$
	는 특정 policy $\pi$의 나머지 부분을 따랐을 때의 value이다. 특정 policy의 value는 optimal value보다 클 수 없다. 그래서 $\text{future value under policy} \space \pi \le v_{t+1}^*(s_{t+1})$ 가 된다.

5. 마지막 줄: action에 대한 max로 바뀐다. $$= \max_{a\in A} \left[ r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}^*(s') \right]$$
	$s_t = s$가 주어져 있으니까, policy가 현재 시점에 하는 일은 결국 action $a$를 고르는 것이다. 그리고 action $a$를 선택하면 다음 state $s'$는 확률 $p(s'|s,a)$로 결정된다. 그래서 다음 value의 기대값은 $$\sum_{s'\in S}p(s'|s,a)v_{t+1}^*(s')$$
	가 된다. 

#### 반대 방향에 대한 proof
$$v_t^*(s)\ge v_t^\pi(s)= \mathbb E^\pi \left[ r_t(s_t,a_t) + \sum_{\tau=t+1}^{T-1}r_\tau(s_\tau,a_\tau) + r_T(s_T) \mid s_t=s \right]$$
$$ = \mathbb E^\pi \left[ r_t(s_t,a_t) + v_{t+1}^\pi(s_{t+1}) \mid s_t=s \right]$$
: policy $\pi$를 따르면, 현재 reward를 받고, 다음 state로 간 뒤 남은 기간 동안 policy $\pi$를 계속 따른다.
만약 policy가 stochastic이면, 이걸 action 확률로 풀어서 $$v_t^\pi(s) = \sum_{a\in A} \pi_t(a|s) \left[ r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}^\pi(s') \right]$$

가 된다.
- Since the inequality above hold for any $(\pi_{t+1}, ..., \pi_{T-1}),$

$$ v_t^*(s) \ge \pi_t(a|s) \left[ r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s') \right]$$
임의의 action a$를 선택해도 $v_t^*(s)$는 그보다 크거나 같다.
- This inequality should hold for any Dirac delta $\pi_t(\dot|s)$. Therefore,
$$ v_t^*(s) \ge \max_{a\in A} \left[ r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s') \right]$$
이게 모든 action에 대해 성립하므로, 그중 가장 큰 값보다도 크거나 같아야 한다.

직관적으로 정리하면 $v_t^*(s)$는 가능한 모든 전략 중 최고 성능이므로 "지금 특정 action 하나를 고르고 이후 최적으로 행동하는 전략"보다 작을 수 없다. 이게 모든 action에 대해 성립하므로, 그중 가장 좋은 action의 값보다도 작을 수 없다.

따라서 

$${ v_t^*(s) = \max_{a\in A} \left[ r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s') \right] }$$
이 된다. 이게 finite-horizon Bellman optimality equation이다.

## Optimal Policy
Define a deterministic Markov policy $\pi^*$ by 
$$ \pi_t^*(s) \in \arg\max_{a\in A} \left( r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}^*(s') \right)$$
: time $t$, state $s$에서 가능한 모든 action 중 지금 reward와 다음 state의 optimal value 기대값을 합친 값이 가장 큰 action을 선택하라.

- Then, it is an optimal policy, i.e., $$ v^{\pi^*}=v^*$$
	즉 이 방식으로 만든 optimal policy $\pi^*$를 따르면 optimal value를 달성한다. 왜냐하면 각 time, state에서 Bellman equation의 오른쪽을 최대화하는 action을 고르기 때문. 
	즉 이 policy는 매 순간:  $$ r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s')$$
	가 가장 큰 action을 선택한다. 그 결과 현재 value가 항상 $v^*_t(s)$와 같아진다. 그래서 이 policy가 optimal policy이다.


이번에 한 증명 : "optimal value function $v_t^*$은 왜 Bellman equation을 만족하는가?"
$v_t^*(s)$의 정의에서 출발해서,
$$ v_t^*(s)=\max_\pi v_t^\pi(s)$$
전체 reward를 $$현재 reward + 미래 reward$$
로 나눈 뒤, tower rule을 쓰고, 미래 reward를 $v_{t+1}^*$로 upper/lower bound 하면서 Bellman equation을 얻었음.
