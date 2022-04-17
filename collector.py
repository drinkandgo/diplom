import psutil
data_storage = {"DeviceId": "1"}
def collector():
    data_storage.update(cpu_load = psutil.cpu_percent())
    data_storage.update(mem_load = psutil.virtual_memory().percent)
    #data_storage.update(interface = psutil.net_connections(kind="inet4"))

collector()
print(data_storage)





print(a)