import torch

a = torch.randn(3, 1)
b = torch.randn(3)
print(a, b, )
print(torch.mul(a, b), torch.mul(a, b).shape)

a = torch.tensor([[1], [2], [3]])
b = torch.tensor([[1, 2, 3]])
print(torch.mul(a, b))
print(torch.mm(a, b))


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


node1 = TreeNode(0)
print(hash(node1))
test = {}
test[node1] = 1
print(test)
node1.val = 1
print(hash(node1))
print(test)
print(test[node1])
node2 = TreeNode(0)
print(hash(node2))
print(id(node2), id(node1))
print(node1 == node2)
import numpy as np

data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(data[..., ::-1, ::])
data.transpose()

a = torch.Tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
b = torch.Tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(a*b)
