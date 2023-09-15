import numpy as np
import pandas as pd
from transformers import AutoTokenizer
from sklearn.cluster import KMeans
import warnings
import datachange as dc

warnings.filterwarnings("ignore")

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)

df = dc.text_to_df()

X = df[['word1', 'word2', 'word3', 'word4']]
y = df[['titles']]

print(X.head())
print(y.head())

max_seq_length = 4  # Adjust this based on the data
X_tokens = {
    col: [] for col in X.columns
}

for col in X.columns:
    X_tokens[col] = X[col].apply(lambda x: tokenizer.encode(x, add_special_tokens=False,
                                                            max_length = max_seq_length,
                                                            padding='max_length',
                                                            truncation=True))
X_tokens = pd.DataFrame(X_tokens)       
print(X_tokens)

merged_column = pd.concat([X_tokens['word1'], X_tokens['word2'], X_tokens['word3'], X_tokens['word4']], axis=0)
print(merged_column)

num_groups = 4
# Randomly select a number of rows and store them in a list
selected_rows = X_tokens.sample(num_groups).values.tolist()
print(selected_rows)

# Convert the list of selected rows into a NumPy array
selected_rows_array = np.array(selected_rows)
selected_rows_array = selected_rows_array.reshape((num_groups*4, num_groups))
print(selected_rows_array)

data = selected_rows_array

# Desired number of clusters and minimum number of samples in each cluster
desired_clusters = num_groups
min_samples_per_cluster = len(data) // desired_clusters

# Initialize variables
equal_clusters = False

while not equal_clusters:
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=desired_clusters, random_state=0)
    cluster_labels = kmeans.fit_predict(data)
    # print(cluster_labels)

    # Calculate the cluster sizes
    cluster_sizes = np.bincount(cluster_labels)

    # Check if all clusters have at least min_samples_per_cluster samples
    if all(size >= min_samples_per_cluster for size in cluster_sizes):
        equal_clusters = True
    else:
        # If not, adjust the cluster assignments
        for cluster_idx, size in enumerate(cluster_sizes):
            if size < min_samples_per_cluster:
                # Find the data points with this cluster assignment
                data_to_move = data[cluster_labels == cluster_idx]

                # Randomly select data points to move to other clusters
                new_cluster_assignments = np.random.choice(desired_clusters, size=len(data_to_move))
                cluster_labels[cluster_labels == cluster_idx] = new_cluster_assignments
                print(cluster_labels)

print(cluster_labels)