import matplotlib.pyplot as plt
import networkx as nx
from transaction_analysis import trace_transactions  # Add this import
from interactive_visualization import interactive_visualization  # For interactive plotting
from heatmap import generate_heatmap  # For heatmap generation
from transaction_mapping import create_transaction_graph
from data_preprocessing import load_data

def visualize_transactions(G, start_address):
    """Visualizes the transaction trail from the start address."""
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    
    # Highlight the trail
    trail = trace_transactions(G, start_address)  # Use the imported function
    edges = [(start_address, trail[0])] + [(trail[i], trail[i + 1]) for i in range(len(trail) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12)
    
    plt.title(f"Transaction Trail from {start_address}")
    plt.show()

def run_interactive_visualization(G, start_address):
    """Runs the interactive visualization."""
    interactive_visualization(G, start_address)

def generate_transaction_heatmap(df):
    """Generates a heatmap for the transactions."""
    generate_heatmap(df)

# Example usage
if __name__ == "__main__":
    df = load_data('ETHlabel.csv')
    G = create_transaction_graph(df)
    
    suspicious_address = '0x82cd9d14ea80ab17d81df310e8a42bdd9bbebcdf'
    
    # Static visualization
    visualize_transactions(G, suspicious_address)
    
    # Interactive visualization
    run_interactive_visualization(G, suspicious_address)
    
    # Generate heatmap of transaction activity
    generate_transaction_heatmap(df)
