import ayla_iot_unofficial
import datetime

from .const import (
    APP_ID,
    APP_SECRET,
)

class EcowaterDevice(ayla_iot_unofficial.device.Device):
    # Device Info
    @property
    def ip_address(self) -> str:
        return self._device_ip_address

    @property
    def rssi(self) -> int:
        return self.get_property_value("rf_signal_strength_dbm")

    # Water
    
    @property
    def water_use_avg_daily(self) -> int:
        return self.get_property_value("avg_daily_use_gals")
    
    @property
    def water_use_today(self) -> int:
        return self.get_property_value("gallons_used_today")
    
    @property
    def water_available(self) -> int:
        return self.get_property_value("treated_water_avail_gals")
    
    # Water flow

    @property
    def current_water_flow(self) -> int:
        return self.get_property_value("current_water_flow_gpm")

    # Salt

    @property
    def salt_level_percentage(self) -> int:
        return self.get_property_value("salt_level_tenths") * 2
    
    @property
    def out_of_salt_days(self) -> int:
        return self.get_property_value("out_of_salt_estimate_days")
    
    @property
    def out_of_salt_date(self) -> datetime.date:
        return datetime.datetime.now().date() + datetime.timedelta(days = self.get_property_value("out_of_salt_estimate_days"))
    
    # Rock

    @property
    def rock_removed(self) -> int:
        return self.get_property_value("total_rock_removed_lbs")
    
    # Recharge

    @property
    def recharge_enabled(self) -> bool:
        return self.get_property_value("regen_enable_enum") == 1
    
    @property
    def recharge_scheduled(self) -> bool:
        return self.get_property_value("regen_status_enum") == 1

    @property
    def last_recharge_days(self) -> int:
        return self.get_property_value("days_since_last_regen")
    
    @property
    def last_recharge_date(self) -> datetime.date:
        return datetime.datetime.now().date() - datetime.timedelta(days = self.get_property_value("days_since_last_regen"))
    

class EcowaterAccount:
    def __init__(self, username: str, password: str) -> None:
        self.ayla_api = ayla_iot_unofficial.new_ayla_api(username, password, APP_ID, APP_SECRET)
        self.ayla_api.sign_in()

    def get_devices(self) -> list:
        devices = self.ayla_api.get_devices()

        # Filter for Ecowater devices
        devices = list(filter(lambda device: device._oem_model_number.startswith("EWS"), devices))

        # Convert devices to EcowaterDevice Class
        for device in devices:
            setattr(device, "__class__", EcowaterDevice)
            device.metric = False
            device.update()

        return devices