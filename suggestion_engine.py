def get_suggestions(parsed_line: dict, all_lines: list, vehicle_features: dict = None) -> list:
    suggestions = []
    part = parsed_line.get("part", "").lower()
    operation = parsed_line.get("operation", "").lower()

    def is_present(keyword):
        return any(keyword in line.get("part", "").lower() for line in all_lines)

    if operation == "rpr" and "bumper" in part:
        if not is_present("park sensor"):
            suggestions.append("CHECK IF EQUIPPED: add for parking sensors")
        if not is_present("auto park"):
            suggestions.append("CHECK IF EQUIPPED: add for auto park")
        if not is_present("headlamp washer"):
            suggestions.append("CHECK IF EQUIPPED: add for headlamp washers")
        if not is_present("fog lamp"):
            suggestions.append("CHECK IF EQUIPPED: add for fog lamps")
        if not is_present("flex additive"):
            suggestions.append("Add flex additive")
        if not is_present("bumper repair kit"):
            suggestions.append("Add bumper repair kit")

    return suggestions
