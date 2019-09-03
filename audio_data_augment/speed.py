import os
import subprocess
from tqdm import trange
import shutil

input_dir = "wavs/"
output_dir = "wavs_8k/"

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

os.mkdir(output_dir)


filenames = os.listdir(input_dir)
print(len(filenames))


def audio(in_path,out_path):
    """
    -r : sample rate
    -b : bit
    -c: channel
    tempo : speed 
    """
    cmd = "sox {} -r 8000 -b 16 -c 1 {} tempo 0.95".format(in_path,out_path)
    subprocess.call(cmd,shell=True)

for i in trange(len(filenames)):
    input_path = input_dir + filenames[i]
    output_path = output_dir + filenames[i]
    audio(input_path,output_path)
