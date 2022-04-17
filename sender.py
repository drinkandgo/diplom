import asyncio
import ssl
import sys
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_userpass]
   nc = NATS()
   future = asyncio.Future()
   #ssl_ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=r"C:\Users\kurmaev.arseny\PycharmProjects\pythonProject\ca.pem")
   #ssl_ctx.load_verify_locations(cafile=r"C:\Users\kurmaev.arseny\PycharmProjects\pythonProject\ca.pem")

   async def cb(msg):
      nonlocal future
      future.set_result(msg)

#connecting
   await nc.connect(servers=["nats://demo.nats.io:4222"], tls=ssl_ctx)

#subscribing
   await nc.publish("dc.notify.76fb136d-44ba-44bc-8c5e-adec00c149c1", cb=cb)
   msg = await asyncio.wait_for(future, 100)









   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()

print(message)