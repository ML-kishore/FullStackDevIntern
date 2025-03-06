import pdfkit
from flask import Flask, render_template, send_file,url_for
import os

app = Flask(__name__)

# Correcting the wkhtmltopdf path
pdfkit_config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def get_names():
    with open("names.txt", "r") as file:
        names = [line.strip() for line in file.readlines()]
    return names

@app.route('/')
def home():
    names = get_names()
    return render_template('index.html', names=names)

@app.route('/certificate/<name>')
def get_certificate(name):
    return render_template('certificate.html', name=name)

@app.route('/certificate/<name>/pdf')
def generate_pdf(name):
    # Render HTML template
    html = render_template('certificate.html', name=name)

    # Convert to PDF
    pdf_file_path = f"certificates/{name}.pdf"
    os.makedirs("certificates", exist_ok=True)  # Ensure directory exists

    pdfkit.from_string(html, pdf_file_path, configuration=pdfkit_config, options={"disable-local-file-access": ""})

    # Return PDF as a file download
    return send_file(pdf_file_path, as_attachment=True, download_name=f"{name}_certificate.pdf")

if __name__ == '__main__':
    app.run(debug=True)
