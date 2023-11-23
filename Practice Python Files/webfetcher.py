#complex code

import threading
import queue
import requests

class DataFetcher(threading.Thread):
    def __init__(self, url_queue, results_queue):
        threading.Thread.__init__(self)
        self.url_queue = url_queue
        self.results_queue = results_queue

    def run(self):
        while True:
            url = self.url_queue.get()
            if url is None:
                break
            response = requests.get(url)
            self.results_queue.put((url, response.status_code))
            self.url_queue.task_done()

def fetch_data_concurrently(urls, num_threads=5):
    url_queue = queue.Queue()
    results_queue = queue.Queue()

    # Start threads
    threads = [DataFetcher(url_queue, results_queue) for _ in range(num_threads)]
    for thread in threads:
        thread.start()

    # Enqueue URLs
    for url in urls:
        url_queue.put(url)

    # Stop workers
    for i in range(num_threads):
        url_queue.put(None)

    for thread in threads:
        thread.join()

    # Collect results
    while not results_queue.empty():
        url, status = results_queue.get()
        print(f"URL: {url}, Status Code: {status}")

# Example usage
urls = ["https://www.google.com", "https://www.wikipedia.org", "https://www.python.org"]
fetch_data_concurrently(urls)
