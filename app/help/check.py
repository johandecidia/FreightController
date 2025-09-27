def check_boolean_in_dict(var: dict) -> dict:
    for key, value in var.items():
        if value.lower() == 'true': var[key] = True
        elif value.lower() == 'false': var[key] = False
        elif value.lower() == 'null': var[key] = None
        elif value.lower() == 'none': var[key] = None
        elif value.lower() == 'any': var[key] = None
    return var