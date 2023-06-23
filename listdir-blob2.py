# listdir-blob2.py
# Usage: python listdir-blob2.py [container] [dir]
import sys, os 
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, __version__
from dotenv import load_dotenv
try:
    arg = sys.argv[1]
    cpath = arg
    opath = sys.argv[2]
except IndexError:
    if len(sys.argv) > 3:
        raise SystemExit(f"Usage: [sys.argv[0]] [container] [dir]")
    else:
        opath = ""
 
try:
    print("Azure Blob Storage v" + __version__)
# Authenticate using the Azure AD credentials:
    if ( os.environ['ENVIRONMENT'] == 'development'):
        load_dotenv(".env")
    token_credential = DefaultAzureCredential()
# Get the name of the container to list:
    container_name = cpath
    prefix = opath
# Initialize blob client
    blob_service_client = BlobServiceClient("https://webaaqmd5870.blob.core.windows.net/", token_credential)
    container_client = blob_service_client.get_container_client(container_name)
    blob_list = container_client.list_blobs(name_starts_with=prefix)
    for blob in blob_list:
        print(blob.name, blob.size) 
except NameError:
    raise SystemExit(f"Usage: [sys.argv[0]] [container] [dir]")
