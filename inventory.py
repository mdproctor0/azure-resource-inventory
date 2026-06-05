from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import csv
import datetime

# Azure subscription ID
subscription_id = 'fd521475-76a6-479b-8f2e-73fe1b53d026'

def main():
    # Authenticate with Azure
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)
    print("Connecting to Azure and collecting resource inventory...")

    # Get the list of resource groups
    resource_groups = resource_client.resource_groups.list()

    # Prepare data for CSV
    inventory_data = []
    for rg in resource_groups:
        print(f"Scanning: {rg.name}")
        resources = resource_client.resources.list_by_resource_group(rg.name)
        for resource in resources:
            inventory_data.append({
                "resource_group": rg.name,
                "name": resource.name,
                "type": resource.type,
                "location": resource.location,
                "tags": resource.tags
            })

    # Write data to CSV
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"azure_inventory_lab_{timestamp}.csv"

    with open(filename, mode='w', newline="") as csv_file:
        fieldnames = ['resource_group', 'name', 'type', 'location', 'tags']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory_data)

    print(f"Inventory has been saved to {filename}")
    

if __name__ == "__main__":
    main()




