# just test
import numpy as np
import torch


def cos_similarity(a1, a2):
    return np.dot(a1, a2) / (np.linalg.norm(a1) * np.linalg.norm(a2))


def cos_similarity_torch(a1, a2):
    a1 = torch.Tensor(a1)
    a2 = torch.Tensor(a2)
    torch_result=torch.dot(a1, a2) / (torch.norm(a1) * torch.norm(a2))
    return float(torch_result)


if __name__ == "__main__":
    print(cos_similarity(a1=[1, 0, 0], a2=[0, 1, 0]))
    print(cos_similarity_torch(a1=[1, 0, 0], a2=[0, 1, 0]))
