# formate
import time
local = time.localtime()
print(local)
print(f"time is : {time.strftime( "%Y-%m-%d %H:%M:%S",local)}")
# print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))

# calculate the execuation time of any function
start = time.time()
for i in range(500000):
    pass
end = time.time()
print(start-end)