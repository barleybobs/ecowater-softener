# Ecowater Softener
 ![PyPI](https://img.shields.io/pypi/v/ecowater-softener?style=for-the-badge)
 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ecowater-softener?style=for-the-badge)
 ![PyPI - License](https://img.shields.io/pypi/l/ecowater-softener?style=for-the-badge)
 ![GitHub Repo stars](https://img.shields.io/github/stars/barleybobs/ecowater-softener?style=for-the-badge)

ecowater-softner is a Python library for collecting information from Ecowater water softeners.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ecowater.

```bash
pip install ecowater-softener
```

## Usage

```python
from ecowater_softener import Ecowater

ecowaterDevice = Ecowater('username', 'password', 'serialnumber')

# returns 'days until the device is out of salt' as an integer
ecowaterDevice.daysUntilOutOfSalt()

# returns 'date when device will run out of salt' as datetime object
ecowaterDevice.outOfSaltOn()

# returns 'the salt level' as an integer
ecowaterDevice.saltLevel()

# returns 'the salt level in percent' as an integer
ecowaterDevice.saltLevelPercent()

# returns 'the amount of water used today' as an integer
ecowaterDevice.waterUsageToday()

# returns 'the average amount of water used daily' as an integer
ecowaterDevice.waterUsageDailyAverage()

# returns 'the amount of water available' as an integer
ecowaterDevice.waterAvailable()

# returns 'the amount of water flow' as an integer
ecowaterDevice.waterFlow()

# returns 'the units for the water measurements' as a string
ecowaterDevice.waterUnits()

# returns 'true or false depending on whether recharge is enabled'
ecowaterDevice.rechargeEnabled()

# returns 'true or false depending on whether there is a recharge scheduled'
ecowaterDevice.rechargeScheduled()

# returns 'true or false depending on whether the device is online'
ecowaterDevice.deviceStatus()
```

## Credits
Thanks to [Kyle Johnson](https://github.com/kylejohnson) for his work on using python to interface with Ecowater water softeners. Most of this libraries code is built upon code which he wrote. You can read his article regarding scraping data from Ecowater water softeners at https://gnulnx.net/2020/02/18/ecowater-api-scraping/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
