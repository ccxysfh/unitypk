import os

import pandas as pd

data_dir_path = "/data/datasets/frames_temp"
file_path = os.path.join(data_dir_path, "particles_1.csv")

if __name__ == '__main__':
    """
    100 methods for data preprocess
    """
    frame_particle = pd.read_csv(file_path)
    frame_particle.tail(5)
