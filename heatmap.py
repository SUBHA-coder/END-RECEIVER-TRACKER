import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_heatmap(transaction_data):
    # Create a DataFrame with transaction counts for each address
    address_counts = transaction_data['to_address'].value_counts().reset_index()
    address_counts.columns = ['Address', 'Transaction Count']
    
    # Create a heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(
        address_counts[['Transaction Count']].transpose(),
        cmap="YlGnBu",
        cbar=True,
        annot=True,
        fmt='d',
        linewidths=0.5
    )
    plt.title("Heatmap of Most Active Addresses")
    plt.xlabel("Addresses")
    plt.ylabel("Transaction Activity")
    plt.show()
