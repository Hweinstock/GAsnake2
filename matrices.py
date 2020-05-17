import copy as c

def multiply(a, b):
    if a.cols != b.rows:
        print "A Columns does not equal B Columns"
        return None
    result = Matrix(a.rows, b.cols)
    for r in range(result.rows):
        for c in range(result.cols):
            sum = 0.0
            for n in range(a.cols):
                sum += a.values[r][n]*b.values[n][c]
            result.values[r][c] = sum
    return result

def fromVector(vector):
    r = len(vector)
    c = 1
    m = Matrix(r, c)
    for i in range(r):
        m.values[i] = [vector[i]]
    return m

def add(a, b):
    output = Matrix(a.rows, a.cols)
    for r in range(output.rows):
        for c in range(output.cols):
            output.values[r][c] = a.values[r][c] + b.values[r][c]
    return output

class Matrix:

    def __init__(self, rows, cols, rand = False):
        self.rows = rows
        self.cols = cols
        self.values = []
        for r in range(self.rows):
            col = []
            for c in range(self.cols):
                col.append(0)
            self.values.append(col)
        if rand:
            self.randomize()

    def printOut(self):
        for r in self.values:
            print r

    def randomize(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.values[r][c] = random(1)*2-1

    def mapOver(self, f):
        for r in range(self.rows):
            for c in range(self.cols):
                self.values[r][c] = f(self.values[r][c])

    def determinant(self):
        pass

    def toVector(self):
        return [x[0] for x in self.values]

    def createCopy(self):
        return c.deepcopy(self)
