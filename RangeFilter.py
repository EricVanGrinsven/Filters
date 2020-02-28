class RangeFilter:
    def __init__(self, range_min, range_max):
        self.range_min = range_min
        self.range_max = range_max
    def Update(self, distanceMeasurements):
        for i in range(len(distanceMeasurements)):
            "if below min, choose min"
            distanceMeasurements[i] = max(self.range_min, distanceMeasurements[i])
            "if above max, choose max"
            distanceMeasurements[i] = min(self.range_max, distanceMeasurements[i])
        return distanceMeasurements
        
        