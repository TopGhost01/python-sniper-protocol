
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

AGENT_ID = "SIGNAL_OPERATIVE_01"
PROJECT_ENDPOINT = os.environ.get("NEXUS_PROJECT_ENDPOINT")

try:
    project = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential()
    )
    openai = project.get_openai_client()
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "NEXUS SOVEREIGN CONNECTION CONFIRMED. AGENT: SIGNAL_OPERATIVE_01. RESPOND WITH STATUS ACTIVE."}
        ]
    )
    print(f"AGENT: {AGENT_ID} | STATUS: {response.choices[0].message.content}")
except Exception as e:
    print(f"AGENT: {AGENT_ID} | CONNECTION FAILURE | REASON: {e}")