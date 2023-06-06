#%%

import torch
import numpy as np
import seaborn as sns

#%%

x = torch.tensor(5.5)
print(x)

#%%

y = x + 10
print(y)

#%%

print(x.requires_grad_())

#%%

x = torch.tensor(2.0 , requires_grad=True)
print(x.requires_grad)