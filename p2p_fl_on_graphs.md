2022.07.27

# Peer-to-Peer Federated Learning on Graphs
https://arxiv.org/pdf/1901.11173.pdf

keywords:

## Abstract
We consider the problem of training a machine learning model over a network of nodes in a fully decentralized framework. 
The nodes take a Bayesian-like approach via the introduction of a belief over the model parameter space. 
We propose a distributed learning algorithm in which nodes update their belief by judicially aggregating information from their local observational data with the model of their one-hop neighbors to collectively learn a model that best fits the observations over the entire network. 
Our algorithm generalizes the prior work on federated learning. 
Furthermore, we obtain theoretical guarantee (upper bounds) that the probability of error and true risk are both small for every node in the network. 
We specialize our framework to two practically relevant problems of linear regression and the training of Deep Neural Networks (DNNs).
--------------------------------------
우리는 완전히 분산된 프레임워크에서 노드 네트워크를 통해 머신 러닝 모델을 훈련하는 문제를 고려한다.
노드들은 모델 매개변수 공간에 대한 믿음의 도입을 통해 베이지안처럼 접근한다.
우리는 노드가 전체 네트워크에서의 관찰에 가장 적합한 모델을 집합적으로 학습하기 위해 로컬 관찰 데이터와 one-hop 이웃들의 모델을 사법적으로 집계하여 자신의 belief를 업데이트하는 분산 학습 알고리즘을 제안한다.
우리의 알고리즘은 연합학습에 대한 이전의 연구를 일반화한다.
또한 우리는 네트워크의 모든 노드에 대해 오류 가능성과 실제 위험도 모두 적다는 이론적인 보증(상한)을 얻는다.
우리는 우리의 프레임워크를 두 개의 실질적으로 관련된 문제인 선형 회귀와 심층 신경망(DNNs) 훈련에 특화한다.


