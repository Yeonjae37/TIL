## Optimality of Deterministic Markov Policies
- Underlying assumption: $S, A$ are finite sets.
![[deterministic_markov.png|525]]
Remark
- For finite MDPs, it suffices to consider deterministic Markov policies.
- finite MDP에서는 optimal policy를 찾을 때 deterministic Markov policy만 봐도 충분하다.

## Proof
방금 theorem으로 정의한 policy $\pi^*$(Bellman equation의 오른쪽을 최대화하는 action으로 정의한 policy)가 정말 optimal policy인가? 
즉 최종적으로 보이고 싶은 것은 : $v_t^{\pi^*} = v_t^*$ 이다.
- **By definition, we have $v_t^{\pi^*} \le v_t^*$ for each $t$.**
- **We use mathematical induction to show that $v_t^{\pi^*} \ge v_t^*$ for wach $t$.**
	- $\pi^*$가 진짜 optimal policy임을 보이려면 반대 방향도 보여야 한다.
	- 그러면 두 개를 합쳐서 $v_t^{\pi^*}(s) = v^*_t(s)$가 됨을 알 수 있다.
	- 왜 mathematical induction을 쓰는가?
		- finite horizon에서는 시간이 뒤에서 앞으로 연결되어 있다. $v_t$를 알기 위해서는 $v_{t+1}$이 필요하다.
		- 먼저 마지막 시간 $T$에서 성립하는지 보고 그 다음 $t+1$에서 성립한다고 가정하면 $t$에서도 성립한다.
- **For $t = T, v_T^{\pi^*} = r_T = v^*_T.$**
	- 마지막 시간 $T$에서는 더 이상 action을 선택하지 않는다. 그냥 terminal reward만 받음. 그래서 어떤 policy를 쓰든: $v_T^{\pi^*}(s) = r_T(s)$이고, optimal value도: $v_T^*(s) = r_T(s)$이다. 이게 induction의 시작 지점.
- **Suppose now that $v_{t+1}^{\pi^*} \ge v_{t+1}^*$ , Then we have** $$\sum_{s'\in S}p(s'|s,\pi_t^*(s))v_{t+1}^{\pi^*}(s') \ge \sum_{s'\in S}p(s'|s,\pi_t^*(s))v_{t+1}^*(s')$$
	- 다음 시간 $t+1$에서는 $\pi^*$를 따랐을 때의 value가 optimal value보다 크거나 같다고 가정하자.
	- 확률로 weighted sum을 해도 부등호의 방향은 유지된다. 즉, 각 state에서 왼쪽 값이 오른쪽 값보다 크거나 같으면, 그 값들을 확률 평균해도 왼쪽 평균이 오른쪽 평균보다 크거나 같다.
