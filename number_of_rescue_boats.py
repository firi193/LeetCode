class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        num_of_boats=0
        l, r=0, len(people) - 1
        while l<=r:
            remain=limit-people[r]
            r-=1
            num_of_boats+=1
            if l<=r and remain>=people[l]:
                l+=1
        return num_of_boats
