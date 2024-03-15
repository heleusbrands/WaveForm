import pandas as pd
import numpy as np
from parselmouth.praat import call
import parselmouth as pm
from typing import Union
from .xtract_configs import *
from .commands import *
from multipledispatch import dispatch, Dispatcher
from typing import Any

class TimeBase:
    pci_dispatch = Dispatcher('pci_dispatch')
    def __init__(self, end_time, Tseries=None, DataSeries=None, name='None'):
        self._TimeSeries = Tseries
        self._DataSeries = DataSeries
        self.name = name
        self.start_time = 0.0
        self.end_time = end_time
        self.type_name = None
        

    def _load(self):
        if self._TimeSeries and self._DataSeries: self.load(self._TimeSeries, self._DataSeries)

    @property    
    def _pci(self):
        return call(self.type_name, self.name, self.start_time, self.end_time)
    
    @dispatch(str, pm.Data, list)
    def _commands_pci(self, command, pci, *args):
        return call([self._pci, pci], command, *args)
    
    @dispatch(str, list)
    def _commands_pci(self, command, *args):
        return call(self._pci, command, *args)
        
    
    def _add_point(self, time, value):
        self._commands_pci('Add point...', time, value)

    def _nearest_index(self, time):
        return self._commands_pci('Get nearest index from time...', time)
    
    @property
    def _point_count(self):
        return self._commands_pci('Get number of points')
    
    def _get_value_at_time(self, time):
        return self._commands_pci('Get value at time...', time)
    
    def _get_value_at_index(self, index):
        return self._commands_pci('Get value at index...', index)
    
    def _values(self):
        return [self._get_value_at_index(i+1) for i in range(self._point_count)]
    
    @dispatch(pd.Series, pd.Series)
    def load(self, Tseries: pd.Series, Oseries: pd.Series):
        t = Tseries.to_list()
        o = Oseries.to_list()
        data = list(zip(t, o))
        for time, value in data:
            self._add_point(time, value)

    @dispatch(list, list)
    def load(self, Tseries: list, Oseries: list):
        data = list(zip(Tseries, Oseries))
        for time, value in data:
            self._add_point(time, value)



class IntensityTier(TimeBase):
    def __init__(self, end_time, TimeSeries=None, DataSeries=None, name='IntensityTier'):
        super().__init__(end_time, TimeSeries, DataSeries, name)
        self.type_name = 'Create IntensityTier...'
        self._load()

    def __repr__(self):
        return f'IntensityTier({self.start_time}, {self.end_time}, {self.name})'
    
    def add_intensity(self, time, intensity):
        if type(intensity) == pd.Series: intensity = intensity.to_list()
        if type(time) == pd.Series: time = time.to_list()
        if type(intensity) == float: self._add_point(time, intensity)
        elif type(intensity) == list and type(time) == list:
            for t, i in zip(time, intensity):
                self._add_point(t, i)
    
    def get_intensity_at_time(self, time):
        return self._get_value_at_time(time)
    
    def get_intensity_at_index(self, index):
        return self._get_value_at_index(index)
    
    def get_nearest_intensity_index(self, time):
        return self._nearest_index(time)
    
    @property
    def intensity_point_count(self):
        return self._point_count
    
    @property
    def intensity_values(self):
        return self._values()
    
    @property
    def amplitude_tier(self):
        return self._commands_pci('To AmplitudeTier')
    
    @property
    def point_process(self):
        return self._commands_pci('Down to PointProcess')

    def multiply(self, sound: pm.Sound):
        return self._commands_pci('Multiply...', sound, 'yes')



