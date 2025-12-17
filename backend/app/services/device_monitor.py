import asyncio
from datetime import datetime, timedelta

from app.services import device_registry
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

async def monitor_devices():
    timeout = timedelta(seconds=settings.DEVICE_OFFLINE_TIMEOUT_SECONDS)

    while True:
        now = datetime.utcnow()

        for device in device_registry.all():
            if (
                device.last_seen
                and device.status == "online"
                and now - device.last_seen > timeout
            ):
                device.mark_offline()
                logger.info(
                    "Device %s marked OFFLINE (timeout)",
                    device.device_id
                )

        await asyncio.sleep(5)