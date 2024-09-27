# **V2.0.0 BREAKING CHANGES**
**For version 2.0.0 the library has been rewritten and methods have changed.**

# Ecowater Softener

ecowater-softener is a Python library for collecting information from Ecowater water softeners.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ecowater.

```bash
pip install ecowater-softener
```

## Usage

Liquids are measured in **US Gallons**, liquid speeds are measured in **US Gallons per Minute (gpm)**, and weights are measured in **Pounds (lbs)**

Importing the library

```python
import ecowater_softener
```

Initialize Ecowater account using username and password credentials

```python
ecowater_account = ecowater_softener.EcowaterAccount('username', 'password')
```

Retrieve a list of all devices associated with the Ecowater account

```python
devices = ecowater_account.get_devices()
```

Access the first device from the list of devices

```python
device = devices[0]
```

Get the signal strength (rssi) (integer)

```python
rssi = device.rssi
```

Get the device's serial number (string)

```python
serial_number = device.serial_number
```

Get the device's ip address (string)

```python
ip_address = device.ip_address
```

Get the number of days until the device runs out of salt (integer)

```python
days_until_out_of_salt = device.out_of_salt_days
```

Get the estimated date when the device will run out of salt (datetime.date)

```python
salt_depletion_date = device.out_of_salt_date
```

Get the current salt level as a percentage (integer)

```python
salt_level_percentage = device.salt_level_percentage
```

Get the amount of water used today (integer)

```python
water_usage_today = device.water_use_avg_today
```

Get the average daily water usage (integer)

```python
average_daily_water_usage = device.water_use_avg_daily
```

Get the current amount of available water (integer)

```python
available_water = device.water_available
```

Get the current water flow rate (integer)

```python
current_water_flow = device.current_water_flow
```

Get the number of days since the last recharge was performed (integer)

```python
days_since_last_recharge = device.last_recharge_days
```

Get the date of the last recharge (datetime.date)

```python
last_recharge_date = device.last_recharge_date
```

Check if recharge is enabled (boolean)

```python
is_recharge_enabled = device.recharge_enabled
```

Check if a recharge is scheduled (boolean)

```python
is_recharge_scheduled = device.recharge_scheduled
```

Get the total amount of rock removed by the device over its lifetime (integer)

```python
lifetime_rock_removed = device.rock_removed
```

## Credits

-   [Kyle Johnson](https://github.com/kylejohnson) for his work on using python to interface with Ecowater water softeners. Most of this libraries code was originally built upon code which he wrote. You can read his article regarding scraping data from Ecowater water softeners at https://gnulnx.net/2020/02/18/ecowater-api-scraping/
-   [@rewardone](https://github.com/rewardone) for creating [ayla-iot-unofficial](https://github.com/rewardone/ayla-iot-unofficial) which is used to fetch the data
-   [Jeff Rescignano](https://github.com/JeffResc) for creating [sharkiq](https://github.com/JeffResc/sharkiq) which [ayla-iot-unofficial](https://github.com/rewardone/ayla-iot-unofficial) is based on.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
