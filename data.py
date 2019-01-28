import csv

class dataCollector:
    
    def __init__(self, NN_file, data_file):
        self.NN_file = NN_file
        self.data_file = data_file
    
    def writeOutData(self, obj):
        with open(self.data_file, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(['Gen', 'Best', 'Average'])
            for i in range(len(obj.bests)):
                writer.writerow([i+1,obj.bests[i], obj.averages[i]])
    
    def writeOutWeights(self, obj):
        with open(self.NN_file, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            tables = [obj.best.nn.weights_i, obj.best.nn.weights_h, obj.best.nn.bias_i, obj.best.nn.bias_h]
            for t in tables:
                writer.writerows(t.values)
                writer.writerow([''])
    
    def readInWeights(self):
        weights = [[],[],[],[]]
        i = 0
    
        with open(self.NN_file, "r") as input:
            reader = csv.reader(input)
            for row in reader:
                if row == ['']:
                    i += 1
                else:
                    weights[i].append([float(r) for r in row])
    
        return weights
    
