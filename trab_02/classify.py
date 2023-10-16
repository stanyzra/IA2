import sys, os
import subprocess
from natsort import os_sorted
from sklearn.ensemble import RandomForestClassifier


def scale_data(path):
    print("\nScaling data...")
    # subprocess.run(["./svm-scale", "-l", "-1", "-u", "1", "-s", "range", "libsvm_features/lbp/train.txt", ">", "libsvm_features/lbp/train_scaled.txt"], cwd=libsvm_root_path)
    # subprocess.run(
    #     [
    #         "./svm-scale",
    #         "-l",
    #         "-1",
    #         "-u",
    #         "1",
    #         "-s",
    #         "range",
    #     ],
    #     cwd=path,
    # )


def use_easy_py_libsvm(train_path, test_path, libsvm_root_path):
    print("\nUsing easy.py libsvm...")
    # os.chdir(f"{libsvm_root_path}/tools/")
    subprocess.run(
        [
            "python",
            "easy.py",
            train_path,
            test_path,
        ],
        cwd=f"{libsvm_root_path}/tools/",
    )


def libsvm_classify():
    libsvm_root_path = f"{sys.path[0]}/libsvm-3.32"
    features_path = f"{sys.path[0]}/libsvm_features/lbp"

    for i, file_name in enumerate(os_sorted(os.listdir(features_path))):
        if i == 10:
            break
        descriptor = file_name.split("_")[0]
        train_path = f"{features_path}/{descriptor}_train-{i + 1}.txt"
        test_path = f"{features_path}/{descriptor}_test-{i + 1}.txt"

        print(f"train_path: {train_path} | test_path: {test_path}")

        use_easy_py_libsvm(train_path, test_path, libsvm_root_path)

    scale_data(libsvm_root_path)


def random_forest_classify(X_train, X_test, y_train, y_test):
    print("\nUsing random forest...")
    clf = RandomForestClassifier(n_estimators=2000, criterion="entropy", n_jobs=-1)
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)
