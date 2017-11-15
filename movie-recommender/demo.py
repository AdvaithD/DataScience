# Recommendation systems - They go through all of our options, learn what we like and recommend what we like best

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# Fetch data
data = fetch_movielens(min_rating = 4.0)


print(repr(data['train']))
print(repr(data['test']))


model = LightFM(loss = 'warp')
# Warp is content and collaborative = hybrid system

model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape
