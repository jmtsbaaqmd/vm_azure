# vmstatus.py
# Checks status of AEDT vm
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from dotenv import load_dotenv
# AIM subscription
SUBSCRIPTION_ID="5861036e-2874-41db-b642-5735b9e010de"
try:
    load_dotenv(".vmenv")
    azure_credential=DefaultAzureCredential()
    resource_group="AEDT_group"
    #Initialize client with credential and subscription.
    compute_client = ComputeManagementClient(
      azure_credential,
      SUBSCRIPTION_ID
    )
    print('\nChecking VM ' + 'AEDT')
    vm_state = compute_client.virtual_machines.instance_view(
       resource_group,
        "AEDTVM"
    )
    power_state=vm_state.statuses[1].code
    print('\n')
    print(power_state)
    if power_state == 'PowerState/running':
        print("VM is up")
    else:
        print("VM is down")
except Exception as err:
    print(err)
