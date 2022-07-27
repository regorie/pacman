(1주차 메모장)
# Flower Framework

2022.07.14

## Quickstart PyTorch
<https://flower.dev/docs/quickstart-pytorch.html>

## PyTorch project
<https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html>

## Train a CNN 
<https://flower.dev/blog/2021-02-24-pytorch-from-centralized-to-federated/>
<https://github.com/adap/flower/tree/main/examples/pytorch_from_centralized_to_federated>
Uses cntralized PyTorch setup as a base to build a federated version

Need definitions:
1. The model itself
2. The data, and how to load the data
3. How to train the model
              train loader
              optimizer
              schedular
              epochs
              device ...
4. How to test the model

#### Client
Client stores CNN, training & test set dataloader as instance variables

1. methods
              - get_parameters
                            locally updated model parameters are returned back to the server
              - set_parameters
                            after recieving CNN model weights from the server, set_parameters() is called to update local model
              - fit
                            recieves global model weights from the server, sets parameters(set_parameters), trains local model(train), and returns updated local parameters to the server(get_parameters)
              - evaluate
                            similar to fit, calculates loss and accuracy

_quickstart pytorch_
```
class CifarClient(fl.client.NumPyClient):
    def get_parameters(self):
        return [val.cpu().numpy() for _, val in net.state_dict().items()]

    def set_parameters(self, parameters):
        params_dict = zip(net.state_dict().keys(), parameters)
        state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
        net.load_state_dict(state_dict, strict=True)

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        train(net, trainloader, epochs=1)
        return self.get_parameters(), num_examples["trainset"], {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        loss, accuracy = test(net, testloader)
        return float(loss), num_examples["testset"], {"accuracy": float(accuracy)}
```

#### Server

1. 
- num_rounds

2. Writing flexible server
- minimum number of clients 
- evalutation can be centralized by passing eval function to strategy
- 

_quickstart pytorch_
```
import flwr as fl

fl.server.start_server(config={"num_rounds": 3})
```

_server.py_
```
from typing import List, Tuple

import flwr as fl
from flwr.common import Metrics


# Define metric aggregation function
def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    # Multiply accuracy of each client by number of examples used
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]

    # Aggregate and return custom metric (weighted average)
    return {"accuracy": sum(accuracies) / sum(examples)}


# Define strategy
strategy = fl.server.strategy.FedAvg(evaluate_metrics_aggregation_fn=weighted_average)

# Start Flower server
fl.server.start_server(
    server_address="[::]:8080",
    config={"num_rounds": 3},
    strategy=strategy,
)
```

------------------------------------------------------------------

1. optimizer
2. scheduler...?

## API reference - flwr
<https://flower.dev/docs/apiref-flwr.html#>

#### Client

1. class flwr.client.Client : Abstract base class
              - abstract evaluate(ins: EvaluateIns) -> EvaluateRes
                            Evaluate the provided weights using the locally held dataset

                            - EvaluateIns : evaluation instructions containing global model parameters and a dictionary of configuration values
                            - EvaluateRes : the loss on the local dataset and other details such as number of local data examples used for evaluation

              - abstract fit(ins: FitIns) -> FitRes
                            Refine the provided weights using local dataset

                            - FitIns : training instructions containing global model parameters and a dictionary of configuration values
                            - FitRes : training results containing updated parameters and other details such as the number of local training examples used for training                          

              - abstract get_parameters(ins: GetParametersIns) -> GetParametersRes
                            Return the current local model parameters

                            - GetParametersIns : get parameters instructions recieved from the server containing a dictionary of configuration values

              get_properties(ins: GetPropertiesIns) -> GetPropertiesRes
                            Return set of client's properties

                            - GetPropertiesIns : get properties instructions containing a dictionary of configuration values

flwr.client.start_client(
              server_address: str, ( [ ::]:8080)
              client: Client,
              grpc_max_message_length: int = ..., ( default is 526870912, 512MB )
              root_certificates: Optional[ bytes] = ... ( default is None)
              )


