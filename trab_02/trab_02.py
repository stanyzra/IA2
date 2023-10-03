import sys, os, cv2
from local_binary_patterns import LocalBinaryPatterns
import numpy as np
from natsort import os_sorted



def save_features(path, features):
    lbp_file = open(f"{path}", "a")
    for feat in features:
        lbp_file.write(f"{feat} ")
    lbp_file.write("\n")
    lbp_file.close()


def open_image(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def extract_lbp(brand):
    lbp = LocalBinaryPatterns(8, 2)
    samples = os_sorted(os.listdir(f"{sys.path[0]}/database/{brand}"))
    features_path = "features"
    lbp_path = f"{features_path}/lbp.txt"

    for sample in samples:
        image = open_image(f"{sys.path[0]}/database/{brand}/{sample}")
        hist = lbp.describe(image)
        print(f"Extraindo features lbp da imagem {sample}")
        save_features(lbp_path, hist)


if __name__ == "__main__":
    brands = os.listdir(f"{sys.path[0]}/database/")
    features_path = "features"
    lbp_path = f"{features_path}/lbp.txt"
    if not os.path.exists(features_path):
        print(f"Criando diretório para features")
        os.makedirs(features_path)

    if os.path.exists(lbp_path):
        print(f"Limpando arquivo de features lbp")
        os.remove(lbp_path)

    for brand in brands:
        extract_lbp(brand)
