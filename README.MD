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

### Account

Initialize Ecowater account using username and password credentials

```python
ecowater_account = ecowater_softener.EcowaterAccount('username', 'password')
```

### Devices

Retrieve a list of all devices associated with the Ecowater account

```python
devices = ecowater_account.get_devices()
```

Access the first device from the list of devices

```python
device = devices[0]
```

Get / Update the devices values (Needs to be ran before accessing data or the data will return None)

```python
device.update()
```

### Device Info

Get the device model (string)

```python
model = device.model
```

Get the device serial number (string)

```python
serial_number = device.serial_number
```

Get the device software version (string)

```python
software_version = device.software_version
```

Get the signal strength (rssi) (integer)

```python
rssi = device.rssi
```

Get the device ip address (string)

```python
ip_address = device.ip_address
```

### Water

Get the average daily water usage (integer)

```python
water_use_avg_daily = device.water_use_avg_daily
```

Get the amount of water used today (integer)

```python
water_use_today = device.water_use_today
```

Get the current amount of available water (integer)

```python
water_available = device.water_available
```

### Water Flow

Get the current water flow rate (integer)

```python
current_water_flow = device.current_water_flow
```

### Salt

Get the current salt level as a percentage (integer)

```python
salt_level_percentage = device.salt_level_percentage
```

Get the number of days until the device runs out of salt (integer)

```python
out_of_salt_days = device.out_of_salt_days
```

Get the estimated date when the device will run out of salt (datetime.date)

```python
out_of_salt_date = device.out_of_salt_date
```

Get the salt type, either "NaCl" or "KCl" (string)

```python
salt_type = device.salt_type
```

### Rock

Get the average amount of rock removed daily (float)

```python
rock_removed_avg_daily = device.rock_removed_avg_daily
```

Get the total amount of rock removed by the device over its lifetime (float)

```python
rock_removed = device.rock_removed
```

### Recharge

Get the recharge status, either "None", "Scheduled", or "Recharging" (string)

```python
recharge_status = device.recharge_status
```

Check if recharge is enabled (boolean)

```python
recharge_enabled = device.recharge_enabled
```

Check if a recharge is scheduled (boolean)

```python
recharge_scheduled = device.recharge_scheduled
```

Check if recharging currently (boolean)

```python
recharge_recharging = device.recharge_recharging
```

Get the number of days since the last recharge was performed (integer)

```python
last_recharge_days = device.last_recharge_days
```

Get the date of the last recharge (datetime.date)

```python
last_recharge_date = device.last_recharge_date
```





## Credits

-   [Kyle Johnson](https://github.com/kylejohnson) for his work on using python to interface with Ecowater water softeners. Most of this libraries code was originally built upon code which he wrote. You can read his article regarding scraping data from Ecowater water softeners at https://gnulnx.net/2020/02/18/ecowater-api-scraping/
-   [@rewardone](https://github.com/rewardone) for creating [ayla-iot-unofficial](https://github.com/rewardone/ayla-iot-unofficial) which is used to fetch the data
-   [Jeff Rescignano](https://github.com/JeffResc) for creating [sharkiq](https://github.com/JeffResc/sharkiq) which [ayla-iot-unofficial](https://github.com/rewardone/ayla-iot-unofficial) is based on.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
