# vmstop.py
# Stop AEDT vm
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from dotenv import load_dotenv
# AIM subscription
SUBSCRIPTION_ID="5861036e-2874-41db-b642-5735b9e010de"
try:
    load_dotenv(".vmenv")
    azure_credential=DefaultAzureCredential()
    resource_group="AEDT_group"
    # Initialize client with credential and subscription
    compute_client = ComputeManagementClient(
      azure_credential,
      SUBSCRIPTION_ID
    )
    print('\nStopping VM AEDT...')
    async_vm_stop= compute_client.virtual_machines.begin_power_off(
      resource_group,
      "AEDTVM"
    )
    async_vm_stop.wait()
    print('\nVM stoped')
except Exception as err:
    print(err)
