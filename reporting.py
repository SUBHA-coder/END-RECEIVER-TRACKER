import pandas as pd

def generate_report(G, trail, output_file='suspicious_trail_report.csv'):
    """Generates a CSV report of the suspicious transaction trail."""
    if len(trail) < 2:
        print("Insufficient trail data to generate a report.")
        return
    
    report_data = []
    
    for i in range(len(trail) - 1):
        from_addr = trail[i]
        to_addr = trail[i + 1]
        edge_data = G.get_edge_data(from_addr, to_addr)
        
        # Check if the edge exists before appending to report
        if edge_data:
            report_data.append({
                'from_address': from_addr,
                'to_address': to_addr,
                'value': edge_data['value'],
                'label': edge_data['label']
            })
        else:
            print(f"No edge data found between {from_addr} and {to_addr}")
    
    if report_data:
        report_df = pd.DataFrame(report_data)
        report_df.to_csv(output_file, index=False)
        print(f"Report generated: {output_file}")
    else:
        print("No valid data to write to the report.")
