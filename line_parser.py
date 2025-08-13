import re

def parse_estimate_lines(raw_text: str) -> list:
    lines = raw_text.split("\n")
    parsed = []

    for line in lines:
        match = re.search(r"(rpr|repl|r&i|refn)\s+(.*?)(\d+\.\d+)?\s*(\d+\.\d+)?$", line.lower())
        if match:
            operation = match.group(1)
            part = match.group(2).strip()
            labor = float(match.group(3)) if match.group(3) else 0.0
            paint = float(match.group(4)) if match.group(4) else 0.0

            parsed.append({
                "operation": operation,
                "part": part,
                "labor_hours": labor,
                "paint_hours": paint
            })

    return parsed
