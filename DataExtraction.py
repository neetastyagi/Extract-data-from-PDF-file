!pip install openai pymupdf
!pip install openai==0.28
!pip install openai pymupdf pandas xlwt
import openai
import fitz  # PyMuPDF
import pandas as pd
import json

# Set your OpenAI API key
openai.api_key = "..."

# Step 1: Extract text from the PDF
def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Step 2: Generate a structured prompt for OpenAI
def create_prompt(pdf_text):
    prompt = f"""
Extract the product price list data below into the following JSON structure:

{{
  "Item": "Beets, Red",
  "Case Size": "bag",
  "Quantity per Case": 25,
  "Price per case": "$40",
  "Wholesale Quantity": "20+ Cases",
  "Wholesale Price": "$35",
  "UOM": "lb",
  "Less Than Case Price": "$3/lb",
  "Quantity Available": 40
}}

ONLY return a JSON array, no extra explanation.

Data:
{pdf_text}
"""
    return prompt

# Step 3: Use OpenAI to extract structured JSON from the prompt
def get_json_from_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message['content']

# Step 4: Convert JSON to Excel
def save_json_to_excel(json_text, output_file):
    try:
        data = json.loads(json_text)
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False, engine="openpyxl")
        print(f"Excel file saved to: {output_file}")
    except json.JSONDecodeError:
        print("Failed to parse JSON from OpenAI response.")
        print("Response was:", json_text)

# === Main Execution ===
pdf_file = "Barbee Farms Price List 2-23-2025.pdf"
output_excel = "barbee_farms_output.xlsx"

pdf_text = extract_pdf_text(pdf_file)
prompt = create_prompt(pdf_text)
json_result = get_json_from_openai(prompt)
save_json_to_excel(json_result, output_excel)


