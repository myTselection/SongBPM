
import logging
import requests
from bs4 import BeautifulSoup


_LOGGER = logging.getLogger(__name__)


class ComponentSession(object):
    def __init__(self):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = "Python/3"
        self.s.headers["Accept-Language"] = "en-US,en;q=0.9"

    

    def getSongBpm(self, song):

       
        # self.s = requests.Session()
        # self.s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

        # header = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
        # response = self.s.get("https://jnm.be/nl/inloggen",headers=header,timeout=10,allow_redirects=False)
        # _LOGGER.debug(f"jnm.be login get result status code: {response.status_code}")
        # _LOGGER.debug(f"jnm.be login header: {response.headers}")
        # assert response.status_code == 200

        # # Parse the HTML content
        # soup = BeautifulSoup(response.text, 'html.parser')

        # # Find the meta tag with the name="csrf-token" attribute
        # csrf_token_meta = soup.find('meta', {'name': 'csrf-token'})
        # assert csrf_token_meta != None
        # # Extract the content of the csrf-token meta tag
        # csrf_token = csrf_token_meta['content']

        
        # header = {"Content-Type": "application/x-www-form-urlencoded", "Referer": "https://jnm.be/nl/inloggen", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
        
        # response = self.s.get("https://tunebat.com/Search",headers=header,data=f"q={song}", timeout=15,allow_redirects=True)
        # _LOGGER.debug(f"songbpm post result status code: {response.status_code}")
        # _LOGGER.debug(f"songbpm header: {response.headers}")
        # _LOGGER.debug(f"songbpm text: {response.text}")
        # assert response.status_code == 200

        # response = self.s.get("https://jnm.be/nl/inloggen",headers=header,timeout=10,allow_redirects=True)
        # _LOGGER.debug(f"jnm.be login get result status code: {response.status_code}")
        # _LOGGER.debug(f"jnm.be login header: {response.headers}")
        # assert response.status_code == 200

        # Parse the HTML content
        # soup = BeautifulSoup(response.text, 'html.parser')

        # # Find the meta tag with the name="csrf-token" attribute
        # csrf_token_meta = soup.find('meta', {'name': 'csrf-token'})
        # assert csrf_token_meta != None
        # # Extract the content of the csrf-token meta tag
        # csrf_token = csrf_token_meta['content']
        
    
        # response = self.s.post("https://jnm.be/nl/inloggen",headers=header,data=f"_token={csrf_token}&username={username}&password={password}&login=", timeout=15,allow_redirects=False)
        # _LOGGER.debug(f"jnm.be login post result status code: {response.status_code}")
        # _LOGGER.debug(f"jnm.be login header: {response.headers}")
        # _LOGGER.debug(f"jnm.be login text: {response.text}")
        # assert response.status_code == 302
        

        # response = self.s.get("https://jnm.be/nl/mijn-profielpagina",headers=header, timeout=15,allow_redirects=False)
        # _LOGGER.debug(f"jnm.be profile get status code: {response.status_code}")
        # _LOGGER.debug(f"jnm.be profile header: {response.headers}")
        # _LOGGER.debug(f"jnm.be profile text: {response.text}")
        # assert response.status_code == 200

        # Parse the HTML content
        # soup = BeautifulSoup(response.text, 'html.parser')

        # Create a dictionary to store the extracted data
        # data = {}

        # Extract relevant data
        # Find the unsorted list with the specified class
        # ulist = soup.find('p', class_='lAjUd')

        # _LOGGER.debug(f"ulist: {ulist.text}")

        # if ulist:
        #     # Extract the second list item as the "name" value
        #     list_items = ulist.find_all('li')
        #     if len(list_items) >= 2:
        #         data['user_details'] = {
        #             'name': list_items[1].text.strip(),
        #             'birth_date': soup.find('time').text.strip()
        #         }
        #     else:
        #         data['user_details'] = {
        #             'name': 'Name not found',
        #             'birth_date': 'Birth date not found'
        #         }
        # data['membership'] = {
        #     'username': soup.find('dd').text.strip(),
        #     'membership_number': soup.find_all('strong')[1].text.strip(),
        #     'membership_fee': soup.find_all('dd', class_='ms-2')[1].text.strip()
        # }
        # department = soup.find('div', class_='member__department')
        # data['department'] = {
        #         'department_title': department.h3.a.text.strip(),
        #         'age_group': department.dl.dd.text.strip()
        #     }

        return data
