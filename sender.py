import asyncio
import ssl
import sys
from nats.aio.client import Client as NATS
import json
import collector

async def send_monitoring_data():

   # [begin connect_userpass]
   nc = NATS()
   future = asyncio.Future()
   #ssl_ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=r"C:\Users\kurmaev.arseny\PycharmProjects\pythonProject\ca.pem")
   #ssl_ctx.load_verify_locations(cafile=r"C:\Users\kurmaev.arseny\PycharmProjects\pythonProject\ca.pem")

   async def cb(msg):
      nonlocal future
      future.set_result(msg)

#connecting
   await nc.connect(servers=["nats://demo.nats.io:4222"], #tls=ssl_ctx
                     )

#subscribing
   await nc.publish("updates", json.dumps(collector.data_storage).encode())
   collector.data_storage.clear()










   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()

print(message)