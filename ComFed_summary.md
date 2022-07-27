2022.07.20/21

# Federated Learning for Non-IID Data via Client Variance Reduction and Adaptive Server Update
https://arxiv.org/pdf/2207.08391.pdf

keywords : FedProx + Scaffold + FedNova

# Abstract


# 1. Introduction

### 3. Baseline Algorithm
##### A. FedAvg

##### B. FedProx
FedProx improves FedAvg by modifying the local objective function. It adds an l2-regularization on the distance between the global model learned in the previous round and the current local model. Instead of just minimizing the local loss function fi , client i minimizes the dissimilarity between its local model wi and the global model ...
-----------------------------
FedProx는 로컬 objevtive function을 수정하여 FedAvg를 개선한다. 이전 라운드에서 학습한 글로벌 모델과 현재의 로컬 모델 사이의 거리에 L2-정규화를 적용한다. 단지 로컬 loss-function을 최소화하는 대신에 클라이언트 i는 로컬모델 wi와 글로벌 모델의 차이를 최소화한다.

The role of this proximal term is to pull local models towards the global model, and as a result, the divergence among clients reduces.
---------------------------
근위 항의 역할은 로컬 모델을 글로벌 모델로 끌어당김으로써 클라이언트 사이의 격차를 줄이는 것이다.

##### C. Scaffold
Scaffold uses control variates c, ci to estimate the model update direction of the server and client i. It proposes two methods for updating ci and uses the average rule for aggregating c: ...
-----------------------------
Scaffold는 변수 c, ci를 이용하여 서버와 클라이언트의 모델 업데이트 방향을 추정한다. Ci를 업데이트하는 두 가지 방법이 있고, c를 취합하는 average rule을 사용한다. :...

Control variates are exchanged between the clients and server along with model weights (Algorithm 1, lines 3 and 10) and maintained across rounds. The difference between the two update directions, c − ci , evaluates the client drift and is used to correct the local update as follows: ...
--------------------------------------
제어 변수는 모델 가중치와 함께 서버와 클라이언트 간에 교환되고, 라운드에 걸쳐 유지된다. 두 업데이트 방향의 차이, c - ci 는 client-drift를 측정하고 로컬 업데이트를 수정하기 위해 다음과 같이 사용된다. : ...

The correction term c − ci ensures that the local and global models are updated in close directions to reduce client drift. Compared to FedAvg, Scaffold doubles the computational and communication cost due to the maintenance of control variates across rounds.
----------------------------
correction term c-ci는 로컬 모델과 글로벌 모델이 client-drift를 줄이기 위해 로컬 모델과 글로벌 모델이 가까운 방향으로 업데이트 되도록 보장한다. FedAvg와 비교했을 때, Scaffold는 제어 변수를 라운드에 걸쳐 유지하기 위해 연산량과 통신 비용을 두 배로 필요로 한다.

##### D. FedNova
FedNova modifies FedAvg by using a normalized aggregation instead of the simple averaging aggregation. It considers that clients can perform different numbers of local updates, employ different local optimizers and learn at different learning rates, resulting in heterogeneous local progress. Clients with larger local updates will significantly impact the global update. To avoid a bias in the global update, FedNova normalizes then re-scales the accumulated local update ∆i before averaging: ...
------------------------------
FedNova는 단순한 평균화 aggregation 대신 정규화된 aggregation을 사용하는 것으로 FedAvg를 수정한다. 클라이언트가 다른 횟수의 로컬 업데이트를 수행할 수 있으며, 다른 로컬 최적화기를 차용하고, 다른 학습률로 학습하여 다른 로컬 진행률을 보일 수 있음을 고려한다. 더 큰 로컬 업데이트를 하는 클라이언트는 글로벌 업데이트에 상당한 영향을 준다. 이러한 글로벌 업데이트의 편향을 피하기 위해서, FedNova는 다음과 같이 평균화하기 전에 누적된 로컬 업데이트를 정규화(normalize)하고 re-scale한다. : ...

##### E. FedAdam, FedAdagrad, FedYogi



### 4. Proposed Arrproach
... ComFed uses client-variance reduction techniques to reduce the gap among clients, making server model aggregation easier. Simultaneously, ComFed applies server-side adaptive update techniques to dampen oscillations, help the global gradient vector point to the right direction, and take more straightforward paths to the global optimum.
--------------------------
ComFed는 클라이언트-분산 감소 기술을 사용하여 클라이언트 간의 격차를 줄임으로써 서버 모델 집계를 더 쉽게 한다. 동시에, ComFed는 서버 측 적응형 업데이트 기술을 적용하여 진동을 감쇠시키고, 전역 그레이디언트 벡터가 올바른 방향을 가리키도록 도우며, 전역 최적화에 대한 보다 간단한 경로를 취한다.

Unlikely state-of-the-art algorithms, ComFed enhances the whole training process on both the client and server sides. Intuitively, ComFed can benefit from the robustness of both kinds of techniques against Non-IID data distributions.
----------------------------
ComFed는 클라이언트와 서버 양측의 훈련 프로세스를 향상시킨다. 직관적으로, ComFed는 non-IID 데이터 분포에 대한 두 종류의 기술의 견고함으로부터 이익을 얻을 수 있다.

We consider three client-variance reduction techniques used in FedProx, Scaffold, and Fedorova. They are to regularize local objectives by a proximal term (briefly called Prox), correct local updates with control variates (called Scaf), and normalize local updates (called Nova). Prox, Scaf, and Nova techniques adjust three steps: mini-batch gradient calculation, local update, and aggregation, respectively.
---------------------------
우리는 FedProx, SCAFFOLD, FedNova에 사용되는 클라이언트 분산 감소 기술을 고려한다. 이들을 로컬 objective를 근위 항을 이용해 정규화하고(Prox), 제어변수를 통해 로컬 업데이트를 수정하고(Scaf), 로컬 업데이트를 정규화한다(Nova). Prox, Scaf, Nova는 각각 세 단계를 조정한다 : mini-batch gradient 계산, 로컬 업데이트, 취합 

To simplify the definition of our algorithms, we group these three steps into a stage. Each learning mechanism associated with this stage, denoted by optc, specifies how to calculate mini-batch gradients, update local models, and aggregate local changes (see Table II for detail).
------------------------------
알고리즘의 정의를 단순화하기 위해 이 세 과정을 단계로 그룹화한다. 이 단계와 관련된 각각의 학습 메커니즘은 mini-batch gradient를 계산하고, 로컬 모델을 업데이트하고, 로컬 변화를 집계하는 방법을 정한다.

On the server side, we consider three adaptive optimizers, Adam, Adagrad, and Yogi, for updating the global model. We develop 9 versions of ComFed corresponding to 9 different combinations between the above client-variance reduction mechanisms and adaptive server optimizers. Table III shows the breakdown of FL algorithms, including 7 state-of-the-art algorithms and 9 ComFed variations. It demonstrates which technique to apply for the client and server sides.
----------------------------------
서버 측에서는, 글로벌 모델을 업데이트하기 위해 3개의 적응형 최적화기 Adam, Adagrad, Yogi를 고려한다. 우리는 클라이언트 분산 감소 메커니즘과 적응형 서버 최적화기의 9개의 조합에 해당하는 9개 버전을 개발한다.


### 5. Experiments
