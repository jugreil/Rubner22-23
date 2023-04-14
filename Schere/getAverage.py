import json
from json import JSONEncoder
import numpy as np

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

players = None
with open("schere.json", "r") as file:
    players = json.load(file)

counter = 0
pointsAverageArr = np.zeros(60).reshape((20,3))
for i in players:
    for p in range(len(i)):
        pointsAverageArr[p][0] += i[p][0]
        pointsAverageArr[p][1] += i[p][1]
        pointsAverageArr[p][2] += i[p][2]
    counter +=1

for p in pointsAverageArr:
    p[0] /= counter
    p[1] /= counter
    p[2] /= counter
ncodedNumpyData = json.dumps(pointsAverageArr, cls=NumpyArrayEncoder)
with open("schereResult.json", "w") as file:
    json.dump(ncodedNumpyData, file)

