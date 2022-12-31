import numpy as np

input_data = np.array([1,2,3])
weights = {'node_0':np.array([1,1,1]),
           'node_1':np.array([-1,2,2]),
           'node_2':np.array([1,3,-1]),
           'output_0':np.array([1,1,-1]),
           'output_1':np.array([1,-1,1])}
node_0_value = (input_data*weights['node_0']).sum()
node_1_value = (input_data*weights['node_1']).sum()
node_2_value = (input_data*weights['node_2']).sum() 

hidden_layer_values = np.array([node_0_value, node_1_value,node_2_value])
print(hidden_layer_values)

output_1 = (hidden_layer_values * weights['output_0']).sum()
print(output_1)
output_2 = (hidden_layer_values * weights['output_1']).sum()
print(output_2)