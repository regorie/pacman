2022.07.20

# FedDC: Federated Learning with Non-IID Data via Local Drift Decoupling and Correction
https://arxiv.org/pdf/2203.11751v1.pdf

keyword : local drift, local druft variable

## Abstract


## 1. Introduction


## 2. Related Work


## 3. Local Drift in Federated Learning
... local drift(client drift) can lead to skewed global model

Therefore, we can learn the local drift between the global model and the local model, and bridge the local drift before uploading the local model parameters to the server
-----------------------------------------
우리는 global model과 local model의 local drift를 배우고, local model의 매개변수를 server에 업로드 하기 전에 local drift를 bridge할 수 있다.

## 4. Proposed Method
Based on the above observation, we propose a novel federated learning algorithm with local drift decoupling and correction (FedDC), which aims to improve the robustness and speed of model convergence by learning the model drift and bridging the drift on the client-side.
Our FedDC introduces lightweight modifications in the training phase to decouple the global model from clients’ local models using the local drift. Specifically, in the local training phase, each client learns a local drift variable that represents the gap between its local model and the global model. Then, the local drift variable is used to correct the local model parameters before the parameter aggregating phase. In this way, FedDC decreases the distance between the local model parameters and the global model parameters, which also decreases the negative influence of the skewed local model on the global model.
---------------------------------------------
위의 관찰을 바탕으로, 우리는 모델 드리프트를 학습하고 클라이언트 측에서 드리프트를 브리징하여 모델 수렴의 견고성과 속도를 향상시키는 것을 목표로 하는 로컬 드리프트 디커플링 및 보정(FedDC)을 갖춘 새로운 연합 학습 알고리듬을 제안한다.
FedDC는 로컬 드리프트를 사용하여 global model과 클라이언트의 local model을 분리하기 위해 학습 단계에서 가벼운 수정을 가한다. 특히, local 학습 단계에서 각각의 클라이언트는 로컬 드리프트 변수(local model과 global model의 격차를 나타냄)를 학습한다. 로컬 드리프트 변수는 매개변수 취합 단계 이전에 로컬 모델의 매개변수를 수정하는 데에 사용된다. 이 방법으로, FedDC는 로컬 매개변수와 글로벌 매개변수 사이의 격차를 줄여 편향된 로컬 모델이 글로벌 모델에 주는 악영향을 줄여준다.

### Objectives in FedDC
