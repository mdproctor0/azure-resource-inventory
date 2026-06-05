# Azure Resource Inventory — Python + Azure SDK

**Deployed and validated against a live Azure subscription**  
**Built:** June 2026  
**Tools:** Python 3.11 · Azure SDK · Microsoft Graph · Azure CLI

---

## What This Does

A Python script that connects to Azure using the Azure SDK, inventories every resource across all resource groups in a subscription, and exports a timestamped CSV report. Built to solve a real operational problem — you can't manage what you can't see.

**Real finding from running this script:** Multiple resources discovered with empty or missing tags — a compliance and cost tracking gap that would generate remediation tickets in a production environment.

---

## What It Reports

| Field | Source | Value |
|-------|--------|-------|
| resource_group | Azure Resource Manager | Resource group name |
| name | Azure Resource Manager | Resource name |
| type | Azure Resource Manager | Resource type (e.g. Microsoft.Storage/storageAccounts) |
| location | Azure Resource Manager | Azure region |
| tags | Azure Resource Manager | Key-value tags or empty |

---

## Sample Output

```
Connecting to Azure and collecting resource inventory...
Scanning: rg-cloud-resume
Scanning: DefaultResourceGroup-EUS
Scanning: proctor-resume-api_group
Scanning: rg-secure-storage-lab
Inventory has been saved to azure_inventory_lab_20260603_160532.csv
```

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/mdproctor0/azure-resource-inventory.git
cd azure-resource-inventory

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Authenticate to Azure
az login

# Run the script
python3 inventory.py
```

---

## Project Structure

```
azure-resource-inventory/
├── inventory.py          # Main script
├── requirements.txt      # Python dependencies
├── .gitignore            # Excludes venv, CSV output, cache
└── README.md
```

---

## Key Concepts Demonstrated

- **DefaultAzureCredential** — automatically finds Azure CLI credentials, managed identity, or environment variables. No hardcoded secrets.
- **ResourceManagementClient** — Azure SDK client for Resource Manager API. Lists resource groups and resources without manual HTTP calls.
- **Virtual environment** — isolated Python dependencies, not installed globally
- **CSV export with timestamp** — machine-readable output for downstream reporting, dashboards, or ticketing systems
- **Real security finding surfaced** — untagged resources identified across the subscription. In production this feeds a remediation workflow.

---

## Production Use Cases

- **Capacity planning** — point-in-time snapshot of all resources and sizes
- **Compliance reporting** — evidence of what exists for auditors
- **Tagging audit** — identify resources missing required tags before a policy enforcement deadline
- **Onboarding** — new team member runs this on day one to understand the environment

---

## Related Projects

- [M365 Cloud Engineering Labs](https://github.com/mdproctor0/m365-cloud-engineering-labs)
- [Secure Azure Foundation — Terraform](https://github.com/mdproctor0/secure-azure-foundation-terraform)
- [Azure Secure Storage — Terraform](https://github.com/mdproctor0/azure-secure-storage)
