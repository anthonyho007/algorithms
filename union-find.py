class UnionFind:
    def __init__(size):
        self.size = size
        self.p = [0] * self.size
        self.rank = [0] * self.size
        for i in len(self.p):
            p[i] = i
    
    def find_set(num):
        return num if self.p[num] == num else find_set(p[num])
    
    def is_union(num1, num2):
        return find_set(num1) == find_set(num2)
    
    def join_set(num1, num2):
        if not is_union(num1, num2):
            end1, end2 = find_set(num1), find_set(num2)
            if rank[end1] > rank[end2]:
                p[end2] = p[end1]
            else:
                p[end1] = p[end2]
                rank[end2] += 1

