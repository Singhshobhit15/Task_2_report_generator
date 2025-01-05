import csv
from fpdf import FPDF

# Function to read data from a CSV file
def read_data_from_file(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to analyze data (e.g., average score calculation)
def analyze_data(data):
    total_score = 0
    count = len(data)
    
    # Calculate total score and average score
    for record in data:
        total_score += int(record['Score'])
        
    average_score = total_score / count if count > 0 else 0
    return total_score, average_score

# Function to generate the PDF report
def generate_pdf_report(data, total_score, average_score, output_filename):
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Automated Report', ln=True, align='C')

    # Adding date of report generation
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)  # line break
    pdf.cell(200, 10, f'Report generated on: 2025-01-05', ln=True, align='C')
    
    # Data Table Header
    pdf.ln(10)  # line break
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Name', 1)
    pdf.cell(60, 10, 'Score', 1)
    pdf.cell(60, 10, 'Date', 1)
    pdf.ln()

    # Table content (iterating through each row of data)
    pdf.set_font('Arial', '', 12)
    for record in data:
        pdf.cell(60, 10, record['Name'], 1)
        pdf.cell(60, 10, record['Score'], 1)
        pdf.cell(60, 10, record['Date'], 1)
        pdf.ln()

    # Adding analysis results
    pdf.ln(10)  # line break
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, f'Total Score: {total_score}', ln=True)
    pdf.cell(200, 10, f'Average Score: {average_score:.2f}', ln=True)

    # Save the PDF to a file
    pdf.output(output_filename)

# Main function to tie everything together
def main():
    file_path = 'data.csv'  # Input file path
    output_filename = 'report.pdf'  # Output PDF filename

    # Step 1: Read data from file
    data = read_data_from_file(file_path)

    # Step 2: Analyze the data
    total_score, average_score = analyze_data(data)

    # Step 3: Generate the PDF report
    generate_pdf_report(data, total_score, average_score, output_filename)
    print(f'Report generated successfully: {output_filename}')

# Run the script
if __name__ == '__main__':
    main()
