import os  # Import the OS module

try:
    home = os.path.expanduser("~")  # Set the variable home by expanding the users set home directory
    print (home)  # Print the location

    if not os.path.exists(home + '/testdir'): # Chcek if it exists
        pass #pas geç
        # os.makedirs(home + '/testdir')  # If not create the directory, inside their home directory
except Exception as e:
    print (e)