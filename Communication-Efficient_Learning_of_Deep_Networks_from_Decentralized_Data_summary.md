2022.07.18

# Communication-Efficient Learning of Deep Networks from Decentralized Data 논문 정리
<https://arxiv.org/pdf/1602.05629v2.pdf>

## Abstract
However, this rich data is often privacy sensitive, large in quantity, or both, which may preclude logging to the data center and training there using conventional approaches.
------------------------------------------
FL의 등장 배경 설명: 모바일 기기의 데이터는 인공지능 학습에 유용하게 사용될 수 있으나 프라이버시 문제와 데이터의 방대한 양 때문에 데이터 센터를 이용한 학습에 어려움이 있음

We advocate an alternative that leaves the training data distributed on the mobile devices, and learns a shared model by aggregating locally-computed updates. We term this decentralized approach Federated Learning.
-------------------------------------------
Federated Learning 소개 : 학습 데이터를 모바일 기기에 분산된 상태로 두고, locally-computed updates를 취함하여 shared model을 학습하는 방식


## 1. Introduction
Models learned on such data hold the promise of greatly improving usability by powering more intelligent applications, but the sensitive nature of the data means there are risks and responsibilities to storing it in a centralized location.
-------------------------------------------
사용자들이 자주 소지하고 다니는 모바일 기기의 데이터로 학습한 모델은 더 나은 애플리케이션을 만들 수 있으나, 데이터의 민감함 때문에 데이터를 중앙 저장소에 저장하는 데에 위험과 책임이 따른다.

We investigate a learning technique that allows users to collectively reap the benefits of shared models trained from this rich data, without the need to centrally store it. We term our approach Federated Learning, since the learning task is solved by a loose federation of participating devices (which we refer to as clients) which are coordinated by a central server. Each client has a local training dataset which is never uploaded to the server. Instead, each client computes an update to the current global model maintained by the server, and only this update is communicated.
------------------------------------------
Federated Learning 소개 : 이 방식은 데이터를 중앙집중적으로 저장할 필요 없이 사용자들이 이 데이터를 이용하여 학습한 shared model의 이점을 얻을 수 있게 한다. Learning task는 서버가 편성한 클라이언트들의 참여로 해결된다. 클라이언트들은 서버로 업로드 되지 않는 로컬 데이터셋을 가지고 서버가 유지하는 global model의 update를 계산하여 그 결과만 공유한다.

A principal advantage of this approach is the decoupling of model training from the need for direct access to the raw training data.
------------------------------------------
이 접근법의 주요한 이점은 모델 학습과 학습 원본 데이터에 접근할 필요성을 분리시킨 데 있다. 학습 목적이 각각의 클라이언트의 데이터에 기반할 때 이 방식은 프라이버시 문제와 보안 위협을 크게 줄여준다.

Our primary contributions are 1) the identification of the problem of training on decentralized data from mobile devices as an important research direction; 2) the selection of a straightforward and practical algorithm that can be applied to this setting; and 3) an extensive empirical evaluation of the proposed approach.
... we introduce the FederatedAveraging algorithm, which combines local stochastic gradient descent (SGD) on each client with a server that performs model averaging.
------------------------------------------
주된 기여 : 1) 모바일 기기의 중앙화되지 않은 데이터를 사용한 학습의 문제 명시, 2) 이 환경에 적용할 수 있는 간단하고 실질적인 알고리즘의 선택, 3) 제안된 접근법의 실험적 평가
FederatedAveraging 알고리즘 소개: 각 클라이언트가 local SGD를 수행하고 서버가 model averaging을 수행한다.

#### Federated Learning
1) Training on real-world data from mobile devices provides a distinct advantage over training on proxy data that is generally available in the data center. 
2) This data is privacy sensitive or large in size (compared to the size of the model), so it is preferable not to log it to the data center purely for the purpose of model training (in service of the focused collection principle). 
3) For supervised tasks, labels on the data can be inferred naturally from user interaction.
------------------------------------------
FL의 이상적인 문제들은 다음과 같은 특징들을 가지고 있다.
1) 실제 세상의 데이터(real-world data)를 이용해 학습하는 것은 데이터센터에서 보통 얻을 수 있는 proxy data를 이용하는 것보다 유익하다.
2) 이 데이터는 프라이버시에 민감하거나 크기가 크므로 순전히 모델 학습만을 위해 데이터 센터에 기록하는 것은 좋지 않다.
3) 지도 학습의 경우, 레이블은 사용자와의 상호작용으로 자연스럽게 추론된다.

