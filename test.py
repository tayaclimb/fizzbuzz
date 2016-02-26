def side_effect_test(value):
    """Shows us about sideeffects"""
    value[1] = "orange"
    print("Inside the function the value becomes{}".format(value))
    
if_name_ == "_main_":
    value = ["red", "green", "blue"]
    print("Outside the function, the value starts as {}".format(value))
    
    side_effect_test(value)
    
    print("Outside the function, the value is now {}".format(value))
    

    

    