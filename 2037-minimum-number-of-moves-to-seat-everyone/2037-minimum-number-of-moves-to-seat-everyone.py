class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        summ = 0
        seats.sort()
        students.sort()
        for i in range(len(students)) :
            summ += (abs(students[i] - seats[i]))
        return summ