import requests, re, json, logging

logger = logging.getLogger(__name__)
request_validation_re = re.compile(r'<input name="__RequestVerificationToken" type="hidden" value="([^"]*)" />')

class Ecowater:
    def __init__(self, username, password, serialnumber):
        try:
            self.payload = {
                "Email" : str(username),
                "Password" : str(password),
                "Remember" : 'false'
            }
            self.dsn = {
                "dsn": str(serialnumber)
            }
        except Exception as e:
            logging.error(f'Error with inputs: {e}')

    def _get(self):
        with requests.Session() as session:
            try:
                payload = self.payload
                dsn = self.dsn

                headers = {
                    'Accept': '*/*',
                    'Accept-Language' : 'en-US,en;q=0.5',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/102.0'
                }
            except Exception as e:
                logging.error(f'Error setting variables: {e}')

            try:
                website_data = session.get('https://wifi.ecowater.com/Site/Login')
            except requests.exceptions.RequestException as e:
                logging.error(f'Error connecting to "wifi.ecowater.com": {e}')

            tokens = request_validation_re.findall(website_data.text)
            payload['__RequestVerificationToken'] = tokens[0]

            try:
                website_login = session.post('https://wifi.ecowater.com/Site/Login', data=payload)
            except requests.exceptions.RequestException as e:
                logging.error(f'Error logging in to "wifi.ecowater.com": {e}')

            headers['Referer'] = website_login.url + '/' + dsn['dsn']

            try:
                data = session.post('https://wifi.ecowater.com/Dashboard/UpdateFrequentData', data=dsn, headers=headers)
            except requests.exceptions.RequestException as e:
                logging.error(f'Error getting json from "wifi.ecowater.com": {e}')

            if data.status_code != 200:
                logging.error(f'Error status code of: {data.status_code}')

            json_data = json.loads(data.text)

            return json_data

    def getData(self):
        try:
            data = self._get()
            new_data = {}

            nextRecharge_re = "device-info-nextRecharge'\)\.html\('(?P<nextRecharge>.*)'"

            new_data['daysUntilOutOfSalt'] = int(data['out_of_salt_days'])
            new_data['outOfSaltOn'] = data['out_of_salt']
            new_data['saltLevel'] = data['salt_level']
            new_data['saltLevelPercent'] = data['salt_level_percent']
            new_data['waterUsageToday'] = data['water_today']
            new_data['waterUsageDailyAverage'] = data['water_avg']
            new_data['waterAvailable'] = data['water_avail']
            new_data['waterFlow'] = data['water_flow']
            new_data['waterUnits'] = data['water_units']
            new_data['rechargeEnabled'] = data['rechargeEnabled']
            new_data['rechargeScheduled'] = False if (re.search(nextRecharge_re, data['recharge'])).group('nextRecharge') == 'Not Scheduled' else True
            new_data['deviceStatus'] = data['online']

            return new_data
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def daysUntilOutOfSalt(self):
        try:
            return int(self._get()['out_of_salt_days'])
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def outOfSaltOn(self):
        try:
            return self._get()['out_of_salt']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def saltLevel(self):
        try:
            return self._get()['salt_level']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def saltLevelPercent(self):
        try:
            return self._get()['salt_level_percent']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def waterUsageToday(self):
        try:
            return self._get()['water_today']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def waterUsageDailyAverage(self):
        try:
            return self._get()['water_avg']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def waterAvailable(self):
        try:
            return self._get()['water_avail']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def waterFlow(self):
        try:
            return self._get()['water_flow']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def waterUnits(self):
        try:
            return self._get()['water_units']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def rechargeEnabled(self):
        try:
            return self._get()['rechargeEnabled']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def rechargeScheduled(self):
        try:
            nextRecharge_re = "device-info-nextRecharge'\)\.html\('(?P<nextRecharge>.*)'"
            nextRecharge_result = re.search(nextRecharge_re, self._get()['recharge'])
            return False if nextRecharge_result.group('nextRecharge') == 'Not Scheduled' else True
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''

    def deviceStatus(self):
        try:
            return self._get()['online']
        except Exception as e:
            logging.error(f'Error with data: {e}')
            return ''
