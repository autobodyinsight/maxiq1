from fastapi import FastAPI, Body, UploadFile, File
from fastapi.responses import HTMLResponse
from line_parser import parse_estimate_line
from suggestion_engine import get_suggestions
from PyPDF2 import PdfReader
import io

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
    reader = PdfReader(io.BytesIO(contents))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return {"extracted_text": text[:1000]}  # Preview first 1000 characters