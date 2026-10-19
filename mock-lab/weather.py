import random 
def get_temperature():
    return random.randint(-10,40)

def describe_weatehr():
    temp = get_temperature()
    if temp < 0: return "Freeze"
    elif temp < 15: return "Cold"
    else: return "Hot"