import ollama
import os

# Paths to input and output files
input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' does not exist.")
    exit(1)

# Read the grocery list from the input file
with open(input_file, "r") as f:
    grocery_list = f.read().strip()

# Categorizethe grocery list using the Ollama API
prompt = f"""
You are an assistant that categorizes and sort grocery items. 
Here is the list:\n{grocery_list}\n\n 
Please :
    1. Categorize the items into appropriate categories like     Fruits, Vegetables, Dairy, Meat, Grains, Snacks, Beverages, etc...
    2. Sort the items alphabetically within each category.
    3. Present the categorized list in a clear and organized format.
"""

try:
    response = ollama.generate(model="llama3.2", prompt=prompt)
    categorized_list = response.get("response", "")
    print("= * 30")
    print("Categorized Grocery List:\n", categorized_list)
    print("= * 30")

    # Write the categorized list to the output file
    with open(output_file, "w") as f:
        f.write(categorized_list)

    print(f"Categorized grocery list has been written to '{output_file}'.")
except Exception as e:
    print(f"An error occurred: {e}")
