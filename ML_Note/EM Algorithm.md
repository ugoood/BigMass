Expectation Maximization Algorithm
===
Author: 相忠良(Zhong-Liang Xiang)
Email: ugoood@163.com
Date: Aug. 24st, 2017

### 0. 目的
求混合高斯分布(或其他分布, 但我们以 Gaussian Distribution 为例)模型的参数．

### 1. 认识
谈及EM算法，我们认为是几个高斯分布(也叫多个组份)协同地生成了一个样本．
**若各组分方差相同，就认为是 k-means 算法模型．**

### 2. 故事
假设有这样一个问题：
1. 有身高样本10000个, 既 $N=10000$;
2. 身高由男人、女人组成；
3. 认为男性身高 ~ $Normal(\mu_1, \sigma_1^2)$;
      　　女性身高 ~ $Normal(\mu_2, \sigma_2^2)$;
4. 10000个人中男女比例未知，既 $\pi_1$, $\pi_2$ 未知
求未知参数 $\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\pi_1$ and $\pi_2$.

上面的故事中, 样本 $x_i$ 是一维的．若 $x_i$ 是5维的，则对应的：
* $\mu$ 是5维的;
* $\Sigma$ 是5*5的半正定方阵(因为高维，把$\sigma^2$换成了$\Sigma$);
* $\pi$ 是比例，仍为标量.

### 3. EM算法
第一步(E-step), 估算数据来自哪个组份．
对于**每个样本$x_i$, 它由第$k$个组份生成的概率为**：
$$r(i,k)=\dfrac{\pi_kN(x_i|\mu_k,\Sigma_k)}{\sum_{j=1}^k\pi_jN(x_i|\mu_j,\Sigma_j)}$$

举个栗子：

$$r(i,male)=\dfrac{\pi_{male}N(x_i|\mu_{male},\Sigma_{male})}{\pi_{male}N(x_i|\mu_{male},\Sigma_{male})+\pi_{female}N(x_i|\mu_{female},\Sigma_{female})}$$

<font color = red>注意：为了计算 $r(i,k)$, 我们需先验地给出 $\pi,\mu,\Sigma$. 另外，还得事先给出 $k$．如男女身高的例子，$k\in \{1,2\}$.</font>

第二步(M-step), 估计每个组份的参数.
**认为每个组份都服从高斯分布，只是各组份各自的$\mu,\sigma^2,\pi$不同．**
根据第一步得到的$r(i,k)$, 更新下列内容：
$$N_k=\sum_{i=1}^kr(i,k)$$
$$\mu_k=\dfrac{1}{N_k}\sum_{i=1}^Nr(i,k)x_i$$
$$\Sigma_k=\dfrac{1}{N_k}\sum_{i=1}^Nr(i,k)(x_i-\mu_k)(x_i-\mu_k)^T$$
$$\pi_k=\dfrac{N_k}{N}=\dfrac{1}{N}\sum_{i=1}^Nr(i,k)$$
重复做 E -> M -> ... -> E -> M 至收敛或达到指定循环次数，求得最终参数 $\pi^*,\mu^*,\Sigma^*$.

### 4. 收敛性证明(TODO)
