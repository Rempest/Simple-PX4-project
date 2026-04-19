import asyncio
from mavsdk import System
async def take_picture(drone):
  try:
    print("Taking a photo...")
    await drone.camera.take_photo()
    print("Photo is taken")
    
    
  
