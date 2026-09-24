import requests
import json

# ☁️ THE CLOUD BRIDGE: Paste your secret Shuffle Cloud Webhook URL right between the quotes!
CLOUD_WEBHOOK_URL = "https://shuffler.io/api"


print("🛰️ [SOC AUTOMATION] Injecting live local telemetry stream outbound to Shuffle Cloud...\n")

# Simulate a real-world critical log matching your Phase 2 nested dictionary matrices
mock_threat_payload = {
    "_source": {
        "agent": {
            "name": "JAM-Windows-Endpoint", 
            "id": "007", 
            "ip": "192.168.1.45"
        },
        "manager": {
            "name": "kali-control-node"
        },
        "location": "vulnerability-detector",
        "vulnerability": {
            "severity": "Critical",
            "cve": "CVE-2026-9999",
            "title": "Cloud Pipeline Webhook Verification Handshake Successful!"
        }
    }
}

headers_config = {"Content-Type": "application/json"}

try:
    # Execute a secure outbound HTTP POST transaction across the live public internet over Port 443
    response = requests.post(CLOUD_WEBHOOK_URL, json=mock_threat_payload)
    
    if response.status_code == 200 or response.status_code == 202:
        print("✅ SUCCESS: Data packet successfully bypassed local hardware RAM limits!")
        print("Telemetry has been safely captured by Shuffle Cloud's remote nodes.")
    else:
        print(f"❌ CLOUD ERROR: Transmission rejected by remote gateway. HTTP Status: {response.status_code}")
        print(f"Details from server: {response.text}")
except Exception as net_err:
    print(f"❌ TRANSPORT EXCEPTION: Failed to reach public cloud endpoint. Details: {net_err}")
