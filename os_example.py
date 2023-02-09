import os
import time

start_t = time.time()
os.system("sleep 1s;echo Hello Python")

end_t = time.time()

print(f"Program Runtime:{end_t-start_t:.4f}s")
