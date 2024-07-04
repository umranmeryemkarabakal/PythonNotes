import time
import requests
import threading

class ThreadingDownloader(threading.Thread):
    json_array = []

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        #threading başlatıldığında yapılacak işler buraya yazılır
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array
    
def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start() #satır okunduğunda run fonksiyonu çalışır
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    et = time.time()
    elapsed_time = et-st
    print("execution time: ",elapsed_time,"seconds")

urls = ["https://postman-echo.com/delay/3"]*10
get_data_threading(urls)