... we consider image classification, for example predicting which photos are most likely to be shared; and language models, which can be used to improve voice recognition and text entry on touch-screen keyboards . The potential training data for both these tasks (all the photos a user takes and everything they type ) can be privacy sensitive. The distributions from which these examples are drawn are also likely to differ substantially from easily available proxy datasets
... the labels for these problems are directly available
-----------------------------------------
윗문단의 문제 예시: _image classification_, _language models_. 이 두 task를 위한 학습 데이터는 프라이버시에 민감할 수 있고, 실 사용 데이터와 proxy 데이터가 다를 수 있다.
레이블은 사용자로부터 직접 얻을 수 있다.

#### Privacy
Federated learning has distinct privacy advantages compared to data center training on persisted data.
...  the information transmitted for federated learning is the minimal update necessary to improve a particular model
They will never contain more information than the raw training data (by the data processing inequality), and will generally contain much less. Further, the source of the updates is not needed by the aggregation algorithm, so updates can be transmitted without identifying meta-data over a mix network such as Tor (Chaum, 1981) or via a trusted third party.
We briefly discuss the possibility of combining federated learning with secure multiparty computation and differential privacy at the end of the paper.
----------------------------------------
연합학습은 data center training과 비교했을 때 분명한 프라이버시의 이점을 가지고 있다. 각각의 udpate는 원본 학습데이터만을 가지고, 일반적으로 더 적은 양의 데이터를 포함한다. 또한, 취합 알고리즘(aggregation algorithm)은 업데이트의 source를 필요로 하지 않으므로 업데이트는 meta-data를 명시하지 않고 전송될 수 있다.
FL과 secure multiparty computation, differential privacy에 대해 간단히 다룬다.

#### Federated Optimization
We refer to the optimization problem implicit in federated learning as federated optimization, drawing a connection (and contrast) to distributed optimization.
Federated optimization has several key properties that differentiate it from a typical distributed optimization problem:
• __Non-IID__ The training data on a given client is typically based on the usage of the mobile device by a particular user, and hence any particular user’s local dataset will not be representative of the population distribution.
• __Unbalanced__ Similarly, some users will make much heavier use of the service or app than others, leading to varying amounts of local training data.
• __Massively distributed__ We expect the number of clients participating in an optimization to be much larger than the average number of examples per client.
• __Limited communication__ Mobile devices are frequently offline or on slow or expensive connections
----------------------------------------
FL의 최적화 문제는 기존의 분산 최적화(distributed optimization)와 구분하기 위해 연합 최적화(federated Optimization)으로 명시한다.
FL 최적화는 일반적인 분산 최적화와 구분되는 특징이 있다.
• non-iid : 특정 클라이언트에 대한 훈련 데이터는 일반적으로 특정 사용자의 모바일 장치 사용에 기초하므로, 특정 사용자의 로컬 데이터 세트는 모집단 분포를 나타내지 않을 것이다.
• unbalanced : 일부 사용자는 다른 사용자보다 훨씬 더 많은 서비스 또는 앱을 사용하여 다양한 양의 로컬 교육 데이터로 이어질 수 있다.
• massively distributed : 최적화에 참여하는 클라이언트 수가 클라이언트 당 평균 예제 수보다 훨씬 많을 것으로 예상된다.
• limited communication : 모바일 기기는 자주 오프라인 상태이거나 느리거나 비용이 많이 드는 연결 상태에 있다.

In this work, our emphasis is on the non-IID and unbalanced properties of the optimization, as well as the critical nature of the communication constraints.
A deployed federated optimization system must also address a myriad of practical issues: client datasets that change as data is added and deleted; client availability that correlates with the local data distribution in complex ways; and clients that never respond or send corrupted updates.
----------------------------------------
이 작업은 최적화의 non-IID 및 unbalanced 특성뿐만 아니라 통신 제약의 중요한 특성에 중점을 둔다.
구축된 federated 최적화 시스템은 수많은 실제 문제를 해결해야 한다; 삭제와 추가로 인해 클라이언트의 데이터셋이 바뀌는 문제, local data의 배포와 복잡하게 연관되는 클라이언트의 가용성, 전혀 응답하지 않거나 손상된 업데이트를 전송하는 클라이언트 등

(실험 환경 설명)