## 1. Introduction
Mobile computing devices have seen a rapid increase in their computational power as well as storage capacity. 
Aided by this increased computational power and abundance of data, as well as due to privacy and security concerns, there is a growing trend towards training machine learning models cooperatively over networks of such devices using only local training data. 
The field of Federated learning initiated by McMahan et al. (2017) and Konecnˇ y et al. (2016) considers the problem of learning a centralized model based on private training data of a number of nodes. 
More specifically, this framework is characterized by a possibly large number of decentralized nodes which are (i) connected to a centralized server and (ii) have access to only local training data possibly correlated across the network. 
It is also assumed that communications between the nodes and the central server incur large costs.
McMahan et al. (2017) proposed the federated optimization algorithm in which the central server randomly selects a fraction of the nodes in each round, shares the current global model with them, and then averages the updated models sent back to the server by the selected nodes.
McMahan et al. (2017) and Konecnˇ y` et al. (2016) also provided experimental results with good accuracy using both convolutional and recurrent neural networks while reducing the communication costs.
-----------------------------------------
연합학습 분야: 모바일 장치의 저장용량 뿐만 아니라 계산 능력도 빠르게 증가하고, 개인정보 보호 문제로 인해 로컬 훈련 데이터만 사용하여 이런한 장치의 네트워크를 통해 기계 학습 모델을 협력적으로 훈련하는 경향이 증가하고 있다. 
McMahan 외(2017)와 Konecnˇy 외(2016)에 의해 시작된 연합 학습 분야는 다수의 노드의 개인 훈련 데이터를 기반으로 중앙 집중식 모델을 학습하는 문제를 고려한다.
구체적으로, 이 모델은 (i)중앙 서버에 연결되고 (ii)네트워크를 통해 연관성 있는 로컬 훈련 데이터에만 접근할 수 있는 많은 수의 분산 노드를 특징으로 한다.
또한 노드들과 중앙 서버의 통신은 많은 비용이 소요된다고 가정된다.
McMahan 등(2017)은 중앙 서버가 각 라운드에서 무작위로 노드의 일부를 선택하고 현재 전역 모델을 공유한 다음, 선택한 노드에 의해 서버로 다시 전송된 업데이트된 모델을 평균하는 연합 최적화 알고리듬을 제안했다.
McMahan 외(2017)와 Konecnˇ y' 외(2016)는 또한 통신 비용을 절감하면서 컨볼루션 및 반복 신경망을 모두 사용하여 우수한 정확도의 실험 결과를 제공했다.


This work generalizes the model and the framework of federated learning framework of McMahan et al. (2017) in the following important directions. 
----------------------------------------
이 연구는 McMahan등(2017)의 연합학습 모델과 프레임워크를 다음과 같은 중요한 방향으로 일반화한다.


Conceptually our contributions are as follows:
- Fully Decentralized Framework : 
We do not require a centralized location where all the training data is collected or a centralized controller to maintain a global model over the network by aggregating information from all the nodes. 
Instead, in our setting, nodes are distributed over a network/graph where they only communicate with their one-hop neighbors. 
Hence, our problem formulation does away with the need of having a centralized controller.
- Localized Data :
We allow the training data available to an individual node to be insufficient for learning the shared global model.
In other words, the nodes must collaborate with their next hop neighbors to learn the optimal model even though for privacy concerns, nodes do not share their raw training data with the neighbors.
----------------------------------------
개념적으로 우리의 기여는 다음과 같다:
- 완전히 분산된 프레임워크: 우리는 훈련 데이터가 수집되거나 모든 노드들로부터 정보를 취합하여 글로벌 모델을 유지하는 중앙 컨트롤러가 필요하지 않다. 대신에, 우리의 환경에서는, 노드들은 네트워크/그래프 상에 분산되어 one-hop 이웃과만 통신한다.
따라서, 우리의 문제 공식화는 중앙 컨트롤러를 가질 필요성을 없앤다.
- 지역화된 데이터 :
우리는 개별 노드에서 사용할 수 있는 훈련 데이터가 공유 글로벌 모델을 학습하는 데 충분하지 않도록 한다.
다시 말해, 프라이버시로 인한 문제로 이웃들과 원시 데이터를 공유하지 않더라도, 노드들은 최적의 모델을 학습하기 위해 next hop 이웃들과 협력해야 한다.


To motivate our work and underline our contributions, consider the following simple toy example.
----------------------------------------


Example 1 (Distributed Linear Regression)
...
Our fully decentralized federated learning, when specialized to this regression example, provides an information exchange rule which, despite the generality of the graph and the deficiency of the local observations, result in each node eventually learning the true parameter θ∗.
Our theoretical contributions are as follows:
- Mathematically, we pose the problem of federated machine learning as a special case of the problem of social learning on a graph. 
Social learning on a graph has long been studied in statistics, economics, and operations research and encompasses canonical problems of consensus DeGroot (1974), belief propagation (Olfati-Saber et al., 2005), and distributed hypothesis testing (Jadbabaie et al., 2013; Nedic et al., 2015; Shahrampour ´ et al., 2016; Lalitha et al., 2018). 
To the best of our knowledge, our proposed formulation is the first to make this connection, allowing for the application of a gamut of statistical tools from social learning in the context of federated learning.
- In particular, borrowing from (Nedic et al., 2015; ´ Shahrampour et al., 2016; Lalitha et al., 2018), we propose a peer-to-peer social learning scheme where the nodes take a Bayesian-like approach via the introduction of a belief over a parameter space characterizing the unknown global (underlying) model. 
Fully decentralized learning of the global (underlying) model is then achieved via a two step procedure. 
First, each node updates its local belief according to a Bayesian inference step (posterior update) based on the node’s local data. 
This step is, then, followed by a consensus step of aggregating information from the one-hop neighbors.
----------------------------------------
이 회귀 예제에 특화된 우리의 완전 분산 학습은 그래프의 일반성과 로컬 관측치의 부족함에도 불구하고 각 노드가 결국 진정한 매개변수  θ∗를 학습하게 하는 정보 교환 규칙을 제공한다.
우리의 이론적인 기여는 다음과 같다:
- 수학적으로, 우리는 연합 기계 학습 문제를 그래프에서의 사회학습 문제의 특별한 사례로 제시한다.
그래프에 대한 사회적 학습은 통계, 경제 및 운영 연구에서 오랫동안 연구되어 왔으며 합의 DeGroot, belief propagation, 분산 가설 테스트의 표준 문제를 포함한다.
우리가 아는 한, 제안된 공식은 연합 학습의 맥락에서 사회 학습에서 얻은 통계 도구의 전반을 적용할 수 있도록 하는 첫 번째 연결이다.
- 특히, (...)에서 차용하여 노드가 알려지지 않은 글로벌(기본) 모델을 특징짓는 매개 변수 공간에 대한 belief의 도입을 통해 Bayesion같은 접근 방식을 차용하는 peer-to-peer 소셜 학습 체계를 제안한다.
그 다음 2단계 절차를 통해 글로벌 모델의 완전한 분산 학습이 달성된다.
먼저, 각 노드는 노드의 로컬 데이터를 기반으로 베이지안 추론 단계(사후 업데이트)에 따라 로컬 belief를 업데이트한다.
다음 단계는 one-hop 이웃의 정보를 집계하는 합의(consensus) 단계이다.
- 네트워크의 네트워크 연결성과 글로벌 학습 가능성에 대한 가벼운 제약 하에서, 우리는 노드가 각각 네트워크에서 샘플에 가장 잘 맞는 글로벌 최적 모델을 학습할 수 있도록 필요한 훈련 샘플 수에 대한 높은 확률 보증을 제공한다.


Empirically, we validate our theoretical framework in two specific, yet canonical, linear and non-linear machine learning problems: linear regression and training of deep neural network (DNN).
Our proposed social learning algorithm and its theoretical analysis rely on a local Bayesian posterior update, which in most practically relevant applications such as training of DNNs turn out to be computationally intractable. 
To overcome this, we employ variational inference (VI) (Gal, 2016, Chapter 3) techniques which replace the Bayesian modelling marginalization with optimization. 
Our experiments on a network of two nodes cooperatively training a shared DNN show that fully decentralized federated learning can be done with little to no drop in accuracy relative to a central node with access to all the training data.
------------------------------------
경험적으로, 우리는 선형 회귀와 심층 신경망이라는 두 가지 구체적이지만 표준적인 선형 및 비선형적인 기계학습 문제에서 우리의 이론적 프레임워크를 검증한다.
우리의 사회 학습 알고리즘과 이론적인 분석은 로컬 베이지안 사후 업데이트에 의존하며, 이는 DNN 훈련과 같은 대부분의 실제 관련된 어플리케이션에서 계산적으로 다루기 어려운 것으로 밝혀졌다.
이를 극복하기 위해, 우리는 베이지안 모델링 주변화(Bayesian modelling marginalization)를 최적화로 대체하는 variational inference(VI) 기법을 차용하였다.
공유된 DNN을 공동으로 훈련하는 두 개의 노드로 이루어진 네트워트에 대한 우리의 실험은 완전히 분산된 연합학습이 모든 훈련 데이터에 접근할 수 있는 중앙 노드에 비해 정확도의 차이가 작거나 없이 수행될 수 있음을 보여준다.


### Notation
...


## 2. Problem Setup
In this section, we formally describe the label generation model at each node, the communication graph, and a criterion for successful learning over the network.
---------------------------------------
이 섹션에서는 각 노드의 레이블 생성 모델, 통신 그래프, 네트워크를 통한 성공적인 학습을 위한 기준(criterion)을 공식적으로 설명한다.


### 2.1 The Model

### 2.2 The Communication Network

### 2.3 The Learning Criterion


## 3. Peer-to-peer Federated Learning Algorithm