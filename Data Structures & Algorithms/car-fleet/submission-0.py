class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        target = 10, position = [1,4], speed = [3,2]

        combine the position and speed arrays together

        [(1, 3), (4, 2)]
        then we can sort it by the position
        [(4,2), (1, 3)]

        iterate through this array to check if it is in a fleet
        use the formula time = (target - position) / speed

        we calcualte and then keep track of the current time because that is the time it takes
        if the next time is greater than the previous one that means it is a new car fleet
        in this case we just increase the number
        but if it is less than or equal then it is in the same car fleet then don't increase it

        [(7,1), (4,2), (1, 2), (0, 1)]
        '''

        combine = []
        carfleet = 0
        starttime = float("-inf")
        for f, s in zip(position, speed):
            combine.append((f, s))
        combine.sort(reverse=True)
        for p, s in combine:
            time = (target - p) / s
            if time > starttime:
                carfleet += 1
            starttime = max(starttime, time)
        return carfleet
            