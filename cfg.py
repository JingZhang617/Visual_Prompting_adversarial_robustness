import os

base_path = f"{os.getenv('HOME')}/workspace"

data_path = os.path.join(base_path, "data")
results_path = os.path.join(base_path, "results", "vp-for-adversarial-robustness")
