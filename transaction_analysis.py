def trace_transactions(G, start_address):
    """Traces the transaction trail starting from the given address."""
    path = []
    current_address = start_address
    
    # Follow the transaction trail
    while True:
        successors = list(G.successors(current_address))
        if not successors:
            print(f"No further transactions from {current_address}")
            break
        next_address = successors[0]  # Follow the first trail
        
        # Check if an edge exists
        if not G.has_edge(current_address, next_address):
            print(f"No edge between {current_address} and {next_address}")
            break
        
        path.append(next_address)
        current_address = next_address
    
    return path

def detect_mixer_addresses(G, threshold=5, amount=0.01):
    """Detects potential mixer addresses sending small amounts to many addresses."""
    potential_mixers = []
    for node in G.nodes:
        successors = list(G.successors(node))
        small_transactions = [succ for succ in successors if G.edges[node, succ]['value'] < amount]
        if len(small_transactions) > threshold:
            potential_mixers.append(node)
    
    return potential_mixers
