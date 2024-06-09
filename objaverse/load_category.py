import json
import os
import objaverse
import objaverse.xl as oxl
import numpy as np
from objaverse import utils
import requests
from concurrent.futures import ThreadPoolExecutor

"""
# the whole dataset
annotations = oxl.get_annotations(
    download_dir="~/.objaverse" # default download directory
)
annotations["source"].value_counts()

sketchfab_objects_annotations = annotations[annotations['source'] == 'sketchfab']
sketchfab_uids = sketchfab_objects_annotations['sha256']
sketchfab_fid = sketchfab_objects_annotations['fileIdentifier']
sketchfab_stripped_id = [os.path.basename(x) for x in sketchfab_fid]
"""

# objaverse 1.0
uids = objaverse.load_uids()
object_paths = objaverse._load_object_paths()
#uid_object_paths = [
#        f"https://huggingface.co/datasets/allenai/objaverse/resolve/main/{object_paths[uid]}"
#        for uid in uids
#    ]

lvis_annotations = objaverse.load_lvis_annotations()
lvis_paths = {}
for category in lvis_annotations.keys():
    lvis_paths[category] = [
        f"https://huggingface.co/datasets/allenai/objaverse/resolve/main/{object_paths[uid]}"
        for uid in lvis_annotations[category]
    ]

# download just the chair category
chair = lvis_paths["chair"]
base_dir = r"C:\Users\azmih\Desktop\Projects\objaverse-xl\data\lvis\chair"
os.makedirs(base_dir, exist_ok=True)


# Function to download a single file
def download_file(url, save_folder):
    local_filename = os.path.join(save_folder, os.path.basename(url))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


# Use ThreadPoolExecutor to download files concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(download_file, url, base_dir) for url in chair]
    for future in futures:
        try:
            print(f"Downloaded {future.result()}")
        except Exception as e:
            print(f"Error downloading file: {e}")


#for url in chair:
#    output_file = os.path.join(base_dir, os.path.basename(url))
#    os.system(f'wget {url} -O {output_file}')


#with open("input_models_path.json", "w") as f:
#    json.dump(lvis_paths, f, indent=2)
















#plt.figure()
#plt.bar(np.arange(len(num_per_category)), height=num_per_category)
#plt.show()


#sources = annotations["source"].value_counts()
#lvis_uids = objaverse.load_uids()
#lvis_annotations = objaverse.load_annotations(uids[:10])


# sample a single object from each source
#sampled_df = annotations.groupby('source').apply(lambda x: x.sample(1)).reset_index(drop=True)
#num_per_category = np.array([len(x) for x in lvis_annotations.values()])
#num_per_category.sort()
#thingiverse = sampled_df[sampled_df['source'] == 'thingiverse']
#thingiverse['metadata']
