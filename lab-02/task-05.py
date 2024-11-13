def generate_code(template, variables):
    code = template.format(**variables)
    try:
        exec(code)  # Dynamically execute the code
    except Exception as e:
        return f"Błąd w generowanym kodzie: {e}"
    return "Kod został wykonany pomyślnie"


template = """
def generated_function(x):
    return x + {value}
"""
variables = {'value': 5}

result = generate_code(template, variables)
print(result)

if 'generated_function' in locals():
    generated_function_result = generated_function(10)
    print(generated_function_result)
else:
    print("Funkcja nie została wygenerowana.")
