
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
	Q) How can we solve this problem?