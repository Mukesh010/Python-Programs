class FibIterator:
    def __init__(self, N):
        self.Fib = [0,1]
        self.i = N
	def next(self):
		self.i +=1
		while(self.i >1):
			self.Fib.append( self.Fib[len(self.Fib)-1] + self.Fib[len(self.Fib)-2] )
			self.i -=1
		return self.Fib[len(self.Fib) -1]
