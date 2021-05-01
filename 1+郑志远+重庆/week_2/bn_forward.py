import torch
import torch.nn as nn
import numpy as np


class TorchModel(nn.Module):
    def __init__(self, input_size,hidden_size,dim):
        super(TorchModel, self).__init__()
        self.layer = nn.Linear(input_size, hidden_size, bias=False)
        self.batchnorm = nn.BatchNorm1d(dim)


    def forward(self, x):
        x = self.batchnorm(x)
        y = self.layer(x)
        return y

x = torch.randn(1, 20)
print(x)
torch_model = TorchModel(x.shape[1],10,x.shape[1])
print(torch_model.state_dict())