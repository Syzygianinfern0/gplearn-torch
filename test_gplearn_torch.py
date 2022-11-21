import torch

from gplearn_torch.genetic import SymbolicRegressor

x0 = torch.rand(10024, 1).cuda()
x1 = torch.rand(10024, 1).cuda()
x2 = torch.rand(10024, 1).cuda()
y0 = x0 + x1 - x2

x_train = torch.cat([x0, x1, x2], 1)
y_train = y0.squeeze()

est_gp = SymbolicRegressor(
    verbose=1,
    n_jobs=4,
    function_set=("add", "sub", "mul"),
)
est_gp.fit(x_train, y_train)
print(est_gp._program)
