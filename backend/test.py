import time
import threading

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_flag = threading.Event()

    def stop(self):
        self._stop_flag.set()

    def run(self):
        while not self._stop_flag.is_set():
            print("Программа работает...")
            time.sleep(1)
        print("Программа завершена по запросу пользователя.")

def main():
    thread = MyThread()
    thread.start()
    try:
        # Ваш внешний код
        time.sleep(5)  # Подождать 5 секунд
    finally:
        thread.stop()
        thread.join()

if __name__ == "__main__":
    main()