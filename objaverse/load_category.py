import objaverse
import objaverse.xl as oxl
import numpy as np
from objaverse import utils


uids = objaverse.load_uids()
annotations = objaverse.load_annotations(uids[:10])

lvis_annotations = objaverse.load_lvis_annotations()
ids = lvis_annotations["chair"]
annotations = objaverse.load_annotations(ids[:10])



annotations = oxl.get_annotations(
    download_dir="~/.objaverse" # default download directory
)


#plt.figure()
#plt.bar(np.arange(len(num_per_category)), height=num_per_category)
#plt.show()


#sources = annotations["source"].value_counts()

# sample a single object from each source
sampled_df = annotations.groupby('source').apply(lambda x: x.sample(1)).reset_index(drop=True)
num_per_category = np.array([len(x) for x in lvis_annotations.values()])
num_per_category.sort()
#thingiverse = sampled_df[sampled_df['source'] == 'thingiverse']
#thingiverse['metadata']
