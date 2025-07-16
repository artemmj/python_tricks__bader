import time


class TimeMeter:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Затраченое время: {time.time() - self.start_time}")


with TimeMeter() as tm:
    time.sleep(2.2)
