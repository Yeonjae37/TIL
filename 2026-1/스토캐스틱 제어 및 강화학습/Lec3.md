## Example: Two-State MDP
### Setting
- State set: $S = \{s_1, s_2\}$
- Action set: $A_{s1} = \{a_{1,1}, a_{1,2}\}, A_{s2} = \{a_{2,1}\}$
- Rewards: $r(s_1, a_{1,1}) = 5, r(s_1, a_{1,2}) = 10, r(s_2, a_{2,1}) = -1$
- Transition probabilities: 
	- $p(s_1|s_1, a_{1,1}) = 0.5$,   $p(s_2|s_1, a_{1,1}) = 0.5$
	- $p(s_1|s_1, a_{1,2}) = 0$,      $p(s_2|s_1, a_{1,2}) = 1$
	- $p(s_1|s_2, a_{2,1}) = 0$,      $p(s_2|s_2, a_{2,1}) = 1$

### Q )
Markov policy : policy가 현재 state만 보고 action을 정한다는 뜻. 과거에 어떤 state를 지나왔는지, 예전에 어떤 action을 했는지는 보지 않는다.
1. Example of deterministic Markov policies?
	- $\pi(s_1) = a_{1,1}$,     $\pi(s_2) = a_{2,1}$
2. Example of randomized Markov policies?
	- $\pi(a_{1,1}|s_1) = 0.7$,   $\pi(a_{1,2}|s_1) = 0.3$,   $\pi(a_{2,1}|s_2) = 1$


Deterministic policy
- $\pi(s) = a$    state $s$에서 action $a$를 선택한다.
Randomized policy
- $\pi(a|s)$          state $s$에서 action $a$를 선택할 확률

## The MDP Problem
To find an optimal policy that maximized the expected cumulative reward:
 $$\displaystyle \\max_{\pi \in \Pi} \mathbb{E}^{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t r(s_t,a_t) \right]$$

- Difficult to solve
	- 지금 action이 미래 state를 바꾼다.
	- Immediate reward와 future reward 사이 trade off가 있다.
	- 확률성이 있다.
	- state와 action이 많아질수록 가능한 policy가 많다.
- Solution we'll study : Dynammic Programming (DP)

원래 강화학습의 최종 목표는 "expected cumulative reward"를 최대화하는 optimal policy $\pi^*$를 찾는 것
바로 optimal policy를 찾으려고 하면 너무 어렵다... 그래서 먼저 더 쉬운 문제를 생각해보기!
먼저 풀고 싶은 쉬운 문제: policy evaluation

## Value Function
Let's first consider a simpler problem of evaluating

$$\mathbb{E}^{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t r(s_t,a_t) \right]$$

given a policy $\pi$.

즉 policy evaluation이란 어떤 policy $\pi$가 이미 정해져 있다고 할 때, 이 policy를 따라 행동했을 때 장기적으로 reward를 얼마나 받을까? 를 계산하자는 뜻  $\rightarrow$ 즉, "최적 policy가 뭐야?"가 아닌 "이 policy가 얼마나 좋은 policy야?"를 묻는 단계

Value function : $V^\pi(s) = state\space s$ 에서 시작해서 $policy\space \pi$를  따르면 앞으로 얼마나 좋을까?, 앞으로 받을 총 reward의 기대값

![[value_function.png]]

조건부 내부 $|s_t = s$는 "현재 시간 t에서 state가 s라고 주어졌을 때" 라는 뜻

## Policy Evaluation
Idea : 
- Decompose the value function into
	(i) immediate reward
	(ii) discounted value of next state
$\rightarrow$ state $s$의 value는 policy $\pi$를 따라 행동했을 때 받는 지금 reward와 다음 state의 value를 할인한 값의 기대값이다.
 $$\displaystyle v^\pi(s) = \mathbb{E}^\pi [ r(s_t, a_t) + \gamma v^\pi(s_{t+1}) | s_t = s]$$
