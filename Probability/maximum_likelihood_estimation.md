# Maximum Likelihood Estimation (최대우도법)

### Likelihood란
확률: 주어진 확률 분포에서 해당 관측값이 나올 확률  
Likelihood : 주어진 관측값이 특정 확률분포로부터 나왔을 확률(PDF의 y값인듯)

Likelihood는 아래와 같은 식으로 표현할 수 있다.   
$L(\theta) = p(X|\theta)$

Likelihood는 어떻게 계산할 수 있을까?   
한 개의 데이터가 정규분포를 따를 확률은 아래와 같다.

$p(x_n|\theta)=\frac{1}{\sqrt{2\pi }\sigma }\exp \left(-\frac{\left(x_n-\mu \right)^2}{2\sigma ^2}\right)\ \ \left(x\in R\right)$

i.i.d (indpendent and identically distributed)  
각 데이터가 서로 영향을 주지 않고 모두 같은 $\theta$에서 생성된다고 가정한다. -> 각 확률의 곱으로 식을 나타내면 아래와 같이 likelihood를 나타낼 수 있다.

$L(\theta) = p(X|\theta) = \prod_{n=1}^N p(x_n|\theta)$

## Maximum Likelihood Estimation
Maximum Likelihood Estimation은 Likelihood 함수의 최대값을 찾는 방법이라고 할 수 있다. 

$\hat{\theta} = argmax_\theta L(\theta)$ 

$\hat{\theta}_{MLE} = argmax_\theta \Sigma_{n=1}^{N}log  p(y_n|x_n, \theta)$ 

대부분 알고리즘은 최소화(minimize)만 지원한다. 그래서 Negative log likelihood로 변경한다.  

$argmaxf(x) = argmin(-f(x))$

$NLL(\theta) = -\Sigma_{n=1}^Nlogp(y_n|x_n, \theta)$

## MLE for the Bernoulli Distribution
동전 던지기  
y = 1 $\to$ 앞면  
y = 0 $\to$ 뒷면

$\theta = P(Y=1)$  

베르누이 PMF : $p(y_n|\theta) = \theta^{y_n}(1-\theta)^{1-y_n}$

$NLL(\theta) = -log\prod_{N=1}^{N}p(y_n|\theta)$

= $-log\prod_{n=1}^{N}\theta^{y_n}(1-\theta)^{1-y_n}$

= $-\Sigma_{n=1}^{N}log(\theta^{y_n}(1-\theta)^{1-y_n})$

= $-\Sigma_{n=1}^{N}[y_nlog\theta +(1-y_n)log(1-\theta)]$

= $-[N_1log\theta + N_0log(1-\theta)]$

최적 $\theta$를 찾기 위해 미분

$\frac{d} {d\theta}NLL(\theta) = \frac{-N_1}{\theta} + \frac{N_0}{1-\theta}$

$\frac{-N_1}{\theta} + \frac{N_0}{1-\theta} = 0$

$\frac{N_0}{1-\theta} = \frac{N_1}{\theta}$

$N_0\theta = N_1(1-\theta)$

$N_0\theta = N_1 - N_1\theta$

$(N_0 + N_1)\theta = N_1$

$\theta = \frac{N_1}{N_0 + N_1}$

$\hat{\theta}_{MLE} = \frac{N_1}{N}$

