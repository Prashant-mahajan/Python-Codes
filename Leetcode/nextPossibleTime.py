class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        
        nums = sorted(set(hour + minute))
        possible_values = [a+b for a in nums for b in nums]
        # print(possible_values)
        
        # Check if next valid minute is in below 60
        i = possible_values.index(minute)
        if i + 1 < len(possible_values) and possible_values[i+1] < "60":
            return hour + ":" + possible_values[i+1]
        
        # Check the next possible min hour 
        i = possible_values.index(hour)
        if i + 1 < len(possible_values) and possible_values[i+1] < "24":
            return possible_values[i+1] + ":" + possible_values[0]
        
        # If both conditions are false, possible value would be first element in the list i.e. next day value
        return possible_values[0] + ":" + possible_values[0]
    