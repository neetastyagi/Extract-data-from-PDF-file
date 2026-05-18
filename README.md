# Extract-data-from-PDF-file

Using prompt engineering extracting data from the PDF file into JSON format

## Overview

This project demonstrates a practical approach to extract structured data from PDF files using OpenAI's GPT models combined with prompt engineering. The extracted data is automatically converted to JSON format and can be exported to Excel for further analysis.

## Features

- **PDF Text Extraction**: Extracts text content from PDF files using PyMuPDF
- **Prompt Engineering**: Uses carefully crafted prompts to instruct OpenAI to structure data in JSON format
- **JSON Output**: Returns structured JSON data with defined fields
- **Excel Export**: Converts extracted JSON data to Excel format (.xlsx)

## Technologies Used

- **Python 3.x**
- **OpenAI API**: GPT-4 (or GPT-3.5-turbo) for data extraction and structuring
- **PyMuPDF (fitz)**: For PDF text extraction
- **Pandas**: For data manipulation and DataFrame operations
- **OpenPyXL**: For Excel file generation

## Installation

Install the required dependencies:

```bash
pip install openai pymupdf pandas openpyxl
```

## Usage

### 1. Set up OpenAI API Key

Before running the script, set your OpenAI API key in `DataExtraction.py`:

```python
openai.api_key = "your-api-key-here"
```

### 2. Run the Script

Update the `pdf_file` variable with your PDF file path:

```python
pdf_file = "your_file.pdf"
output_excel = "output.xlsx"
```

Then execute:

```bash
python DataExtraction.py
```

## How It Works

### Step 1: Extract Text from PDF
The `extract_pdf_text()` function opens the PDF file and extracts all text content from each page using PyMuPDF.

### Step 2: Create Structured Prompt
The `create_prompt()` function generates a prompt that instructs OpenAI to extract data in a specific JSON structure. It includes:
- Example JSON schema showing the expected output format
- Instructions to return ONLY JSON array without extra explanation
- The extracted PDF text for processing

### Step 3: Get JSON from OpenAI
The `get_json_from_openai()` function sends the prompt to OpenAI's API using GPT-4 (or GPT-3.5-turbo) with temperature set to 0 for deterministic results.

### Step 4: Export to Excel
The `save_json_to_excel()` function:
- Parses the JSON response
- Converts it to a Pandas DataFrame
- Exports the data to an Excel file

## Example Output Format

The script extracts data into the following JSON structure:

```json
{
  "Item": "Beets, Red",
  "Case Size": "bag",
  "Quantity per Case": 25,
  "Price per case": "$40",
  "Wholesale Quantity": "20+ Cases",
  "Wholesale Price": "$35",
  "UOM": "lb",
  "Less Than Case Price": "$3/lb",
  "Quantity Available": 40
}
```

## Requirements

- Valid OpenAI API key
- PDF file with data to extract
- Python 3.6+

## Notes

- The temperature parameter is set to 0 for consistent, deterministic output
- For large PDFs, consider OpenAI API rate limits and costs
- The prompt structure can be customized based on your specific data format

## License

This project is open source and available under the MIT License.
