from tqdm.notebook import trange
from tqdm import tqdm
from time import sleep

with tqdm(total=100, desc='Processing') as process:
    for i in tqdm(range(100), desc = 'Progress Bar 2'):
        sleep(0.5)
        process.update(1)
    

