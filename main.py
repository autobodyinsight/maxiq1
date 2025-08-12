from fastapi import FastAPI, Body
from line_parser import parse_estimate_line
from suggestion_engine import get_suggestions

app = FastAPI()

@app.post("/audit")
def audit_line(line: str = Body(...), features: dict = Body(default={})):
    parsed = parse_estimate_line(line)
    if not parsed:
        return {"error": "Invalid estimate line format"}
    suggestions = get_suggestions(parsed, features)
    return {"parsed": parsed, "suggestions": suggestions}