These issues are beyond the scope of the current work; instead, we use a controlled environment that is suitable for experiments, but still address the key issues of client availability and unbalanced and non-IID data. We assume a synchronous update scheme that proceeds in rounds of communication. 
There is a fixed set of K clients, each with a fixed local dataset. At the beginning of each round, a random fraction C of clients is selected, and the server sends the current global algorithm state to each of these clients (e.g., the current model parameters). Each client then performs local computation based on the global state and its local dataset, and sends an update to the server. The server then applies these updates to its global state, and the process repeats.
-----------------------------------------
이러한 문제들은 현재 작업 범위을 벗어난다. 대신에 실험에 적합한 제한된 환경을 사용하지만 클라이언트 가용성, unbalanced and non-IID 데이터의 주된 문제를 다룬다. 우리는 communicaton round에서 동기화된 업데이트가 진행되는 체계를 가정한다.
FL 학습 방법 설명 : 각각 고정된 로컬 데이터셋을 가진 고정된 K 클라이언트 셋이 있다. 각 라운드의 시작에 랜덤하게 C 클라이언트가 선정되고, 서버는 현재의 global algorithm state(현재의 모델 인자 등)를 이 C 클라이언트에게 전송한다. 각각의 클라이언트는 global state와 local dataset에 기반하여 로컬 계산을 수행하고, 업데이트를 서버로 전송한다. 서버는 이 업데이트들을 global state에 반영하며, 이 과정이 반복된다.

the algorithm we consider is applicable to any finite-sum objective of the form (수식 이미지 대체하기)
min(w∈Rd)  f(w)    where    f(w) def = 1/n (sigma) n i=1 fi(w)
fi(w) = l(xi, yi; w) : the loss of the prediction on example (xi, yi) made with model parameters w
K clients, Pk the set of indexes of data point on client k, nk = |Pk|
-----------------------------------------
(연합 학습 알고리즘이 해결하려는 문제)

... in federated optimization communication costs dominate — we will typically be limited by an upload bandwidth of 1 MB/s or less.
... clients will typically only volunteer to participate in the optimization when they are charged, plugged-in, and on an unmetered wi-fi connection. Further, we expect each client will only participate in a small number of update rounds per day
-----------------------------------------
data center communication과는 다르게 fl optimization에서는 communication 비용이 가장 큰 문제이다 - 업로드 bandwidth는 1MB/s 또는 그보다 적게 제한한다.
클라이언트는 충전되어 있고, plugged-in 되어 있고, unmetered wifi 연결 시에만 최적화에 참여할 것이다. 또한 각각의 클라이언트는 하루에 적은 횟수의 업데이트 라운드에 참여할 것으로 예상한다.

On the other hand, since any single on-device dataset is small compared to the total dataset size, and modern smartphones have relatively fast processors (including GPUs), computation becomes essentially free compared to communication costs for many model types. Thus, our goal is to use additional computation in order to decrease the number of rounds of communication needed to train a model. There are two primary ways we can add computation: 
1) increased parallelism, where we use more clients working independently between each communication round; and, 
2) increased computation on each client, where rather than performing a simple computation like a gradient calculation, each client performs a more complex calculation between each communication round.
------------------------------------------
단일 디바이스의 데이터셋은 전체 데이터셋에 비해 작고, 현대 스마트폰은 상대적으로 빠른 프로세서를 가졌으므로 연산(computation)은 통신(communication) 비용에 비해 근본적으로 비용이 없다. 따라서 우리의 목표는 추가적인 연산능력을 communication round를 줄이기 위해 사용하는 데에 있다. 연산을 추가하기 위한 두 가지 주된 방법은
1) 병렬성 증가 : 각 communication round에서 클라이언트들이 독립적으로 작업
2) 각 클라이언트의 연산 증가 : 클라이언트가 단순한 미분 계산이 아니라 더 복잡한 연산을 하는 것이 있다.
두 방식 모두 연구하지만, 속도 향상은 각 2번째 방법으로 인한 것이 더 크다.


#### Related Work


## 2. The FederatedAveraging Algorithm
Thus, it is natural that we build algorithms for federated optimization by starting from SGD.
-------------------------------------------
FL 최적화를 위한 알고리즘 작성은 SGD에서 시작한다.

SGD can be applied naively to the federated optimization problem, where a single batch gradient calculation (say on a randomly selected client) is done per round of communication.
-------------------------------------------
SGD는 각 communication round에 batch gradient 계산이 이루어지는 방식으로 FL 최적화 문제에 단순하게 적용될 수 있다. 그러나 이 방식은 좋은 모델을 위해 아주 많은 round의 학습을 해야 한다. 이 baseline은 CIFAR_10 실험에서 고려한다.