class Grid:
    def __init__(self, sound):
        if type(sound) == pm.Sound: self.sound: pm.Sound = sound
        elif type(sound) == str: self.sound = pm.Sound(sound)
        elif type(sound) == pm.Matrix: self.sound = sound
        else: raise TypeError('The sound must be a sound object, a string, or a matrix object.')
        # Creates a PraatCommands object called pci, which is preloaded with the sound. 
        self.pci = PraatCommands(self.sound)
        self._extract_all = True

    def _extract(self, input, obj_type: Union[str, None]=None):
        '''It takes a Praat object (e.g. a Sound, a Formant, a Matrix, etc.) and returns a Matrix object
        
        The function takes two arguments:
        
        1. input: the input object to be converted to a matrix
        2. obj_type: str, optional
        
        The function returns a list of matrixes
        
        Parameters
        ----------
        input
            the input object to be converted to a matrix
        obj_type : Union[str, None]
            str, optional
        
        Returns
        -------
            A list of matrixes.
        
        '''
        f_types = ['f', 'formant', 'formants']
        d_types = ['d', 'data', 'to matrix', 'matrix']
        s_types = ['s', 'sound', 'sound object']
        if obj_type is not None: 
            if obj_type.lower() in f_types:
                formant = PraatCommands(input).to_formant()
                nformants = PraatCommands(formant.result).get_number_of_formants_in_frame()
                matrixes = [
                    PraatCommands(formant.result).to_matrix(column_index=i).result for i in range(nformants)
                    ]
                return matrixes
            elif obj_type.lower() in d_types:
                matrix = PraatCommands(input).to_matrix()
                return matrix.result
            elif obj_type.lower() in s_types:
                if type(input) == pm.Sound: return input
        realtable = PraatCommands(input).down_to_table_of_real()
        matrix = PraatCommands(realtable.result).to_matrix()
        return matrix.result
    
    def _to_feature(self, matrix, col_names:list = None, name: str=None, obj_type: Union[str, None]=None):
        '''> It takes a matrix, and returns a feature
        
        Parameters
        ----------
        matrix
            The matrix to be converted to a feature.
        col_names : list
            list of column names
        name : str
            The name of the feature.
        obj_type : Union[str, None]
            str = None
        
        Returns
        -------
            A Feature object
        
        '''

        if name is None: name = matrix.name
        return Feature(self._extract(matrix, obj_type), col_names, name)
    
