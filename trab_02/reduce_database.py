import sys, os


def get_sample_min_len(brands):
    samples_number = []
    for brand in brands:
        samples_number.append(len(os.listdir(f"{sys.path[0]}/database/{brand}")))
    return min(samples_number)


if __name__ == "__main__":
    brands = os.listdir(f"{sys.path[0]}/database/")

    max_sample_number = get_sample_min_len(brands)

    for brand in brands:
        samples = os.listdir(f"{sys.path[0]}/database/{brand}")
        if len(samples) > max_sample_number:
            for sample in samples[max_sample_number:]:
                os.remove(f"{sys.path[0]}/database/{brand}/{sample}")