In the federated setting, there is little cost in wall-clock time to involving more clients, and so for our baseline we use large-batch synchronous SGD; experiments by Chen et al. (2016) show this approach is state-of-the-art in the data center setting, where it outperforms asynchronous approaches.
To apply this approach in the federated setting, we select a C-fraction of clients on each round, and computes the gradient of the loss over all the data held by these clients. Thus, C controls the global batch size, with C = 1 corresponding to full-batch (non stochastic) gradient descent. We refer to this baseline algorithm as FederatedSGD (or FedSGD).
------------------------------------------
연합 환경에서는, 더 많은 클라이언트를 참여시키는 데 월 클럭 시간 비용이 거의 들지 않기 때문에, baseline에 대해 large-batch synchronous SGD를 사용한다. Chen 외(2016)의 실험 결과, 이 접근 방식은 데이터 센터 환경에서 최신 방식으로, 비동기 접근 방식보다 성능이 뛰어난 것으로 나타났다.
연합 설정에서 이 접근 방식을 적용하기 위해, 우리는 각 라운드에서 클라이언트의 C-분배를 선택하고, 이러한 클라이언트가 보유한 모든 데이터에 대한 손실의 기울기를 계산한다. 따라서 C는 전체 배치 크기를 제어하며, C = 1은 full-batch(비확률적) 그레이디언트 강하에 해당한다(모든 클라이언트 참여...?). 우리는 이 baseline 알고리즘을 FederatedSGD(또는 FedSGD)라고 부른다.

A typical implementation of FedSGD with C = 1 and a fixed learning rate η has each client k compute gk, the average gradient on its local data at the current model wt, and the central server aggregates these gradients and applies the update ...
That is, each client locally takes one step of gradient descent on the current model using its local data, and the server then takes a weighted average of the resulting models. Once the algorithm is written this way, we can add more computation to each client by iterating the local update multiple times before the averaging step. We term this approach FederatedAveraging (or FedAvg).
------------------------------------------
(FedAvg 설명)

The amount of computation is controlled by three key parameters: C, the fraction of clients that perform computation on each round; E, then number of training passes each client makes over its local dataset on each round; and B, the local minibatch size used for the client updates.
------------------------------------------
연산량은 3개의 매게변수로 조절된다. C: 각 round에서 연산을 수행하는 client, E: 각 라운드에서 각 클라이언트가 로컬 데이터 세트에 만드는 훈련 패스 수(epoch), B: 클라이언트 업데이트에 사용된 local minibatch size(batch)

We write B = ∞ to indicate that the full local dataset is treated as a single minibatch. Thus, at one endpoint of this algorithm family, we can take B = ∞ and E = 1 which corresponds exactly to FedSGD.
-----------------------------------------
전체 로컬 데이터 셋이 단일 minibatch로 처리됨을 나타내기 위해 B = ∞ 라고 쓴다. 따라서 이 알고리즘 패밀리의 한 끝점에서 FedSGD에 정확히 해당하는 B = ∞ 및 E = 1을 취할 수 있다. (전체 데이터가 1 배치, 1 에폭)

For general non-convex objectives, averaging models in parameter space could produce an arbitrarily bad model.
-----------------------------------------
일반적인 non-convex 목적함수의 경우 parameter space에서 모델을 평균화하는 것은 불량한 모델을 생성할 수 있다.

Recent work indicates that in practice, the loss surfaces of sufficiently over-parameterized NNs are surprisingly well behaved and in particular less prone to bad local minima than previously thought (Dauphin et al., 2014; Goodfellow et al., 2015; Choromanska et al., 2015). And indeed, when we start two models from the same random initialization and then again train each independently on a different subset of the data (as described above), we find that naive parameter averaging works surprisingly well (Figure 1, right): the average of these two models, (1/2)w + (1/2)w', achieves significantly lower loss on the full MNIST training set than the best model achieved by training on either of the small datasets independently. While Figure 1 starts from a random initialization, note a shared starting model wt is used for each round of FedAvg, and so the same intuition applies.
-----------------------------------------
최근의 연구는 실제로 충분히 과도하게 매개 변수화된 NN의 손실 표면은 놀랍게도 잘 작동하고 있으며, 특히 이전에 생각했던 것보다 나쁜 국소 최소값의 경향이 덜하다는 것을 보여준다.
(비교) ...?

The success of dropout training also provides some intuition for the success of our model averaging scheme; dropout training can be interpreted as averaging models of different architectures which share parameters, and the inference time scaling of the model parameters is analogous to the model averaging used in FedAvg (Srivastava et al., 2014)
-----------------------------------------
드롭아웃 훈련의 성공은 또한 모델 평균화 계획의 성공에 대한 약간의 직관을 제공한다. 드롭아웃 훈련은 매개 변수를 공유하는 다른 아키텍처의 평균 모델로 해석될 수 있으며, 모델 매개 변수의 추론 시간 스케일링은 FedAvg에서 사용되는 모델 평균화와 유사하다. ...?몰?루


## 3. Experimental Results

## 4. Conclusions and Future Work