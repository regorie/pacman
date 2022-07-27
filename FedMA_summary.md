2022.07.20/21

# Federated Learning with Matched Averaging
https://arxiv.org/pdf/2002.06440.pdf 2020.02.15
https://github.com/IBM/FedMA

keyword: Layer-wise


# Abstract
We propose the Federated matched averaging (FedMA) algorithm designed for federated learning of modern neural network architectures e.g. convolutional neural networks (CNNs) and LSTMs. FedMA constructs the shared global model in a layer-wise manner by matching and averaging hidden elements (i.e. channels for convolution layers; hidden states for LSTM; neurons for fully connected layers) with similar feature extraction signatures. Our experiments indicate that FedMA not only outperforms popular state-of-the-art federated learning algorithms on deep CNN and LSTM architectures trained on real world datasets, but also reduces the overall communication burden.


# 1. Introduction
...
### Our Contribution
In this work, we demonstrate how PFNM can be applied to CNNs and LSTMs, but we find that it only gives very minor improvements over weight averaging. To address this issue, we propose Federated Matched Averaging (FedMA), a new layers-wise federated learning algorithm for modern CNNs and LSTMs that appeal to Bayesian nonparametric methods to adapt to heterogeniety in the data. We show empirically that FedMA not only reduces the communcations burden, but also outperforms state-of-the-art federated learning algorithms.


# 2. Federated Matched Averaging of Neural Networks


https://mitibmwatsonailab.mit.edu/research/blog/fedma-layer-wise-federated-learning-with-the-potential-to-fight-ai-bias/

The Algorithmic Design of FedMA
The proposed FedMA algorithm uses the following layer-wise matching scheme. First, the data center gathers only the weights of the first layers from the clients and performs one-layer matching to obtain the first layer weights of the federated model. A data center then broadcasts these weights to the clients, which proceed to train all consecutive layers on their datasets, keeping the matched federated layers frozen. This procedure is then repeated up to the last layer for which we conduct a weighted averaging based on the class proportions of data points per client.
-------------------------------------
먼저, 데이터 센터는 federated model의 첫 번째 레이어의 가중치를 얻기 위해 클라이언트들의 첫 번째 layer의 가중치들만 모아 단일 계층 일치(one-layer matching)를 수행한다. 그 다음 데이터 센터는 이 가중치들을 클라이언트들에게 배포하고, 클라이언트는 그들의 데이터셋에서 모든 연속 layer를 학습하여 일치하는 federated layer를 동결시킨다.
