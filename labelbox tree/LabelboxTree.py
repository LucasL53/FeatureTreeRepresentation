import json

# Load the JSON data from the file
with open('labelbox tree/label-tree.json', 'r') as file:
    data = json.load(file)

# Function to transform the JSON data
def transform_data(data):
    def process_tool(tool):
        node = {
            "name": tool["name"],   
            "children": []
        }
        for classification in tool["classifications"]:
            node["children"].append(process_classification(classification))
        return node

    def process_classification(classification):
        node = {
            "name": classification["name"],
            "children": []
        }
        for option in classification["options"]:
            node["children"].append(process_option(option))
        return node

    def process_option(option):
        node = {
            "name": option.get("value", ""),
            "children": []
        }
        for sub_option in option.get("options", []):
            node["children"].append(process_option(sub_option))
        return node

    return {
        "name": "Root",
        "children": [process_tool(tool) for tool in data["tools"]]
    }

transformed_data = transform_data(data)

# Save the transformed data to a file
with open('transformed_label_tree.json', 'w') as file:
    json.dump(transformed_data, file, indent=2)
