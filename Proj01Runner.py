import math

class mean:
    def __init__(self, dataset):
        self.dataset = dataset
        print("\nI certify that this program is my own work\n" +
              "and is not the work of others. I agree not\n" +
              "to share my solution with others.\n" +
              "Thomas Brightly.")

    def calculate(self):
        total = 0
        count = 0
        for num in self.dataset:
            total += num
            count += 1
        return total / count

class median:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
        # calculate odd num dataset
        if len(self.dataset) %2 != 0:
            numCount = len(self.dataset)
            medIndex = int(numCount/2)
            sortedData = sorted(self.dataset)
            return sortedData[medIndex]
        
        # take avg for even num dataset
        else:
            numIndexes = []
            numIndexes.append(int(len(self.dataset) / 2))
            numIndexes.append((int(len(self.dataset) / 2) - 1))
            sortedData = sorted(self.dataset)
            return (sortedData[numIndexes[0]] + sortedData[numIndexes[1]]) / 2


class stdev:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
        calcSum = 0

        for i in self.dataset:
            calcSum += i
        
        calcMean = calcSum / len(self.dataset)

        
        subtractedNums = []
        squaredNums = []

        for num in self.dataset:
            subtractedNums.append(num-calcMean)

        for num in subtractedNums:
            squaredNums.append(num**2)

        squaredSums = 0

        for num in squaredNums:
            squaredSums += num

        return math.sqrt(squaredSums / (len(self.dataset) - 1))


class pstdev:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
        calcSum = 0
        for num in self.dataset:
            calcSum += num
        
        mean = calcSum / len(self.dataset)


        subtractedNums = []
        squaredNums = []
        for num in self.dataset:
            subtractedNums.append(num-mean)

        for num in subtractedNums:
            squaredNums.append(num*num)

        squaredSums = 0

        for num in squaredNums:
            squaredSums += num

        return math.sqrt(squaredSums / len(self.dataset))
    
