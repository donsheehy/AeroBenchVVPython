import pickle
from metricspaces import NumpyPoint as Point

data = [pickle.load(open('simulation' + str(i) + '.p', 'rb')) for i in range(10)]



print((data[0]['states'][50]))

# x,u = data[i]['states']
# where x has type SystemState
# and u has type InputState
