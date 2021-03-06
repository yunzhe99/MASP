import numpy as np

from config import Config
from context_classification import context_classification_by_kmeans, context_cluster_by_hierarchy_cluster
from context_classification import get_features
from context_classification import context_cluster_by_dbscan

if __name__ == "__main__":

    # get_features(Config)

    img_features = np.load("img_features.npy")

    print(img_features.shape)

    cluster_phase1 = context_classification_by_kmeans(img_features)

    context_cluster_by_dbscan(cluster_phase1)
