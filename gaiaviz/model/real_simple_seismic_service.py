from dotenv import load_dotenv

from gaiaviz.model.i_seismic_service import ISeismicService


class RSSSeismicService(ISeismicService):

    def __init__(self, filename):
        load_dotenv()
        access_key = 
        

    def load_line(line_type, line_number):
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
        self.client
