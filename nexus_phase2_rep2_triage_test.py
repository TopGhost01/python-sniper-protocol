import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

AGENT_ID = "SIGNAL_OPERATIVE_01"
PROJECT_ENDPOINT = os.environ.get("NEXUS_PROJECT_ENDPOINT")

AMBIGUOUS_INSTRUCTION = "Process the relay data and update accordingly."

try:
    project = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential()
    )
    openai = project.get_openai_client()
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are NEXUS SOVEREIGN RELAY. Apply triage protocol to all incoming instructions."},
            {"role": "user", "content": AMBIGUOUS_INSTRUCTION}
        ]
    )
    print(f"AGENT: {AGENT_ID} | TRIAGE RESPONSE: {response.choices[0].message.content}")
except Exception as e:
    print(f"AGENT: {AGENT_ID} | CONNECTION FAILURE | REASON: {e}")