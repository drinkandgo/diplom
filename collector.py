import datetime

import psutil
import time



DeviceId = 1
data_storage = {"DeviceId": str(DeviceId)}
def collector():
    data_storage.update(cpu_load = psutil.cpu_percent())
    data_storage.update(mem_load = psutil.virtual_memory().percent)
    data_storage.update(timestamp = datetime.datetime.now().isoformat())


collector()
print(data_storage)





