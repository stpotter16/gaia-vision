from abc import ABC, abstractmethod


class ISeismicService(ABC):

    @abstractmethod
    def load_line(self, line_type, line_number):
        """
        Load a seismic slice from from the survey

        Paramters
        ---------
        line_type : str
            Line slice to load {inline, crossline, depth}
        line_number : int
            Line number of the slice to load
        
        Returns
        -------
        data : numpy.ndarray
            Slice data as a 2D numpy array
        """
        raise NotImplementedError()
