def min1(salary):
    m=salary[0]
    for i in salary:
        if i<m:
            m=i
    return m
def max1(salary):
    m=salary[0]
    for i in salary:
        if i>m:
            m=i
    return m
class Solution:
    def average(self, salary: List[int]) -> float:
        m=min1(salary)
        m2=max1(salary)
        salary.remove(m)
        salary.remove(m2)
        return sum(salary)/len(salary)