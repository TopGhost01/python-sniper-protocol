

import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

AGENT_ID = "MARITIME_SENTINEL_01"
AGENT_INSTRUCTIONS = "You are a sovereign maritime threat classification operative. Classify incoming sensor transmissions as CLEAR, MONITOR, or INTERCEPT. State your classification and routing decision."
THREAD_TRANSMISSION = "VESSEL_07 :: SECTOR_DELTA :: UNIDENTIFIED_CONTACT_BEARING_270 :: CLOSING_SPEED_18_KNOTS"
PROJECT_ENDPOINT = os.environ.get("NEXUS_PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = "gpt-4.1-mini"

try:
    project = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential()
    )

    with project.get_openai_client() as openai_client:
        response = openai_client.responses.create(
            model=MODEL_DEPLOYMENT,
            instructions=AGENT_INSTRUCTIONS,
            input=THREAD_TRANSMISSION,
        )
        print(f"AGENT: {AGENT_ID} | {response.output_text}")

except Exception as e:
    print(f"FAILURE: {AGENT_ID} | TRANSMISSION: {THREAD_TRANSMISSION} | REASON: {e}")