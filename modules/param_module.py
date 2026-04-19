import asyncio
from mavsdk import System
async def set_param(drone):
  print("Set param...")
  await drone.param.set_param_float(""MPC_XY_CRUISE", 5.0")
