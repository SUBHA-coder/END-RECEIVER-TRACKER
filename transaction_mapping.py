import networkx as nx

def create_transaction_graph(df):
    """Creates a directed graph from the transaction data."""
    G = nx.DiGraph()
    
    # Add edges from the transaction data
    for index, row in df.iterrows():
        G.add_edge(row['from_address'], row['to_address'], value=row['value'], label=row['Label'])
    
    return G

# Example usage
if __name__ == "__main__":
    from data_preprocessing import load_data
    
    df = load_data('ETHlabel.csv')
    G = create_transaction_graph(df)
    print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