2. class flwr.client.NumPyClient : Abstract base class for clients using Numpy
              - abstract evaluate(parameters: List[ ndarray], config: Dict[str, Union[bool, bytes, float, int, str]]) -> Tuple[float, int, Dict[str, Union[bool, bytes, float, int, str]]]

                            - parameters : current global model parameters
                            - config : configuration parameters which allow the server to influence evaluation on the client, can be used to communicate values from the server to the client
                            - loss (float) : evaluation loss of the model on the local dataset
                            - num_examples (int) : number of examples used for evaluation
                            - metrics (Dict) : used to communicate values back to the server

              - abstract fit(parameters: List[ndarray], config: Dict[str, Union[bool, bytes, float, int, str]]) -> Tuple[List[ndarray], int, Dict[str, Union[bool, bytes, float, int, str]]]

              - abstract get_parameters(config: Dict[str, Union[bool, bytes, float, int, str]]) -> List[ndarray]

              get_properties(config: Dict[str, Union[bool, bytes, float, int, str]]) -> Dict[str, Union[bool, bytes, float, int, str]]

flwr.client.start_nmpy_client(
              server_address: str, 
              client: NumPyClient,
              grpc_max_message_length: int = ..., ( default is 526870912, 512MB )
              root_certificates: Optional[ bytes] = ... ( default is None)
              )

#### Server

1. flwr.server.start_server

2. class flwr.server.strategy.Strategy

3. class flwr.server.strategy.FedAvg(
              fraction_fit: float = 1.0, 
              fraction_eval: float = 1.0, 
              min_fit_clients: int = 2, min_eval_clients: int = 2, 
              min_available_clients: int = 2, 
              eval_fn: Optional[ Callable[[List[ ndarray]], Optional[Tuple[float, Dict[str, Union[bool, bytes, float, int, str]]]]]] = None, 
              on_fit_config_fn: Optional[Callable[[ int], Dict[str, Union[bool, bytes, float, int, str]]]] = None, 
              on_evaluate_config_fn: Optional[Callable[[ int], Dict[str, Union[bool, bytes, float, int, str]]]] = None, 
              accept_failures: bool = True, initial_parameters: Optional[ Parameters] = None, 
              fit_metrics_aggregation_fn: Optional[Callable[[List[Tuple[int, Dict[str, Union[bool, bytes, float, int, str]]]]], Dict[str, Union[bool, bytes, float, int, str]]]] = None, 
              evaluate_metrics_aggregation_fn: Optional[Callable[[List[Tuple[int, Dict[str, Union[bool, bytes, float, int, str]]]]], Dict[str, Union[bool, bytes, float, int, str]]]] = None)


2022.07.18

# Flower Framework

## Flower Summit 2021

### 

## Flower Summit 2022

## Implementing new strategy
<https://flower.dev/docs/implementing-strategies.html.>

2022.07.20

```
class Strategy(ABC):
    """Abstract base class for server strategy implementations."""

    @abstractmethod
    def initialize_parameters(
        self, client_manager: ClientManager
    ) -> Optional[Parameters]:
        """Initialize the (global) model parameters."""

    @abstractmethod
    def configure_fit(
        self, rnd: int, parameters: Parameters, client_manager: ClientManager
    ) -> List[Tuple[ClientProxy, FitIns]]:
        """Configure the next round of training."""

    @abstractmethod
    def aggregate_fit(
        self,
        rnd: int,
        results: List[Tuple[ClientProxy, FitRes]],
        failures: List[BaseException],
    ) -> Tuple[Optional[Parameters], Dict[str, Scalar]]:
        """Aggregate training results."""

    @abstractmethod
    def configure_evaluate(
        self, rnd: int, parameters: Parameters, client_manager: ClientManager
    ) -> List[Tuple[ClientProxy, EvaluateIns]]:
        """Configure the next round of evaluation."""

    @abstractmethod
    def aggregate_evaluate(
        self,
        rnd: int,
        results: List[Tuple[ClientProxy, EvaluateRes]],
        failures: List[BaseException],
    ) -> Tuple[Optional[float], Dict[str, Scalar]]:
        """Aggregate evaluation results."""

    @abstractmethod
    def evaluate(
        self, parameters: Parameters
    ) -> Optional[Tuple[float, Dict[str, Scalar]]]:
        """Evaluate the current model parameters."""
```

```
class SotaStrategy(Strategy):
    def initialize_parameters(self, client_manager):
        # Your implementation here

    def configure_fit(self, rnd, parameters, client_manager):
        # Your implementation here

    def aggregate_fit(self, rnd, results, failures):
        # Your implementation here

    def configure_evaluate(self, rnd, parameters, client_manager):
        # Your implementation here

    def aggregate_evaluate(self, rnd, results, failures):
        # Your implementation here

    def evaluate(self, parameters):
        # Your implementation here
```