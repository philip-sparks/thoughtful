def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky
    is_bulky = (volume >= 1000000 or 
                width >= 150 or 
                height >= 150 or 
                length >= 150)
    
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Sort packages based on conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(100, 100, 100, 10))  
print(sort(150, 100, 100, 10))
print(sort(100, 100, 100, 20))  
print(sort(150, 100, 100, 20)) 
