from ..wrapper import NWaves 


 

class MathUtils:

	def __init__(self, *args, **kwargs):
		self._MathUtils = NWaves.Utils.MathUtils(*args, **kwargs)
 
	def asinh(self, x):
		return self._MathUtils.Asinh(x)
 
	def bilinear_transform(self, re, im):
		return self._MathUtils.BilinearTransform(re, im)
 
	def binomial_coefficient(self, k, n):
		return self._MathUtils.BinomialCoefficient(k, n)
 
	def diff(self, samples, diff):
		return self._MathUtils.Diff(samples, diff)
 
	def divide_polynomial(self, dividend, divisor):
		return self._MathUtils.DividePolynomial(dividend, divisor)
 
	def equals(self, *args, **kwargs):
		return self._MathUtils.Equals(*args, **kwargs)
 
	def evaluate_polynomial(self, a, x):
		return self._MathUtils.EvaluatePolynomial(a, x)
 
	def factorial(self, n):
		return self._MathUtils.Factorial(n)
 
	def finalize(self, *args, **kwargs):
		return self._MathUtils.Finalize(*args, **kwargs)
 
	def find_nth(self, a, n, start, end):
		return self._MathUtils.FindNth(a, n, start, end)
 
	def gcd(self, n, m):
		return self._MathUtils.Gcd(n, m)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MathUtils.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MathUtils.GetType(*args, **kwargs)
 
	def i0(self, x):
		return self._MathUtils.I0(x)
 
	def interpolate_linear(self, x, y, arg, interp):
		return self._MathUtils.InterpolateLinear(x, y, arg, interp)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MathUtils.MemberwiseClone(*args, **kwargs)
 
	def mod(self, a, b):
		return self._MathUtils.Mod(a, b)
 
	def multiply_polynomials(self, poly1, poly2):
		return self._MathUtils.MultiplyPolynomials(poly1, poly2)
 
	def next_power_of_two(self, n):
		return self._MathUtils.NextPowerOfTwo(n)
 
	def overloads(self, *args, **kwargs):
		return self._MathUtils.Overloads(*args, **kwargs)
 
	def polynomial_roots(self, a, maxIterations: int=25000):
		return self._MathUtils.PolynomialRoots(a, maxIterations)
 
	def reference_equals(self, objA, objB):
		return self._MathUtils.ReferenceEquals(objA, objB)
 
	def sinc(self, x):
		return self._MathUtils.Sinc(x)
 
	def to_string(self, *args, **kwargs):
		return self._MathUtils.ToString(*args, **kwargs)
 
	def unwrap(self, phase, tolerance=3.141592653589793):
		return self._MathUtils.Unwrap(phase, tolerance)
 
	def wrap(self, phase, tolerance=3.141592653589793):
		return self._MathUtils.Wrap(phase, tolerance)