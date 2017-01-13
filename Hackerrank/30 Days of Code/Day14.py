	# Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in a:
            for j in a:
                if (i - j) > self.maximumDifference:
                    self.maximumDifference = (i-j)
        return self.maximumDifference
            