- **By the definition of $\pi_t^*$, we have for all $a \in A$** $$r_t(s,\pi_t^*(s)) + \sum_{s'}p(s'|s,\pi_t^*(s))v_{t+1}^*(s') \ge r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s')$$
	- 여기서 $\pi^*_t(s)$를  이렇게 정의함.$$ \pi_t^*(s) \in \arg\max_{a\in A} \left[ r_t(s,a)+ \sum_{s'}p(s'|s,a)v_{t+1}^*(s') \right] $$
	- 즉 $\pi_t^*(s)$는 괄호 안의 값을 가장 크게 만드는 action이다. 그래서 어떤 다른 action $a$와 비교해도: "$\pi_t^*(s)$를 선택했을 때의 값 $\ge$ $a$를 선택했을 때의 값" 이 성립한다.
- **Combining the two inequalities, we have for all $a \in A$** $$r_t(s,\pi_t^*(s)) + \sum_{s'}p(s'|s,\pi_t^*(s))v_{t+1}^{\pi^*}(s') \ge r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s')$$
	- 여기서 왼쪽 항은 사실 policy $\pi^*$를 따랐을 때의 Bellman evaluation 식이다. 따라서 방금 부등식은 
	- $v_t^{\pi^*}(s) \ge r_t(s,a) + \sum_{s'}p(s'|s,a)v_{t+1}^*(s')$ 이렇게 볼 수 있고, 이게 모든 action $a \in A$에 대해 성립한다.
	- 왼쪽은 $a$에 의존하지 않은 고정된 숫자였던 반면, 오른쪽은 $a$에 따라 달라진다. 
	- 그런데 왼쪽이 모든 $a$에 대한 오른쪽 값보다 크거나 같다면, 오른쪽 값들 중 가장 큰 값보다도 크거나 같다. 그래서 $v_t^{\pi^*}(s) \ge \max_{a\in A} \left[ r_t(s,a)+ \sum_{s'}p(s'|s,a)v_{t+1}^*(s') \right]$ 
	- 그런데 Bellman equation에 의해 오른쪽 max는 바로 $v_t^*(s)$이다. 따라서 아래와 같은 식을 얻게 된다.
- **Taking maximum of both sides w.r.t. $a$ yields**$$v_t^{\pi^*}(s) \ge v_t^*(s).$$
	**Therefore, the result follows.**
- 최종적으로 왜 equality인가?
	처음에 이미 정의상 $v_t^{\pi^*}(s)\le v_t^*(s)$를 알고 있었다. 이번 induction으로 반대 방향을 보였으므로 둘 다 성립하여 : $$v_t^{\pi^*}(s)=v_t^*(s).$$
	- $v_t^{\pi^*}(s)$ : 이 policy를 실제로 따랐을 때의 값
	- $v_t^*(s)$ : 가능한 모든 policy 중 최고의 값
	- $\pi^*$: 행동 규칙 (그 최고값을 얻으려면 어떤 action을 골라야 하는가?) optimal policy
## Deterministic vs Stochastic Policy
**Q) Can we construct an optimal policy, which is stochastic?**
최적 정책을 stochastic policy로 만들 수 있는가?
-> 가능하다. 단, 최적 action이 여러 개 있을 때 가능하다.'

## Dynamic Programming (Backward Induction) Algorithm
- 목표는 $v_t^*(s)$와 $\pi^*_t(s)$를 동시에 찾는 것. 각 시간 $t$, 각 state $s$에서의 optimal value와 optimal action을 계산한다.
- Initialize $$v_T^*(s):=r_T(s) \qquad \forall s ;$$
	- 마지막 시간 $T$에서는 더 이상 action을 선택하지 않으므로, value는 terminal reward와 같다.
- For $t = T -1: -1:0$, set
$$v_t^*(s) := \max_{a\in A} \left( r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}^*(s') \right) \qquad \forall s ;$$
$$ \pi_t^*(s) \in \arg\max_{a\in A} \left( r_t(s,a) + \sum_{s'\in S}p(s'|s,a)v_{t+1}^*(s') \right) \qquad \forall s;$$
- Properties:
	- It finds the optimal value function for each stage.
	- It finds an optimal policy. There could be multiple optimal policies.
		Q) Why?

## Example: Two-State MDP
Two-State MDP 예제로 backward induction을 직접 계산해보자

- $T = 3, S:=\{1, 2\}, A:=\{1,2\}$
- $p(1|1,1) = 0.5, p(2|1,1) = 0.5$
- $p(1|1,2) = 0.7, p(2|1,2) = 0.3$
- $p(1|2,1) = 0.2, p(2|2,1) = 0.8$
- $p(1|2,2) = 0.6, p(2|2,2) = 0.4$
- $r(1,1)=2, r(1,2)=1, r(2,1)=0, r(2,2) = 1, r_T ≡ 0$

#### Step 1: $t = 3$
- $v_3(1)=v_3(2)=0$ 
	- $T=3$에서는 terminal reward만 있음.
#### Step 2: $t = 2$ 계산
- 현재 state가 1일 때, 
	- action 1 : $r(1,1) + p(1|1,1)v_3(1) + p(2|1,1)v_3(2)$
		$= 2 + 0.5 \cdot 0 + 0.5 \cdot 0 = 2$
	- action 2 : $r(1,2) + p(1|1,2)v_3(1) + p(2|1,2)v_3(2)$
		$= 1 + 0.7 \cdot 0 + 0.3 \cdot 0 = 1$
	- $v_2(1) = max\{2,1\} = 2$
	- $\pi_2(1) = 1$
- 현재 state가 2일 때,
	- action 1 : $r(2,1) + p(1|2,1)v_3(1) + p(2|2,1)v_3(2)$
		$= 0 + 0.2 \cdot 0 + 0.8 \cdot 0 = 0$
	- action 2 : $r(2,2) + p(1|2,1)v_3(1) + p(2|2,2)v_3(2)$
		$= 1 + 0.6 \cdot 0 + 0.4 \cdot 0 = 1$
	- $v_2(2) = max\{0,1\} = 1$
	- $\pi_2(2) = 2$
#### Step 3: $t=1$ 계산
- 현재 state가 1일 때,
	- action 1 : $r(1,1) + p(1|1,1)v_2(1) + p(2|1,1)v_2(2)$
		$= 2 + 0.5 \cdot 2 + 0.5 \cdot 1$
		$= 2 + 1 + 0.5 = 3.5$
	- action 2 : $r(1,2) + p(1|1,2)v_2(1) + p(2|1,2)v_2(2)$
		$= 1 + 0.7 \cdot 2 + 0.3 \cdot 1$
		$= 1 + 1.4 + 0.3 = 2.7$
	- $v_1(1) = max\{3.5, 2.7\} = 3.5$
	- $\pi_1(1) = 1$
- 현재 state가 2일 때,
	- action 1 : $r(2,1) + p(1|2,1)v_2(1) + p(2|2,1)v_2(2)$
		$= 0+0.2 \cdot 2 + 0.8 \cdot 1$
		$= 0.4 + 0.8 = 1.2$
	- action 2 : $r(2,2) + p(1|2,2)v_2(1) + p(2|2,2)v_2(2)$
		$= 1 + 0.6 \cdot 2 + 0.4 \cdot 1$
		$= 1 + 1.2 + 0.4 = 2.6$
	- $v_1(2) = max{1.2, 2.6} = 2.6$
	- $\pi_1(2) = 2$

## Extension to Continuous Control
discrete MDP에서 continuous control 문제로 넘어가는 부분.
보통 실제 제어 문제에서는 state와 action이 연속값인 경우가 많다.
- System model: 
		$s_{t+1} = f(s_t, a_t, w_t),$ 
	where the prob. distribution of $w_t$ is known ($p_w(\cdot))$
	- 다음 state는 현재 state, action, noise에 의해 결정된다.
	- $w_t$ : randomness
- The problem: $$ \max_\pi \mathbb E^\pi \left[ \sum_{t=0}^{T-1}r(s_t,a_t)+r(s_T) \right] $$
- Q) How can we solve this problem?

## Bellman Equation
- Q) What is transition probability?
	$p(s'|s,a)=p_w(w)\mathbf{1}_{\{s'=f(s,a,w)\}}$
	- 원래 기존 Discrete MDP에서는 transition probability $p(s'|s,a)$를 직접 줬다. 그런데 continuous control에서는 next state를 직접 확률표로 주는 대신, $s' = f(s, a, w)$라는 dynamics와 $w$의 분포를 준다. 즉 randomness는 $s'$ 자체에서 오는 게 아니라 $w$에서 온다. 
	- 그래서 다음 state $s'$가 될 확률은: 어떤 noise $w$가 나와서 $f(s, a, w) = s'$가 되는가? 로 결정된다.
	- $\mathbf{1}_{\{s'=f(s,a,w)\}} = \begin{cases} 1, & s'=f(s,a,w)\text{이면}\\ 0, & \text{아니면} \end{cases}$
		- $p_w(w)$에 이 indicator를 곱하면, $s'=f(s,a,w)$를 만족하는 $w$만 남기고 나머지 $w$는 0으로 제거하는 효과가 있다.
- Q) What is the Bellman equation? $$ v_t(s) = \sup_{a\in A} \left[ r(s,a) + \int_{s'\in S} v_{t+1}(s')p(ds'|s,a) \right]$$
	- $p(ds'|s,a)$는 "다음 state $s'$에 대한 확률분포"를 의미한다.
	- Discrete : $\sum_{s'}p(s'|s,a)v_{t+1}(s')$
	- Continuous : $\int_{s'\in S}v_{t+1}(s')p(ds'|s,a)$
	- $sup$ : supremum, 상한의 최솟값. "가장 큰 값에 한없이 가까운 값"
- Q) How can we rewrite it using $p_w$? $$v_t(s) = \sup_{a\in A} \left[ r(s,a) + \int_w v_{t+1}(f(s,a,w))p_w(dw) \right]$$
	- $s'$가 랜덤인 이유는 사실 noise $w$가 랜덤이기 때문이다. 즉 next state $s'$가 독립적으로 랜덤하게 튀어나오는게 아니라, $w$가 랜덤으로 뽑히고, 그 다음에 $s' = f(s, a, w)$로 next state가 결정되는 구조다.
	- 그러면 $s'$에 대해 적분하는 대신, noise $w$에 대해 적분할 수 있다. 이게 위 식임.
	- 즉 discrete에서 $\sum_{s'}p(s'|s,a)v_{t+1}(s')$ 였던 것이 continuous system model에서는 $\int_w v_{t+1}(f(s,a,w))p_w(dw)$가 된 것
## Optimal Policy
Q) How can we construct an optimal policy?
$$\pi_t^*(s) \in \arg\max_{a\in A} \left[ r(s,a) + \int_w v_{t+1}(f(s,a,w))p_w(dw) \right]$$
- 현재 state $s$에서 가능한 action $a$를 넣어보고, 이 값이 가장 큰 action을 고르면 된다. 이 값은 action $a$의 점수임. "action score = 현재 reward + noise를 고려한 next state value 평균" 그 점수가 가장 큰 action을 고르는 게 optimal policy이다.
Note: Existence of an optimal policy is not quaranteed!
- continuous action space에서는 최대값이 실제로 달성되지 않을 수 있다.
- 최적에 가까운 policy는 만들 수 있다.
## Dynamic Programmin Algorithm for Continous Control
- Initialize $$v_T^*(s):=r_T(s) \qquad \forall s$$
	- 마지막 시점에는 terminal reward만 받으므로 discrete와 똑같음
- For $t = T - 1 : -1 : 0,$ set$$v_t^*(s) := \sup_{a\in A} \left[ r(s,a) + \int_w v_{t+1}^*(f(s,a,w))p_w(dw) \right]$$
	- 각 state $s$에 대해서, optimal value function을 계산
$$\pi_t^*(s) \in \arg\max_{a\in A} \left[ r(s,a) + \int_w v_{t+1}^*(f(s,a,w))p_w(dw) \right]$$
	- maximixer가 존재하면, optimal policy를 만든다.
- Properties:
	- It finds the optimal value function for each stage.
		- 각 시간 $t$에 대해 $v_t^*(s)$를 찾는다.
	- An optimal policy may not exist. It finds an optimal policy if a maximizer exists.
		- continuous control에서는 optimal value는 $sup$으로 계산할 수 있어도, 그 값을 실제로 달성하는 action이 없으면 optimal policy는 없을 수 있다. 하지만 어떤 action이 실제로 그 값을 달성한다면, 즉 maximizer가 존재한다면, argmax를 통해 optimal policy를 찾을 수 있다.
- It finds an optimal policy. There could be multiple optimal policies.
	- Q) Why?
	- 어떤 state에서 최댓값을 만드는 action이 여러 개일수 있기 때문