from datetime import datetime


def get_new_email():
    time_stab = datetime.now().strftime("%Y_%m_%d_%H_%S")
    return "manas" + time_stab + "@gmail.com"
