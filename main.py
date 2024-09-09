from data_preprocessing import load_data
from transaction_mapping import create_transaction_graph
from transaction_analysis import trace_transactions, detect_mixer_addresses
from visualization import visualize_transactions
from reporting import generate_report

def main():
    # Load data and create transaction graph
    df = load_data('ETHlabel.csv')
    G = create_transaction_graph(df)
    
    # Define a suspicious address for analysis
    suspicious_address = '0x82cd9d14ea80ab17d81df310e8a42bdd9bbebcdf'
    
    # Trace transactions
    trail = trace_transactions(G, suspicious_address)
    
    if not trail:
        print(f"No transaction trail found for {suspicious_address}")
    else:
        print("Transaction trail:", trail)
    
    # Detect mixer addresses
    mixers = detect_mixer_addresses(G)
    print("Potential mixer addresses:", mixers)
    
    # Visualize transactions
    visualize_transactions(G, suspicious_address)
    
    # Generate report
    generate_report(G, trail)

if __name__ == "__main__":
    main()
