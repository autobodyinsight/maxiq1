def parse_estimate_line(line: str) -> dict:
    tokens = line.strip().split()
    if len(tokens) < 4:
        return {}
    return {
        "operation": tokens[0],
        "part": " ".join(tokens[1:-2]),
        "body_lab": float(tokens[-2]),
        "paint_lab": float(tokens[-1])
    }