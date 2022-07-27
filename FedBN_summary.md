2022.07.19

# FedBN: Federated Learning on Non-IID Features via Local Batch Normalization
https://openreview.net/pdf?id=6YEQUn0QICG 2021


keyword : Batch Normalization, Feature shift


## Abstract
... In most cases, the assumption of independent and identically distributed samples across local clients does not hold for federated learning setups. Under this setting, neural network training performance may vary significantly according to the data distribution and even hurt training convergence. Most of the previous work has focused on a difference in the distribution of labels or client shifts.
------------------------------------



Unlike those settings, we address an important problem of FL ... where local clients store examples with different distributions compared to other clients, which we denote as feature shift non-iid

... we propose an effective method that uses local batch normalization to alleviate the feature shift before averaging models. The resulting scheme, called FedBN, outperforms both classical FedAvg, as well as the state-of-the-art for non-iid data (FedProx) on our extensive experiments. These empirical results are supported by a convergence analysis that shows in a simplified setting that FedBN has a faster convergence rate than FedAvg.
-----------------------------------
우리는 모델을 평균화하기 전에 feature shift를 완화하기 위해 local batch normalization을 사용하는 효과적인 방법을 제시한다. FedBN은 FedAvg와 FedProx보다 좋은 성능을 보여준다.


## 1. Introduction
A major challenge in FL is the training data statistical heterogeneity among the clients (Kairouz et al., 2019; Li et al., 2020b). It has been shown that standard federated methods such as FedAvg (McMahan et al., 2017) which are not designed particularly taking care of non-iid data significantly suffer from performance degradation or even diverge if deployed over non-iid samples (Karimireddy et al., 2019; Li et al., 2018; 2020a).
------------------------------------


... we focus on the shift in the feature space, which has not yet been explored in the literature. Specifically, we consider that local data deviates in terms of the distribution in feature space, and identify this scenario as feature shift. This type of non-iid data is a critical problem in many real-world scenarios, typically in cases where the local devices are responisble for a heterogeneity in the feature distributions
------------------------------------

Motivated by the above insight and observation, this paper proposes a novel federated learning method, called FedBN, for addressing non-iid training data which keeps the client BN layers updated locally, without communicating, and aggregating them at the server. In practice, we can simply update the non-BN layers using FedAvg, without modifying any optimization or aggregation scheme. This approach has zero parameters to tune, requires minimal additional computational resources, and can be easily applied to arbitrary neural network architectures with BN layers in FL.


## 2. Related Work


## 3. Preliminary
#### Non-IID data in FL
We introduce the concept of feature shift in federated learning as a novel category of client’s non-iid data distribution. So far, the categories of non-iid data considered according to Kairouz et al. (2019); Hsieh et al. (2019) can be described by the joint probability between features x and labels y on each client. We can rewrite Pi(x, y) as Pi(y|x)Pi(x) and Pi(x|y)Pi(y). 
We define feature shift as the case that covers: 1) covariate shift: the marginal distributions Pi(x) varies across clients, even if Pi(y|x) is the same for all client; and 2) concept shift: the conditional distribution Pi(x|y) varies across clients and P(y) is the same.
------------------------------------
우리는 FL에 클라이언트의 non-IID 데이터 분포의 새로운 카테고리로 feature shift라는 개념을 도입한다. ...
우리는 feature shift를 다음을 포함하는 경우로 정의한다: 1) 공변량 변화 (covariate shift),  2) concept shift


##### FedAvg
We establish our algorithm on FedAvg introduced by McMahan et al. (2017) which is the most popular existing and easiest to implement federated learning strategy, where clients collaboratively send updates of locally trained models to a global server.

## 4. Federated Averaging with Local Batch Normalization
### 4.1 Proposed method - FedBN
We propose an efficient and effective learning strategy denoted FedBN. Similar to FedAvg, FedBN performs local updates and averages local models. However, FedBN assumes local models have BN layers and excludes their parameters from the averaging step. We present the full algorithm in Appendix C. This simple modification results in significant empirical improvements in non-iid settings. We provide an explanation for these improvements in a simplified scenario, in which we show that FedBN improves the convergence rate under feature shift.
------------------------------------
우리는 FedBN이라는 효율적이고 효과적인 학습 방법을 제안한다. FedBN은 FedAvg와 마찬가지로 로컬 업데이트를 실행하고 로컬 모델을 평균화한다. 그러나 FedBN은 로컬 모델들이 BN layer를 가진다고 가정하고 평균화 단계에서 매개변수를 제외한다. ... 이 단순한 수정은 non-IID 환경에서 상당한 경험적 개선을 가져온다. ...
