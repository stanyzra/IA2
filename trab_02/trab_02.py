import sys, os, cv2
from local_binary_patterns import LocalBinaryPatterns
import numpy as np
from natsort import os_sorted
import subprocess
from sklearn.model_selection import StratifiedKFold
from classify import *
from get_result import *


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


def save_in_libsvm_format(path, features, labels):
    libsvm_file = open(f"{path}", "w")
    for i, feat in np.ndenumerate(features):
        # print(i)
        if i[1] == 0:
            libsvm_file.write(f"{labels[i[0]] + 1} ")
        libsvm_file.write(f"{i[1] + 1}:{feat} ")
        if i[1] == features.shape[1] - 1:
            libsvm_file.write("\n")
    libsvm_file.close()


def cross_validation(
    features,
    n_folds,
    n_features,
    save_output=False,
    output_path="",
    output_name="",
    clf=None,
):
    labels = np.repeat(np.arange(n_features, dtype=np.int32), n_folds)

    skf = StratifiedKFold(n_splits=10)
    skf.get_n_splits(features, labels)

    for i, (train_index, test_index) in enumerate(skf.split(features, labels)):
        print(f"Salvando treino e teste de Fold {i + 1}:")
        # print(f"  Train: index={train_index}")
        # print(f"  Test:  index={test_index}")

        X_train, X_test = features[train_index], features[test_index]
        y_train, y_test = labels[train_index], labels[test_index]

        if save_output == True:
            save_in_libsvm_format(
                f"{output_path}/{output_name}_train-{i + 1}.txt", X_train, y_train
            )
            save_in_libsvm_format(
                f"{output_path}/{output_name}_test-{i + 1}.txt", X_test, y_test
            )

        if clf == "rf":
            print(
                f"Score do Fold {i + 1}: {random_forest_classify(X_train, X_test, y_train, y_test)}"
            )


def read_features(path):
    original_features_file = open(f"{sys.path[0]}/{path}", "r")
    original_features = [
        i[:-1].split(" ") for i in original_features_file.read().splitlines()
    ]
    original_features = np.array(original_features, dtype=np.float32)
    original_features_file.close()
    return original_features


def format_libsvm_data(
    output_path="libsvm_features", features_path="features/lbp.txt", descriptor="lbp"
):
    if not os.path.exists(f"{output_path}/{descriptor}"):
        print(f"Criando diretório {output_path}/{descriptor}")
        os.makedirs(f"{output_path}/{descriptor}")

    features = read_features(features_path)

    cross_validation(features, 80, 50, True, f"{output_path}/{descriptor}", "lbp")


def menu():
    user_option = 0
    brands = os.listdir(f"{sys.path[0]}/database/")
    features_path = "features"
    lbp_path = f"{features_path}/lbp.txt"

    while user_option != -1:
        print("Sistema de predição de marca de carro")
        print("1 - Reduzir e normalizar tamanho da base de dados")
        print("2 - Extrair features com LBP")
        print("3 - Formatar dados para o LIBSVM com cross-validation")
        print("4 - Classificar dados com o LIBSVM")
        print("5 - Classificar dados com o Random Forest utilizando cross-validation")
        print("6 - Calcular resultados")
        print("7 - Sair")

        user_option = int(input("\nDigite a opção desejada: "))

        match user_option:
            case 1:
                print("\nReduzindo e normalizando tamanho da base de dados...")
                subprocess.run(["python", "reduce_database.py"])
            case 2:
                print("Extraindo features com LBP...")
                if not os.path.exists(features_path):
                    print(f"Criando diretório para features")
                    os.makedirs(features_path)

                if os.path.exists(lbp_path):
                    print(f"Limpando arquivo de features lbp")
                    os.remove(lbp_path)

                for brand in brands:
                    extract_lbp(brand)
            case 3:
                print("Formatando dados para o LIBSVM (cross-validation)")
                format_libsvm_data()
            case 4:
                print("Classificando dados com o LIBSVM")
                libsvm_classify()
            case 5:
                print("Classificando dados com o Random Forest (cross-validation)")
                features = read_features("features/lbp.txt")
                cross_validation(
                    features,
                    80,
                    50,
                    False,
                    clf="rf",
                )
            case 6:
                file_path = input("\nDigite o caminho do arquivo de resultados: ")
                if not os.path.isfile(file_path):
                    print("Arquivo não encontrado")
                else: 
                    calculate_result(file_path)
            case 7:
                exit()
            case _:
                print("Opção inválida\n")


if __name__ == "__main__":
    menu()
