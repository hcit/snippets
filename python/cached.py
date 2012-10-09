import datetime

class cached(object):

	def __init__(self, method, name=None):
		self.method = method
		self.name = name or method.__name__

	def __get__(self, inst, cls):
		if inst is None:
			return self

		result = self.method(inst)
		setattr(inst, self.name, result)
		return result

class MyObject(object):

	def __init__(self, n):
		self.n = n

	@cached
	def square(self):
		return self.n * self.n

if __name__ == '__main__':
	m = MyObject(3)

	print m.square
	print m.square