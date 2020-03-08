
import torch
a=torch.randn(3,1)
b=torch.randn(3)
print(a,b,)
print(torch.mul(a,b),torch.mul(a,b).shape)

a=torch.tensor([[1],[2],[3]])
b=torch.tensor([[1,2,3]])
print(torch.mul(a,b))
print(torch.mm(a,b))