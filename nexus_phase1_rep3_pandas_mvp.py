# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Pandas MVP locked cold — CSV reading, inspection, missing value handling, cleaning, filtering — two-function sovereign pipeline





import pandas as pd

AGENT_ID = "SIGNAL_OPERATIVE_01"
LOG_FILE = "nexus_node_logs.csv"
PRIORITY_FILTER = "URGENT"

def inspect_node_logs(filename):
    df = pd.read_csv(filename)
    print(f"SHAPE: {df.shape}")
    print(df.head())
    print(df.dtypes)
    print(f"NULL COUNT:\n{df.isnull().sum()}")
    df_clean = df.dropna()
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.reset_index(drop=True)
    return df_clean

def filter_urgent_nodes(df, priority=PRIORITY_FILTER):
    urgent = df[df["priority"] == priority]
    print(f"URGENT NODES CONFIRMED: {AGENT_ID} | COUNT: {len(urgent)}")
    return urgent

df_clean = inspect_node_logs(LOG_FILE)
urgent_nodes = filter_urgent_nodes(df_clean)
print(df_clean)
print(urgent_nodes)