class Feature(ObjectX):
    """A class for extracting features from a Praat object.
    Parameters
    ----------
    matrix: Union[pm.Matrix, pm.Sound, pm.Intensity]
        The Praat object to extract features from.
    column_names: list
        The names of the columns in the matrix.
    feature_name: str
        The name of the feature.
    manual_array: None or array
        If the feature is not a Praat object, you can manually pass in the array of features.
    """
    
    def __init__(self, 
                 matrix: Union[pm.Matrix, pm.Sound, pm.Intensity], 
                 column_names: list, 
                 feature_name: str = None, 
                 manual_array: np.ndarray = None):
        self._PM_Types = [pm.Matrix, pm.Sound, pm.Intensity]
        self._M = False
        self._S = False
        self._MSET = False
        self._series = {}
        self._drop = []
        self._replace = {}
        if type(matrix) in self._PM_Types: self._M = True
        elif type(matrix) == pm.Sound: self._S = True
        if manual_array is not None: self._MSET = True
        self._matrix = matrix
        if self._M or self._S: self._val_iter = iter(matrix.values)
        elif self._MSET: self._val_iter = iter(manual_array)
        self.name = feature_name
        self.column_names = column_names
        if self._M: self.column_count = matrix.get_number_of_columns()
        if self._M: self.row_count = matrix.get_number_of_rows()
        if self._M: self.info = matrix.info()
        if self._S or self._M: self.array = matrix.values
        elif self._MSET: self.array = manual_array
        else: self.array = matrix.as_array()
        if 'time' in [i.lower() for i in column_names]: self._time = True
        else: self._time = False
        

    @property
    def get_next_value(self):
        return next(self._val_iter)

    @property
    def dataframe(self):
        x, y = self.array.shape
        if x > 2 and y > 2:
            data = {self.column_names[i]: self.array[:,i] for i in range(y)}
            dataframe = pd.DataFrame(data)
            if self._drop: dataframe.drop(columns=self._drop, inplace=True)
            if self._replace: dataframe.replace(self._replace, inplace=True)
            return self._update_series(dataframe)
        elif x > 1 and y > 1:
            dataframe = pd.DataFrame(self.array.squeeze(), columns=self.column_names)
            if self._drop: dataframe.drop(columns=self._drop, inplace=True)
            if self._replace: dataframe.replace(self._replace, inplace=True)
            return self._update_series(dataframe)
        else:
            if self.array is None: raise ValueError('The array is empty.')
            dataframe = pd.Series(self.array.squeeze(), name=self.name)
            if self._drop: dataframe.drop(columns=self._drop, inplace=True)
            if self._replace: dataframe.replace(self._replace, inplace=True)
            return self._update_series(dataframe)
    
    @property
    def time_series(self):
        self.dataframe
        if self._time:
            series = self._series.keys()
            for s in series:
                if 'time' in s.lower(): return self._series[s]
        else:
            raise ValueError('The feature does not have a time column.')

    def _update_series(self, dataframe: Union[pd.DataFrame, pd.Series]):
        if type(dataframe) == pd.Series:
            self._series[self.name] = dataframe
        elif type(dataframe) == pd.DataFrame:
            for col in dataframe.columns:
                self._series[self.name.replace(' ', '') + '_' + col.replace(' ', '')] = pd.Series(dataframe[col], name=col)
        return dataframe

    @property
    def min(self):
        return self.dataframe.min()
    
    @property
    def max(self):
        return self.dataframe.max()
    
    @property
    def mean(self):
        return self.dataframe.mean()
    
    @property
    def median(self):
        return self.dataframe.median()
    
    @property
    def std(self):
        return self.dataframe.std()
    
    @property
    def var(self):
        return self.dataframe.var()
    
    @property


    @property
    def columns_count(self):
        return self.dataframe.columns.size
    
    def find_clostest_indexes_to(self, value, column, dataframe:pd.DataFrame=None):
        """
        Find the indexes of the closest values to a given value in a column of a dataframe.
        """
        if dataframe is None: df = self.dataframe
        else: df = dataframe
        exactmatch = df[df[column] == value]
        if not exactmatch.empty:
            return exactmatch.index
        else:
            low_neighbor_idx = df[df[column] < value][column].idxmax()
            high_neighbor_idx = df[df[column] > value][column].idxmin()
            return low_neighbor_idx, high_neighbor_idx

    def find_clostest_values_to(self, value, column, dataframe: pd.DataFrame=None):
        """
        Find the closest values to a given value in a column of a dataframe.
        Returns
        -------
        lower_value: the lower value
        higher_value: the higher value
        Example
        -------
        >>> df = pd.DataFrame([[1,2,3], [2,3,4], [3,4,5]], columns=['a', 'b', 'c'])
        >>> df
           a  b  c
        0  1  2  3
        1  2  3  4
        2  3  4  5
        >>> find_clostest_values_to(1.5, 'a', df)
        (1, 2)
        >>> find_clostest_values_to(2.5, 'a', df)
        (2, 3)
        >>> find_clostest_values_to(2.5, 'b', df)
        (2, 3)
        >>> find_clostest_values_to(2.5, 'c', df)
        (3, 4)
        >>> find_clostest_values_to(1.5, 'c', df)
        (3, 4)
        >>> find_clostest_values_to(3.5, 'c', df)
        (5, "IndexError: index 3 is out of bounds for axis 0 with size 3
        """

        if dataframe is None: df = self.dataframe
        else: df = dataframe
        i1, i2 = self.find_clostest_indexes_to(value, column, df)
        lower_value = df.loc[i1, column]
        higher_value = df.loc[i2, column]
        return lower_value, higher_value

    def value_pairs(self, other: FeatureType = None):
        """
        Returns a list of tuples of value pairs.
        """
        if other is None:
            return [v for v in self.dataframe.rolling(2)]
        else:
            data = {self.name: self.dataframe, other.name: other.dataframe}
            return [v for v in pd.DataFrame(data).rolling(1)]
    
    @property
    def vp(self):
        return self.value_pairs

    def vp_deviations(self, other: FeatureType = None):
        """
        Value Pair Deviations
        """
        vp = self.value_pairs(other)
        return pd.Series([s.std() for s in vp], name=f'{self.name} VP Deviation')
    
    @property
    def vp_max(self):
        """
        Value Pair Deviations Max
        """
        return self.vp_deviations.max()
    
    @property
    def vp_min(self):
        """
        Value Pair Deviations Min
        """
        return self.vp_deviations.min()

class ComparisonGrid:
    def __init__(self, fseries1: pd.Series, fseries2: pd.Series):
        self.__S1 = fseries1
        self.__S2 = fseries2
        self.series1 = fseries1
        self.series2 = fseries2

    @property
    def reverse(self):
        self.series1 = self.__S2
        self.series2 = self.__S1
        return self

    @property
    def compare(self):
        return self.series1.compare(self.series2)
    
    @property
    def difference(self):
        return self.series1 - self.series2
    
    @property
    def quotient(self):
        return self.series1 / self.series2
    
    @property
    def percentage_comparison(self):
        return self.quotient * 100
    
    @property
    def percentage_difference(self):
        return 100 - self.percentage_comparison
    
class CollectionMatrix:
    def __init__(self, features: list[Feature], name: str = None):
        self.name = name
        self._features = features
        self.features = [feature.array for feature in features]
        self.column_names = [feature.column_names for feature in features]

    @property
    def dataframe(self):
        return pd.DataFrame(self.features, columns=self.colum_names)