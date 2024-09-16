def print_key_value_args(**kvargs):  # key value arguments
    for key , value in kvargs.items():
        print(f"{key} : {value}")    # formating strings

print_key_value_args(name="ashis" , power="coding")
print_key_value_args(name="ashis" , power="coding" , age=23)
print_key_value_args(name="ashis" , power="coding" , age=23 , country="India")



