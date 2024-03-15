from ...wrapper import NWaves 


 

class DesignFilter:

	def __init__(self, *args, **kwargs):
		self._DesignFilter = NWaves.Filters.Fda.DesignFilter(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._DesignFilter.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._DesignFilter.Finalize(*args, **kwargs)
 
	def fir(self, o: int, frequencies, gain, fftSize: int=0, window=NWaves.Windows.WindowType):
		return self._DesignFilter.Fir(order, frequencies, gain, fftSize, window)
 
	def fir_bp_to_bs(self, kernel):
		return self._DesignFilter.FirBpToBs(kernel)
 
	def fir_bs_to_bp(self, kernel):
		return self._DesignFilter.FirBsToBp(kernel)
 
	def fir_equiripple_bp(self, order, fa1, fp1, fp2, fa2, wa1, wp, wa2):
		return self._DesignFilter.FirEquirippleBp(order, fa1, fp1, fp2, fa2, wa1, wp, wa2)
 
	def fir_equiripple_bs(self, order, fp1, fa1, fa2, fp2, wp1, wa, wp2):
		return self._DesignFilter.FirEquirippleBs(order, fp1, fa1, fa2, fp2, wp1, wa, wp2)
 
	def fir_equiripple_hp(self, order, fa, fp, wa, wp):
		return self._DesignFilter.FirEquirippleHp(order, fa, fp, wa, wp)
 
	def fir_equiripple_lp(self, order, fp, fa, wp, wa):
		return self._DesignFilter.FirEquirippleLp(order, fp, fa, wp, wa)
 
	def fir_hp_to_lp(self, kernel):
		return self._DesignFilter.FirHpToLp(kernel)
 
	def fir_lp_to_hp(self, kernel):
		return self._DesignFilter.FirLpToHp(kernel)
 
	def fir_win_bp(self, order, frequencyLow, frequencyHigh, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinBp(order, frequencyLow, frequencyHigh, window)
 
	def fir_win_bs(self, order, frequencyLow, frequencyHigh, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinBs(order, frequencyLow, frequencyHigh, window)
 
	def fir_win_fd_ap(self, order, delay, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinFdAp(order, delay, window)
 
	def fir_win_fd_bp(self, order, frequencyLow, frequencyHigh, delay, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinFdBp(order, frequencyLow, frequencyHigh, delay, window)
 
	def fir_win_fd_bs(self, order, frequencyLow, frequencyHigh, delay, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinFdBs(order, frequencyLow, frequencyHigh, delay, window)
 
	def fir_win_fd_hp(self, order, frequency, delay, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinFdHp(order, frequency, delay, window)
 
	def fir_win_fd_lp(self, order, frequency, delay, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinFdLp(order, frequency, delay, window)
 
	def fir_win_hp(self, order, frequency, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinHp(order, frequency, window)
 
	def fir_win_lp(self, order, frequency, window=NWaves.Windows.WindowType):
		return self._DesignFilter.FirWinLp(order, frequency, window)
 
	def get_hash_code(self, *args, **kwargs):
		return self._DesignFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._DesignFilter.GetType(*args, **kwargs)
 
	def iir_bp_tf(self, frequencyLow, frequencyHigh, poles, zeros=None):
		return self._DesignFilter.IirBpTf(frequencyLow, frequencyHigh, poles, zeros)
 
	def iir_bs_tf(self, frequencyLow, frequencyHigh, poles, zeros=None):
		return self._DesignFilter.IirBsTf(frequencyLow, frequencyHigh, poles, zeros)
 
	def iir_comb_notch(self, f: float, q=20.0):
		return self._DesignFilter.IirCombNotch(frequency, q)
 
	def iir_comb_peak(self, f: float, q=20.0):
		return self._DesignFilter.IirCombPeak(frequency, q)
 
	def iir_hp_tf(self, frequency, poles, zeros=None):
		return self._DesignFilter.IirHpTf(frequency, poles, zeros)
 
	def iir_lp_tf(self, frequency, poles, zeros=None):
		return self._DesignFilter.IirLpTf(frequency, poles, zeros)
 
	def iir_notch(self, f: float, q=20.0):
		return self._DesignFilter.IirNotch(frequency, q)
 
	def iir_peak(self, f: float, q=20.0):
		return self._DesignFilter.IirPeak(frequency, q)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._DesignFilter.MemberwiseClone(*args, **kwargs)
 
	def normalize_kernel(self, kernel, frequency=0.0):
		return self._DesignFilter.NormalizeKernel(kernel, frequency)
 
	def overloads(self, *args, **kwargs):
		return self._DesignFilter.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._DesignFilter.ReferenceEquals(objA, objB)
 
	def sos_to_tf(self, sos):
		return self._DesignFilter.SosToTf(sos)
 
	def tf_to_sos(self, tf):
		return self._DesignFilter.TfToSos(tf)
 
	def to_string(self, *args, **kwargs):
		return self._DesignFilter.ToString(*args, **kwargs)