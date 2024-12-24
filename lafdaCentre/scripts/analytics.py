import pandas as pd

def perform_analytics():
    # Example: Analyze case status distribution
    df = pd.read_csv("lafdaCentre/data/cases.csv")
    print("Case Distribution:")
    print(df['status'].value_counts())

if __name__ == "__main__":
    perform_analytics()
