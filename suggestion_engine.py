def get_suggestions(parsed_line: dict, vehicle_features: dict = None) -> list:
    suggestions = []
    part = parsed_line.get("part", "").lower()
    operation = parsed_line.get("operation", "").lower()

    if operation == "rpr" and "bumper" in part:
        suggestions.extend([
            "Add flex additive",
            "Add bumper repair kit"
        ])
        if vehicle_features:
            if vehicle_features.get("parking_sensors"):
                suggestions.append("Add for parking sensors")
            if vehicle_features.get("auto_park"):
                suggestions.append("Add for auto park")
            if vehicle_features.get("headlamp_washers"):
                suggestions.append("Add for headlamp washers")
    return suggestions