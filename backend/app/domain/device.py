from datetime import datetime
from enum import Enum

class DeviceStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"

class Device:
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.status: DeviceStatus = DeviceStatus.UNKNOWN
        self.last_seen: datetime | None = None

    def mark_online(self):
        self.status = DeviceStatus.ONLINE
        self.last_seen = datetime.utcnow()

    def mark_offline(self):
        self.status = DeviceStatus.OFFLINE