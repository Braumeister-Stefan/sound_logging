import subprocess
import os
import winsound
import time

# Path to the VBS script
vbs_path = f"{os.getcwd()}/alert_user.vbs"

# Decorator function
def speak_function_name(func):
    def wrapper(*args, **kwargs):
        try:
            # Try to call the original function
            result = func(*args, **kwargs)
            status = "finished"
            # High frequency beep for success
            winsound.Beep(2000, 500)  # Frequency, Duration in milliseconds
            winsound.Beep(2000, 500)
            winsound.Beep(2000, 500)


        except Exception as e:
            # Handle the exception and set a failure message
            status = "failed"
            result = None
            # Low frequency beep for failure
            winsound.Beep(750, 750)  # Frequency, Duration in milliseconds
            winsound.Beep(500, 750)
            winsound.Beep(400, 1000)


            # Speak the function name and status
        subprocess.call(["cscript", vbs_path, f"function {func.__name__.replace('_', ' ')} {status}", status])

        return result
    return wrapper

# Example usage of the decorator
@speak_function_name
def print_something():
    print("Function is running")
    time.sleep(4)  # Wait for half a second
    print("Function is running again")

@speak_function_name
def add_numbers(num1, num2):
    return num1 + num2

@speak_function_name
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32



if __name__ == "__main__":
    print_something()
    add_numbers(1, 2)
    add_numbers(1, 2)
    add_numbers(1, 2)
    celsius_to_fahrenheit("twelve")  # This will cause an exception