from dotenv import dotenv_values
from rss.client import rssFromS3

from gaiaviz.model.i_seismic_service import ISeismicService

ACCESS_KEY = 'AWS_ACCESS_KEY'
SECRET_KEY = 'AWS_SECRET_KEY'

class RSSSeismicService(ISeismicService):

    def __init__(self, filename):
        env_data = dotenv_values('.env')
        access_key =  env_data[ACCESS_KEY]
        secret_key = env_data[SECRET_KEY]

        connection_kwargs = {
            'aws_access_key_id': access_key,
            'aws_secret_access_key': secret_key
        }

        self.client = rssFromS3(filename=filename,
                                client_kwargs=connection_kwargs)

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
        array, mask = self.client.line(line_number, line_type)
        return array
