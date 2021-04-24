import numpy as np

def batch_norm_implement(data):
    mini_batch_mean = data.sum(axis=0) / len(data)
    mini_batch_var = ((data-mini_batch_mean) ** 2).sum(axis=0) / len(data)
    batch_norm_res = (data-mini_batch_mean) / ((mini_batch_var + 1e-8) ** 0.5)
    return batch_norm_res

if __name__ == '__main__':
    data = np.array([[1,2,4],[3,4,5]])
    print(batch_norm_implement(data))
