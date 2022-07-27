2022.07.19

# SCAFFOLD : Stochastic Controlled Averaging for Federated Learning
https://arxiv.org/pdf/1910.06378.pdf 2021.04.09

keyword : Client-drift. control variates (variance reduction) 제어 변수 (분산 감소)


## Abstract
We obtain tight convergence rates for FEDAVG and prove that it suffers from ‘client-drift’ when the data is heterogeneous (non-iid), resulting in unstable and slow convergence.

we propose a new algorithm (SCAFFOLD) which uses control variates (variance reduction) to correct for the ‘client-drift’ in its local updates. We prove that SCAFFOLD requires significantly fewer communication rounds and is not affected by data heterogeneity or client sampling. Further, we show that (for quadratics) SCAFFOLD can take advantage of similarity in the client’s data yielding even faster convergence.


## 1. Introduction
We prove that indeed such heterogeneity has a large effect on FEDAVG—it introduces a drift in the updates of each client resulting in slow and unstable convergence. Further, we show that this client-drift persists even if full batch gradients are used and all clients participate throughout the training
----------------------------------


As a solution, we propose a new Stochastic Controlled Averaging algorithm (SCAFFOLD) which tries to correct for this client-drift.

Intuitively, SCAFFOLD estimates the update direction for the server model (c) and the update direction for each client ci. The difference (c − ci) is then an estimate of the client-drift which is used to correct the local update. This strategy successfully overcomes heterogeneity and converges in significantly fewer rounds of communication.
Alternatively, one can see heterogeneity as introducing ‘client-variance’ in the updates across the different clients and SCAFFOLD then performs ‘client-variance reduction’ (Schmidt et al., 2017; Johnson & Zhang, 2013; Defazio et al., 2014). We use this viewpoint to show that SCAFFOLD is relatively unaffected by client sampling.

Finally, while accommodating heterogeneity is important, it is equally important that a method can take advantage of similarities in the client data. We prove that SCAFFOLD indeed has such a property, requiring fewer rounds of communication when the clients are more similar.

#### Contributions.
 We summarize our main results below.
• We derive tighter convergence rates for FEDAVG than previously known for convex and non-convex functions with client sampling and heterogeneous data.
• We give matching lower bounds to prove that even with no client sampling and full batch gradients, FEDAVG can be slower than SGD due to client-drift.
• We propose a new Stochastic Controlled Averaging algorithm (SCAFFOLD) which corrects for this client drift. We prove that SCAFFOLD is at least as fast as SGD and converges for arbitrarily heterogeneous data.
• We show SCAFFOLD can additionally take advantage of similarity between the clients to further reduce the communication required, proving the advantage of taking local steps over large-batch SGD for the first time.
• We prove that SCAFFOLD is relatively unaffected by the client sampling obtaining variance reduced rates, making it especially suitable for federated learning.


## 4. SCAFFOLD algorithm

#### Method
SCAFFOLD has three main steps: local updates to the client model, local updates to the client control variate, and aggregating the updates. We describe each in more detail.
-----------------------------------
SCAFFOLD는 크게 3단계로 나뉜다: 클라이언트 모델의 로컬 업데이트, 클라이언트 control variate의 로컬 업데이트, 업데이트 취합


클라이언트 모델 업데이트 : yi <- yi - nl(gi(yi) + c - ci)
              
클라이언트의 제어 변수 업데이트 : 두 가지 선택지가 있음 

...

만약 ci(클라이언트 제어변수)가 항상 0이면 SCAFFOLD는 FedAvg가 된다.