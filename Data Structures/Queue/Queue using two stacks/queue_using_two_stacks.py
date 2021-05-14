class Solution:
    def implementQueue(self, Query):
        # write your method here
        ret_arr = []
        for q in Query:
            self.s1 = []
            self.s2 = []
            self.query = q
            if int(self.query[0]) == 1:
                self.enqueue(self.query[-1])
            elif int(self.query[0]) == 2:
                self.dequeue()
            elif int(self.query[0]) == 3:
                ret_arr.append(self.print_front())
        return ret_arr

    def enqueue(self,val):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(val)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) >= 1:
            x = self.s1[-1]
            self.s1.pop()
            return x

    def print_front(self):
        if len(self.s1) == 0:
            return 0
        else:
            return self.s1[-1]