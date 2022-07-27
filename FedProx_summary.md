2022.07.19

# FEDERATED OPTIMIZATION IN HETEROGENEOUS NETWORKS
https://arxiv.org/pdf/1812.06127.pdf 2020.04.21

keyword: FedProx - proximal term / capable of handling heterogeneous federated enviornments while maintaining similar privacy and computational benefits
         systems heterogeneity, statistical heterogeneity

## Abstract
Federated Learning is a distributed learning paradigm with two key challenges that differentiate it from traditional distributed optimization: (1) significant variability in terms of the systems characteristics on each device in the network (systems heterogeneity), and (2) non-identically distributed data across the network (statistical heterogeneity).
---------------------------------------
FL은 기존의 분산 최적화와 구분되는 두 가지 핵심 과제를 가지고 있다. (1) 네트워크의 각 장치의 시스템적 자양성(시스템적 이질성), (2) non-IID 데이터(통계적 이질성)

In this work, we introduce a framework, FedProx, to tackle heterogeneity in federated networks. FedProx can be viewed as a generalization and re-parametrization of FedAvg, the current state-of-the-art method for federated learning.
---------------------------------------
우리는 연합 네트워크의 이질성을 해결하기 위한 프레임워크 FedProx를 제안한다. FedProx는 FedAvg의 일반화 및 re-parametrization으로 볼 수 있다.

While this re-parameterization makes only minor modifications to the method itself, these modifications have important ramifications both in theory and in practice. Theoretically, we provide convergence guarantees for our framework when learning over data from non-identical distributions (statistical heterogeneity), and while adhering to device-level systems constraints by allowing each participating device to perform a variable amount of work (systems heterogeneity).
---------------------------------------
이 re-parametrization은 방법 자체에 사소한 수정만 하지만 이론적으로, 실질적으로 중요한 영향을 미친다. 이론적으로 우리는 non-IID 데이터를 학습할 때, 참여하는 기기가 가변적인 양의 작업을 수행할 수 있도록 하여 device-level의 제약조건에 적용하면서 우리의 프레임워크가 수렴함을 보증한다.

Practically, we demonstrate that FedProx allows for more robust convergence than FedAvg across a suite of realistic federated datasets. In particular, in highly heterogeneous settings, FedProx demonstrates significantly more stable and accurate convergence behavior relative to FedAvg—improving absolute test accuracy by 22% on average.
---------------------------------------
실제로 우리는 FedProx가 현실적인 연합 학습 데이터셋에서 FedAvg보다 더 확실하게 수렴함을 보여준다. 매우 이질적인 데이터 환경에서, FedProx는 FedAvg보다 훨씬 안정적이고 정확하여 평균적으로 22% 더 높은 정확도를 보인다.


## 1. Introduction
...
In this work, we propose FedProx, a federated optimization algorithm that addresses the challenges of heterogeneity both theoretically and empirically. A key insight we have in developing FedProx is that an interplay exists between systems and statistical heterogeneity in federated learning. Indeed, both dropping stragglers (as in FedAvg) or naively incorporating partial information from stragglers (as in FedProx with the proximal term set to 0) implicitly increases statistical heterogeneity and can adversely impact convergence behavior. To mitigate this issue, we propose adding a proximal term to the objective that helps to improve the stability of the method. This term provides a principled way for the server to account for heterogeneity associated with partial information. Theoretically, these modifications allow us to provide convergence guarantees for our method and to analyze the effect of heterogeneity. Empirically, we demonstrate that the modifications improve the stability and overall accuracy of federated learning in heterogeneous networks—improving the absolute testing accuracy by 22% on average in highly heterogeneous settings.
---------------------------------------
본 연구에서는 이론적으로나 경험적으로나 이질성의 과제를 해결하는 연합 최적화 알고리즘인 FedProx를 제안한다. ... 핵심적인 통찰은 연합학습에서 시스템과 통계적 이질성 사이에 상호작용이 존재한다는 것이다. 실제로 (FedAvg와 같이) straggler를 드롭하는 것과 (FedProx에서 proximal term이 0으로 설정된 것과 같이) straggler의 부분정보를 단순하게 포함하는 것은 통계적 이질성을 증가시키고 수렴 행동에 악영향을 미칠 수 있다. 이 문제를 완화하기 위해 method의 안정성을 향상시키도록 우리는 근위 항(proximal term)을 목적에 추가할 것을 제안한다. 이 항은 서버가 부분적 정보와 관련된 이질성을 처리할 수 있는 원칙적인 방법을 제공한다. 이론적으로, 이 수정은 우리의 method의 수렴을 보장하고 이질성이 미치는 영향을 분석할 수 있게 한다. 경험적으로 우리는 이 수정이 이질적인 네트워트에서의 연합학습의 안정성과 전반적인 정확도를 높임을 보여준다. - 매우 이질적인 환경에서 테스트 정확도가 평균적으로 22% 향상
...


