class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_record = []
        for i in operations:
            if i == "+":
                new_sum = new_record[-1] + new_record[-2]
                new_record.append(new_sum)
            elif i == "D":
                double = 2 * new_record[-1]
                new_record.append(double)
            elif i == "C":
                new_record.pop()
            else:
                new_record.append(int(i))
        return sum(new_record)