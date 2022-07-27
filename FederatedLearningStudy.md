(1주차 메모장)
# Federated Learning summary

<https://arxiv.org/pdf/1912.04977.pdf>
<https://www.youtube.com/watch?v=oWD4z4DcHXs>

Many clients collaboratively train a model under the orchestration of a central server.
Raw data is not shared (each client stores data locally)
              Data privacy
- cross-silo
- cross-device

1. Problem to solve (Optimization task)

2. Common assumptions
- IID setting
              This assumption almost never holds

- non-IID setting
              Client collects their own training dataset, and never shares

- Lipschitz gradient
- Bounded variance
- Bounded gradient

### Typical training process - in one round
1. Client selection
              Clients selected randomly
2. Broadcast
              Broadcast global model to selected clients
3. Client computation
              each loss function, SGD locally, in parallel
4. Aggregation
              Clients send local updates to server(their own model, or difference between local model and broadcasted global model), server aggregates
5. Model update
              Global model update


- centralized
              A server aggregates updates

- decentralized (peer to peer...?)
              No server
              Every device communicate with its local neighbors (weighted graph)
              Gossip averaging...?

p.26 Assumptions, methods, convergence rates...?

### Federated Averaging
Approach to solve the above problem
An adaption of local-update or parallel SGD
Each client runs some number of SGD steps locally, and then the updated local models are averaged to form the global model on the coordinating server.

pros

cons
              Client drift
              Lack of adaptive learning rate
              -> use non-collaborative optimization algorithms

              If one client slows down or fails, bottleneck, can it be dropped?

Data leakage...?

### Adaptive Federated Optimization
Server : ADAGRAD, ADAM, YOGI (FEDADAGRAD, FEDYOGI/FEDADAM)
Client : SGD

### Semi-cyclic SGD ...?
p.27
Clients can perform different local steps because of heterogeneity in their computing capacities

### Decentralized Federated Averaging

### Gossip Averaging

### Split Learning
Partition the execution of a mobel between the client and the server
minimize the distance correlation between the raw data point and communicated smashed data(outputs at the cut layer)

### Communication Compression
Communication can be a primary bottleneck
Reduces the amount of data that has to be sent over each communication link in the network by compression

CHOCO-SGD : modified gossip averaging + compression + 'communication(updates neighbor's variables)' + 'local update'
              each node have local variable and a publicaly available copy of it
              parallel

### Multi-model
Using different models for different clients

### Peronalization ...?

### Multi-task learning ...?
consider each client's local problem as a seperate task
Each client trains individual model.
Assume all clients participate in each training round
Requires stateful clients
Hard for cross-device
For cross-silo

### Security/Privacy problems

### Problems on Data - Fairness, Bias

------------------------------------------------------------------------------------------------------------

A Comprehensive Survey on Federated Learning: Concept and Applications
<https://arxiv.org/ftp/arxiv/papers/2201/2201.09384.pdf>

Decentralized Federated Averaging - Tao Sun, Dongsheng Li, and Bao Wang
<https://arxiv.org/pdf/2104.11375.pdf>

Communication Compression for Decentralized Training - Hanlin Tang, Shaoduo Gan, Ce Zhang, Tong Zhang, and Ji Liu
<https://arxiv.org/pdf/1803.06443.pdf>

Tackling the Objective Inconsistency Problem in Heterogeneous Federated Optimization - Jianyu Wang, Qinghua Liu, Hao Liang, Gauri Joshi, H. Vincent Poor
<https://arxiv.org/abs/2007.07481>

A Joint Learning and Communications Framework for Federated Learning Over Wireless Networks
<https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9210812>

Data Leakage in Federated Averaging
<https://arxiv.org/pdf/2206.12395.pdf>

TOWARDS FEDERATED LEARNING AT SCALE: SYSTEM DESIGN
<https://arxiv.org/pdf/1902.01046.pdf>

Cooperative SGD: A unified Framework for the Design and Analysis of Communication-Efficient SGD Algorithms
<https://arxiv.org/abs/1808.07576>

-------------------------------------------------------------------------------------------------------------