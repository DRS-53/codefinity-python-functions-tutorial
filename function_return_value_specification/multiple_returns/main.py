def validate_registration(username, email, password):
    errors = []
    is_valid = True

    if len(username) < 3:
        errors.append("Username must be at least 3 characters long.")
    if "@" not in email:
        errors.append("Invalid email format.")
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")
    if errors:
        is_valid = False
    
    return is_valid, errors

# Testing the result
is_valid, errors = validate_registration("js", "userexample.com", "123")

if is_valid:
    print("Validation successful:", is_valid)
else:
    print("Errors:", errors)