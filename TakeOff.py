import asyncio
from mavsdk import System

class Drone:
    async def run(self):
        drone = System()

        print("Connecting to drone...")
        await drone.connect(system_address="udp://:14540")

        print("Waiting for connection...")
        async for state in drone.core.connection_state():
            if state.is_connected:
                print("Drone connected!")
                break

        print("Waiting for GPS...")
        async for health in drone.telemetry.health():
            if health.is_global_position_ok:
                print("GPS ready!")
                break

        print("Arming...")
        await drone.action.arm()

        print("Takeoff...")
        await drone.action.takeoff()

        print("Flying 5 seconds...")
        await asyncio.sleep(5)

        print("Landing...")
        await drone.action.land()


async def main():
    green_sky = Drone()
    await green_sky.run()

asyncio.run(main())
