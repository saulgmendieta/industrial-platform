from app.domain.device import Device

class DeviceRegistry:
    def __init__(self):
        self._devices: dict[str, Device] = {}

    def get(self, device_id: str) -> Device:
        if device_id not in self._devices:
            self._devices[device_id] = Device(device_id)
        return self._devices[device_id]

    def all(self):
        return list(self._devices.values())