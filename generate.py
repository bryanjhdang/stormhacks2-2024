import os
import yaml
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

TEMPLATE_DIR = "configuration/coverletter-template.md"
POSTING_TXT_DIR = "configuration/posting.txt"
POSTING_YML_DIR = "configuration/posting.yml"
PREFERENCES_DIR = "configuration/preferences.yml"
OUTPUT_DIR = "output"

def load_preferences():
    with open(PREFERENCES_DIR, 'r') as file:
        preferences = yaml.safe_load(file)
    return preferences

def load_posting_txt():
    posting_data = {}
    
    with open(POSTING_TXT_DIR, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace from each line
            line = line.strip()
            if not line:
                continue
            
            # Split only if the line contains a colon
            if ":" in line:
                key, value = line.split(":", 1)  # Split at the first colon only
                posting_data[key.strip()] = value.strip()
    
    return posting_data

def load_posting_yml():
    with open(POSTING_YML_DIR, 'r') as file:
        posting = yaml.safe_load(file)
    return posting

def load_template():
    with open(TEMPLATE_DIR, 'r') as file:
        template = file.read()
    return template

def fill_template(template, details):
    return template.format(**details)

def generate_pdf(content, output_filename="output.pdf"):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    # Create a canvas object and set the page size to letter (8.5 x 11 inches)
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Times-Roman", 12)

    # Split the content into lines to draw each line
    lines = content.split('\n')
    y_position = 10 * inch
    for line in lines:
        c.drawString(1 * inch, y_position, line)
        y_position -= 0.5 * inch  # Adjust line spacing

    # Save the PDF file
    c.save()
    print(f"PDF generated: {output_path}")

def generate_cover_letter(manual_posting):
    preference_detail = load_preferences()
    template = load_template()
    
    if manual_posting:
        posting = load_posting_yml()
    else:
        posting = load_posting_txt()

    preference_details = {
      'first_name': preferences['first_name'],
      'last_name': preferences['last_name'],
      'email': preferences['email'],
      'phone': preferences['phone'],
      'semester': preferences['semester']
    }
    
    posting_details = {
      'position_name': posting['Job Title'],
      'company_name': posting['Organization'],
      'recruiter_name': f"{posting['Job Contact First Name']} {posting['Job Contact Last Name']}",
      'address': posting['Address Line One'],
      'city': posting['City'],
      'province': posting['Province / State'],
      'postal_code': posting['Postal Code / Zip Code']
    }
    
    
    print(posting_details)
    # title = generate_title(preference_details)
    # info = generate_info(posting_details)
    # body = generate_body()
    
    # generate_pdf(posting_details, title, info, body)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a cover letter PDF.')
    parser.add_argument('--manual', type=bool, default=False, help='Use posting.yml instead of posting.txt')
    args = parser.parse_args()
    generate_cover_letter(args.manual)
