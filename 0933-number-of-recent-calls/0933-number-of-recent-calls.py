class RecentCounter:

   def __init__(self):
       self.time = collections.deque()
       # self.time = []

   def ping(self, t: int) -> int:
       # out = 1 # include the recent t
       # for i in self.time[::-1]:
       #     if i < t - 3000:
       #         break
       #     else:
       #         out += 1
       
       # self.time.append(t)
       # return out 
       self.time.append(t)
       while self.time[0] < t - 3000:
           self.time.popleft()
       return len(self.time)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)