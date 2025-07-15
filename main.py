def sort(width, height, length, mass):
    # Validate inputs
    for val in (width, height, length, mass):
        if not isinstance(val, (int, float)):
            raise TypeError("All inputs must be numbers (int or float).")
        if val <= 0:
            raise ValueError("Dimensions and mass must be greater than zero.")

    volume = width * height * length

    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
if __name__ == "__main__":
    test_cases = [
        (50, 40, 30, 10),       # STANDARD
        (200, 30, 40, 10),      # SPECIAL (bulky)
        (50, 40, 30, 25),       # SPECIAL (heavy)
        (200, 200, 200, 25),    # REJECTED (bulky and heavy)
        (150, 10, 10, 10),      # SPECIAL (bulky: dimension)
        (100, 100, 100, 19.9),  # STANDARD
        (100, 100, 100, 20),    # SPECIAL (heavy)
        (100, 100, 100, 0),     # Invalid (mass zero)
        (-10, 100, 100, 10),    # Invalid (negative dimension)
        ("50", 40, 30, 10),     # Invalid (string input)
    ]

    for i, (w, h, l, m) in enumerate(test_cases):
        try:
            result = sort(w, h, l, m)
            print(f"Test {i+1}: sort({w}, {h}, {l}, {m}) -> {result}")
        except Exception as e:
            print(f"Test {i+1}: sort({w}, {h}, {l}, {m}) -> Error: {e}")