## 2. Background and Related Work


## 3. Federated Optimization : Methods
### 3.2 Proposed Framework : FedProx
Our proposed framework, FedProx (Algorithm 2), is similar to FedAvg in that a subset of devices are selected at each round, local updates are performed, and these updates are then averaged to form a global update. However, FedProx makes the following simple yet critical modifications, which result in significant empirical improvements and also allow us to provide convergence guarantees for the method.
----------------------------------------
우리가 제안한 프레임워크 FedProx는 FedAvg와 비슷하다 - 각 라운드에서 장치들의 하위 집합이 선택되고, 로컬 업데이트가 진행되며, 이 업데이트가 취합되어 글로벌 업데이트를 형성한다. 그러나 FedProx는 단순하지만 중요한 수정을 가하여 ...

##### Tolerating partial work
... it is unrealistic to force each device to perform a uniform amount of work (i.e., running the same number of local epochs, E), as in FedAvg. In FedProx, we generalize FedAvg by allowing for variable amounts of work to be performed locally across devices based on their available systems resources, and then aggregate the partial solutions sent from the stragglers (as compared to dropping these devices). 
... instead of assuming a uniform γ for all devices throughout the training process, FedProx implicitly accommodates variable γ’s for different devices and at different iterations.
----------------------------------------
FedAvg처럼 각각의 장치가 동일한 양의 일을 하도록 하는 것은 비현실적이다. FedProx에서는, FedAvg를 일반화하여 장치들이 시스템 리소스에 기반하여 가변적인 양의 일을 하도록 허용하고, straggler들이 보낸 부분적인 solution을 취합한다(그저 드롭하는 것과 다르게)
FedProx는 학습 프로세스 전반에 걸쳐 모든 장치로부터 균일한 γ를 가정하는 대신, 암묵적으로 다른 장치와 다른 반복 회차에서 변수 γ를 수용한다.

##### Proximal term
while tolerating nonuniform amounts of work to be performed across devices can help alleviate negative impacts of systems heterogeneity, too many local updates may still (potentially) cause the methods to diverge due to the underlying heterogeneous data.
We propose to add a proximal term to the local subproblem to effectively limit the impact of variable local updates. In particular, instead of just minimizing the local function Fk(·), device k uses its local solver of choice to approximately minimize the following objective hk :
----------------------------------------
장치 간에 불균일한 양의 일을 수용하는 것은 시스템 이질성의 악영향을 완화할 수 있지만, 너무 많은 로컬 업데이트는 여전히 이질적인 데이터로 인해 method가 분산되도록 할 수 있다.
우리는 근위 항(proximal term)을 로컬 subproblem(objective function)에 추가할 것을 제시하여 가변적인 로컬 업데이트의 영향을 제한한다.

The proximal term is beneficial in two aspects: (1) It addresses the issue of statistical heterogeneity by restricting the local updates to be closer to the initial (global) model without any need to manually set the number of local epochs. (2) It allows for safely incorporating variable amounts of local work resulting from systems heterogeneity.
------------------------------------------
근위 항은 두 가지 측면에서 이점이 있다. (1) 로컬 에폭의 수를 수동으로 설정할 필요 없이 로컬 업데이트를 초기의(global) 모델에 가깝도록 제한하여 통계적 이질성 문제를 해결한다. (2) 시스템 이질성으로 인한 가변적인 양의 로컬 작업을 안전하게 통합할 수 있다.


## 4. FedProx : Convergence Analysis
### 4.2 FedProx Analysis


## 5. Experiments
### 5.3 Statistical Heterogeneity : Proximal Term

##### 5.3.1 Effects of Statistical Heterogeneity


## 6. Conclusion