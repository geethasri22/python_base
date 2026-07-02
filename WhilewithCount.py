class Solution:
    def whileLoop(self, d : int) -> int:
        # Your code goes here
        total =0
        count = 0 
        c_n = d if d >0 else 10 #c_n =2 if d =2 
        while count <50: #count = 0 so true
            total += c_n #total =2 
            c_n += 10     #c_n 12
            count += 1     #count = 1
        return total
