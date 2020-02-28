import numpy as np
import statistics
class MedianFilter:
    def __init__(self, D):
        self.D = D
        self.measurements = None
        self.count = 0
    def Update(self, distanceMeasurements):
        distanceMeasurements = np.array([distanceMeasurements])
        "Initialize if first one"
        if self.count == 0:
            self.measurements = distanceMeasurements
        else:
            self.measurements = np.append(self.measurements, distanceMeasurements, axis=0)
        "Remove from matrix the oldest measurement"
        if self.count > self.D:
            self.measurements = np.delete(self.measurements,0,0)
        else:
            self.count += 1


        "Median for odd case"
        "if self.measuresments.shape[1] % 2 = 1"
        distance_return = []
        print(self.measurements)
        for col in range(self.measurements.shape[1]):
            distance_return.append(statistics.median(self.measurements[:,col]))
        return distance_return


'''
Algorithm:
sort the array each time
take the middle guy / avg of middle 2
keep track of where each row of the Dth oldest element
'''