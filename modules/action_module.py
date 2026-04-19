import asyncio
from mavsdk import System
async def arm_and_takeoff(drone, altitude):
  print("Arming...")
  await drone.action.arm()
  await drone.action.set_takeoff_altitude(altitude)
  print("Taking off...")
  await drone.action.takeoff()
  
