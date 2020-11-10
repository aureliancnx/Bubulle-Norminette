def fill_variable(content, variable, value):
    return content.replace("{{" + variable + "}}", value)
