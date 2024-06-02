import objaverse
import objaverse.xl as oxl
import matplotlib.pyplot as plt
import numpy as np
objaverse.__version__


annotations = oxl.get_annotations(
    download_dir="~/.objaverse" # default download directory
)
lvis_annotations = objaverse.load_lvis_annotations()
num_per_category = np.array([len(x) for x in lvis_annotations.values()])
num_per_category.sort()
#plt.figure()
#plt.bar(np.arange(len(num_per_category)), height=num_per_category)
#plt.show()


sources = annotations["source"].value_counts()

# sample a single object from each source
sampled_df = annotations.groupby('source').apply(lambda x: x.sample(1)).reset_index(drop=True)
thingiverse = sampled_df[sampled_df['source'] == 'thingiverse']
thingiverse['metadata']
