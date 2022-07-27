2022.07.19

# Adaptive Federated Optimization
https://arxiv.org/pdf/2003.00295.pdf 2021.09.08

keyword : Adaptive Optimzizer


## Abstract
Federated learning is a distributed machine learning paradigm in which a large number of clients coordinate with a central server to learn a model without sharing their own training data. Standard federated optimization methods such as Federated Averaging (FEDAVG) are often difficult to tune and exhibit unfavorable convergence behavior.
In non-federated settings, adaptive optimization methods have had notable success in combating such issues. 
In this work, we propose federated versions of adaptive optimizers, including ADAGRAD, ADAM, and YOGI, and analyze their convergence in the presence of heterogeneous data for general nonconvex settings. Our results highlight the interplay between client heterogeneity and communication efficiency. We also perform extensive experiments on these methods and show that the use of adaptive optimizers can significantly improve the performance of federated learning.
----------------------------------------------------------
...
본 연구에서, 우리는 AdaGrad, Adam, Yogi를 포함한 적응형 최적화기(adaptive optimizer)의 federated 버전을 제안하고, 일반적인 비볼록 환경에서 이질적 데이터가 존재하는 경우의 수렴을 분석한다. 우리의 결과는 클라이언트 이질성과 통신 효율성 사이의 상호 작용을 강조한다. 우리는 또한 실험을 통해 적응형 최적화기가 연합학습의 성능을 상당하게 향상시킬 수 있음을 보인다.


## 1. Introduction
While FEDAVG has seen great success, recent works have highlighted its convergence issues in some settings (Karimireddy et al., 2019; Hsu et al., 2019). This is due to a variety of factors including (1) client drift (Karimireddy et al., 2019), where local client models move away from globally optimal models, and (2) a lack of adaptivity. 
FEDAVG is similar in spirit to SGD, and may be unsuitable for settings with heavy-tail stochastic gradient noise distributions, which often arise when training language models (Zhang et al., 2019a). Such settings benefit from adaptive learning rates, which incorporate knowledge of past iterations to perform more informed optimization.
----------------------------------------------------------
FedAvg는 성공적이지만, 최근의 연구는 특정 환경에서의 수렴 문제를 부각시켰다. 이는 다음을 포함하는 여러 요인 때문이다: (1) Client Drift : 로컬 클라이언트 모델이 글로벌 최적 모델과 멀어지는 것 (2) Lack of adaptivity : 적응성의 부재
FedAvg는 SGD와 유사하며 언어 모델을 훈련할 때 종종 발생하는 헤비테일 확률적 그레이디언트 노이즈 분포를 가진 설정에 적합하지 않을 수 있다. 이러한 설정은 과거 반복에 대한 지식을 통합하여 보다 정보에 입각한 최적화를 수행하는 적응형 학습률의 이점을 제공한다.

In this paper, we focus on the second issue and present a simple framework for incorporating adaptivity in FL. In particular, we propose a general optimization framework in which (1) clients perform multiple epochs of training using a client optimizer to minimize loss on their local data and (2) server updates its global model by applying a gradient-based server optimizer to the average of the clients’ model updates.
We show that FEDAVG is the special case where SGD is used as both client and server optimizer and server learning rate is 1. This framework can also seamlessly incorporate adaptivity by using adaptive optimizers as client or server optimizers. Building upon this, we develop novel adaptive optimization techniques for FL by using per-coordinate methods as server optimizers. By focusing on adaptive server optimization, we enable use of adaptive learning rates without increase in client storage or communication costs, and ensure compatibility with cross-device FL.
-----------------------------------------------------------
이 논문에서 우리는 두번째 문제에 집중하고 FL에 적응성을 통합하기 위한 간단한 프레임워크를 제시한다. 특히, 우리는 (1) 클라이언트가 그들의 로컬 데이터에 대한 손실을 최소화하기 위해 클라이언트 최적화기를 사용하여 여러 에폭을 수행하고, (2) 서버는 gradient-based 서버 최적화기를 클라이언트 모델 업데이트의 평균화에 사용하여 글로벌 모델을 업데이트하는 일반적인 최적화 프레임워크를 제안한다.

### Main contributions 
In light of the above, we highlight the main contributions of the paper.
• We study a general framework for federated optimization using server and client optimizers. This framework generalizes many existing federated optimization methods, including FEDAVG.
• We use this framework to design novel, cross-device compatible, adaptive federated optimization methods, and provide convergence analysis in general nonconvex settings. To the best of our knowledge, these are the first methods for FL using adaptive server optimization. We show an important interplay between the number of local steps and the heterogeneity among clients.
• We introduce comprehensive and reproducible empirical benchmarks for comparing federated optimization methods. These benchmarks consist of seven diverse and representative FL tasks involving both image and text data, with varying amounts of heterogeneity and numbers of clients.
• We demonstrate strong empirical performance of our adaptive optimizers throughout, improving upon commonly used baselines. Our results show that our methods can be easier to tune, and highlight their utility in cross-device settings.

## 2. Federated Learning and FedAvg


## 3. Adaptive Federated Optimization
In this section, we specialize FEDOPT to settings where SERVEROPT is an adaptive optimization method (one of ADAGRAD, YOGI or ADAM) and CLIENTOPT is SGD. By using adaptive methods (which generally require maintaining state) on the server and SGD on the clients, we ensure our methods have the same communication cost as FEDAVG and work in cross-device settings.
--------------------------------------------------------
우리는 SERRVEROPT를 적응형 최적화기 방식(Adagrad, Yogi, adam) 중 하나이고, CLIENTOPT가 SGD인 설정으로 FEDOPT를 다룬다.

