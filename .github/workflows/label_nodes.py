import sys

# Define the list of labels
label_keywords = {
    "3D": "3D",
    "Channel": "Channel",
    "Deep": "Deep",
    "Filter": "Filter",
    "Grading or color": "Grading or color",
    "helper": "helper",
    "Image": "Image",
    "Keyer": "Keyer",
    "Merge": "Merge",
    "MetaData": "MetaData",
    "Other": "Other",
    "Particles": "Particles",
    "Time": "Time",
    "Transform": "Transform"
}

def label_node(node_label):
    """
    Function to match node_label with the predefined list of labels
    and return the appropriate label to apply.
    """
    for keyword, label in label_keywords.items():
        if keyword.lower() in node_label.lower():
            return label
    return "Uncategorized"  # If no match is found

# Assuming the node label is passed as a command-line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python label_nodes.py <node_label>")
        sys.exit(1)

    node_label = sys.argv[1]
    result = label_node(node_label)
    print(f"Node Label: {node_label} -> Applied Label: {result}")
