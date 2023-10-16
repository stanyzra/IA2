import numpy as np
import sys, os, cv2

if __name__ == "__main__":
    database_path = f"{sys.path[0]}/database/"
    brands = os.listdir(database_path)
    samples = []
    for i, brand in enumerate(brands):
        samples.append(len(os.listdir(f"{database_path}/{brand}")))

    samples = np.array(samples)
    print(np.sum(samples))
