test_settings = {}

def add_setting(setting, key_value):
    key = str(key_value[0]).lower()
    value = str(key_value[1]).lower()

    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
        
    setting[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting, key_value):
    key = str(key_value[0]).lower()
    value = str(key_value[1]).lower()

    if key in setting:
        setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
        
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting, key):
    key = str(key).lower()

    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"
        
    return "Setting not found!"

def view_settings(setting):
    if not setting:
        return "No settings available."
    output = "Current User Settings:\n"
    for key, value in setting.items():
        output += f"- {key.capitalize()}: {value.capitalize()}\n"
    return output.strip()

#Test
print(add_setting(test_settings, ('Theme', 'Light')))
print(add_setting(test_settings, ('Notifications', 'enabled')))
print(view_settings(test_settings))
print(update_setting(test_settings, ('theme', 'dark')))
print(delete_setting(test_settings, ('notifications')))
print(view_settings(test_settings))
