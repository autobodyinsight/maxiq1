def get_suggestions(parsed_line: dict, all_lines: list, vehicle_features: dict = None) -> list:
    """
    Generate audit suggestions for a parsed line item, only if those items are missing from the estimate.
    """
    suggestions = []
    part = parsed_line.get("part", "").lower()
    operation = parsed_line.get("operation", "").lower()

    if operation == "rpr" and "bumper" in part:
        def is_present(keyword):
            return any(keyword in line.get("part", "").lower() or keyword in line.get("operation", "").lower()
                       for line in all_lines)

        if not is_present("flex additive"):
            suggestions.append("Add flex additive")
        if not is_present("bumper repair kit"):
            suggestions.append("Add bumper repair kit")

        if vehicle_features:
            if vehicle_features.get("parking_sensors") and not is_present("parking sensor"):
                suggestions.append("Add for parking sensors")
            if vehicle_features.get("auto_park") and not is_present("auto park"):
                suggestions.append("Add for auto park")
            if vehicle_features.get("headlamp_washers") and not is_present("headlamp washer"):
                suggestions.append("Add for headlamp washers")
            if vehicle_features.get("fog_lamps") and not is_present("fog lamp"):
                suggestions.append("Add for fog lamps (R&I)")

    return suggestions
