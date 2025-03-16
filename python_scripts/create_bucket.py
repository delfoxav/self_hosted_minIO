
# Import the required libraries
from minio import Minio
from minio.error import S3Error
from sklearn.datasets import load_iris
import pandas as pd
import os

# --- Replace with your own MinIO server and credentials ---
MINIO_URL = "your_minio_url:port"
ACCESS_KEY = "your_access_key"
SECRET_KEY = "your_secret_key"


# create a MinIO client with the MinIO server information
client = Minio(MINIO_URL,
               access_key=ACCESS_KEY,
               secret_key=SECRET_KEY,
                   secure=False  # Set to False if not using SSL
)

# Create bucket.
client.make_bucket("toybucket")

# Load the Iris dataset
iris = load_iris()

# Convert it to a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Save the DataFrame as a CSV file
df.to_csv('iris_dataset.csv', index=False)

# File to upload
file_path = "iris_dataset.csv"  # Path to the dataset file you created
bucket_name = "toybucket"  
object_name = "iris_dataset.csv"  # The name to give the file in the bucket

# Upload the file to the MinIO bucket
try:
    client.fput_object(bucket_name, object_name, file_path)
    print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
except S3Error as e:
    print(f"Error: {e}")

# delete the file
os.remove(file_path)