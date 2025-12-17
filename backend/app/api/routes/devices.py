from fastapi import APIRouter
from app.services import device_registry

router = APIRouter(prefix="/devices", tags=["devices"])

@router.get("/")
def list_devices():
    return [
        {
            "device_id": d.device_id,
            "status": d.status,
            "last_seen": d.last_seen
        }
        for d in device_registry.all()
    ]

@router.post("/{device_id}/heartbeat")
def heartbeat(device_id: str):
    device = device_registry.get(device_id)
    device.mark_online()
    return {
        "device_id": device.device_id,
        "status": device.status,
        "last_seen": device.last_seen
    }