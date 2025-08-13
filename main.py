from fastapi import FastAPI, Body, UploadFile, File
from fastapi.responses import HTMLResponse
from line_parser import parse_estimate_line, parse_estimate_lines  # ✅ Add this
from suggestion_engine import get_suggestions
from PyPDF2 import PdfReader
import io
import pdfplumber

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>MAXIQ Audit Engine is Live 🚀</h1><p>Ready to receive requests.</p>"

@app.get("/favicon.ico")
def favicon():
    return ""

@app.post("/audit")
def audit_line(line: str = Body(...), features: dict = Body(default={})):
    parsed = parse_estimate_line(line)
    if not parsed:
        return {"error": "Invalid estimate line format"}
    suggestions = get_suggestions(parsed, features)
    return {"parsed": parsed, "suggestions": suggestions}

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    contents = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(contents)

    text = ""
    with pdfplumber.open("temp.pdf") as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return {"extracted_text": text[:5000]}  # Increase preview limit
