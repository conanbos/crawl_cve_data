import time

from tqdm import trange

def pbar(counter):
    for i in trange(counter):
        time.sleep(1)