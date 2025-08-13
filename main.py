from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from line_parser import parse_estimate_line
from suggestion_engine import get_suggestions

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