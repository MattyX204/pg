from unittest.mock import MagicMock
from sixth import download_url_and_get_all_hrefs

class result:
    def __init__(self, status_code, content)
        self.ok = status_code == 200
        self.content = content
        

def test_download_url_and_get_all_hrefs():
    requests.get = MagicMock (return_value=result(200,"ahoj"))