$$\displaystyle = \sum_{a\in A} \pi(a|s) \left( r(s,a) + \gamma
\sum_{s'\in S}
p(s'|s,a)v^\pi(s')\right)$$
- In matrix form: 
	$v^{\pi} = R^\pi + \gamma P^{\pi}v^{\pi}$
- In operator form: 
	$v^{\pi} = \tau^{\pi}v^{\pi}$

## Optimal Value Functions

![[optimal_value.png]]


$$v^*(s) := max_{\pi \in \Pi} v^{\pi}(s)$$
: 가능한 모든 policy $\pi$ 중에서, state $s$의 value를 가장 크게 만드는 값을 $v^*(s)$라고 하자.
: 현재 state가 s일 때, 가능한 모든 policy 중에서 앞으로 받을 discounted cumulative reward의 기대값이 가장 큰 값을 $v^*(s)$라고 한다.

- $v^*$ specifies the best possible performance in the MDP
- An MDP is "solved" when the optimal value function is found.
	- why? : $v^*(s)$를 알면 각 state에서 어떤 action이 최적인지 고를 수 있기 때문

## Dynamic Programming (DP)

![[DP.png]]

앞에서 배운 것들을 정리하면, 흐름은
**MDP를 푼다 = Optimal policy $\pi^*$을 찾는다**
그런데 optimal policy를 바로 찾는 대신 먼저 optimal value function $v^*(s)$를 찾을 수 있음.
**$v^*(s) = state \space s$ 에서 시작했을 때 얻을 수 있는 최대 기대 누적 reward**

value function, optimal policy, optimal value function이 헷갈릴 때...
**value function $v^\pi$** = policy $\pi$가 고정되었을 때, 각 state에서 시작하여 그 policy를 계속 따를 경우 얻는 expected discounted return.
**optimal value function $v^*(s)$** = 모든 가능한 policy 중에 가장 큰 value를 주는 함수
**optimal policy $\pi^*$** = 모든 state에서 optimal value를 달성하는 policy. 각 state에서의 return을 동시에 최대로 만드는 정책

$$ v^*(s) = \max_{a_t\in A} \mathbb E \left[ r(s_t,a_t) + \gamma v^*(s_{t+1}) \mid s_t=s \right] $$
: 현재 state가 $s$일 때, 가능한 action 중에서 **현재 reward + $\gamma$ x 다음 state의 optimal value**
의 기대값이 가장 큰 action을 고른다.
$$ v^*(s) = \max_{a\in A} \left( r(s,a) + \gamma \sum_{s'\in S} p(s'|s,a)v^*(s') \right) $$
: expectation을 transition probability로 풀어쓴 것

$\sum_{s'\in S}p(s'|s,a)v^*(s')$  $\rightarrow$ action $a$를 했을 때 가능한 모든 next state $s'$에 대해  **갈 확률 x next state s'의 optimal value** 를 더한 것. 즉 next state value의 기대값

### Policy evalution과 비교

**policy evaluation :** $$ v^\pi(s) = \sum_a \pi(a|s) \left( r(s,a) + \gamma \sum_{s'}p(s'|s,a)v^\pi(s') \right) $$
이건 정해진 policy를 따랐을 때의 value임.
즉 action 선택이 $\pi(a|s)$에 의해 정해져 있으니까, action들에 대해 policy 확률로 평균을 냄.

**Bellman optimality equation : **
$$ v^*(s) = \max_a \left( r(s,a) + \gamma \sum_{s'}p(s'|s,a)v^*(s') \right) $$
여기서는 policy가 


classify : input - image, output - text
image, 판독문 input 2개가 들어가고
원래 그렇게 하려고 생각했는데, mimic cxr이 데이터 특성 때문에 
중요한 건 
input으로 indication을 넣어줘서.. 성능을 조금만 높여줘도 프로젝트가 될 것 같다