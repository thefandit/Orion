import json
import os

class JSONHandler:
    def __init__(self, filename, full_write=False, load_on_init=True):
        """
        Initialize the JSONHandler class.

        Args:
            filename (str): The filename of the JSON file to be handled.
            full_write (bool, optional): If true, upon write_json, the data will replace the entire file.  Defaults to False. WARNING: DO NOT SET TO TRUE.
            load_on_init (bool, optional): If true, upon initialization, the data will be loaded from the JSON file. Defaults to True.
        """
        self.filename = filename
        self.data = None
        self.full_write = full_write
        if load_on_init:
            self.load_json()
    
    def load_json(self):
        """Loads the JSON into the handler.

        Returns:
            String: If any errors are encountered, returns the error message. Otherwise returns None.
        """
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            return f"File '{self.filename}' not found."
        except json.JSONDecodeError:
            return "Invalid JSON format."
        
    def write_json(self, data):
        """Writes the data to the JSON file. If full_write is true, sets the file to the data. If full_write is false, only updates fields.

        Args:
            data (JSON): JSON data to be writen to the file.

        Returns:
            String: Success or the caught exception.
        """
        if self.full_write:
            try:
                with open(self.filename, 'w') as file:
                    json.dump(data, file)
                return "Data written to the entire file."
            except Exception as e:
                return f"Error writing to file: {str(e)}"
            
        else:
            try:
                with open(self.filename, 'r') as file:
                    current_data = json.load(file)
                current_data.update(data)
                with open(self.filename, 'w') as file:
                    json.dump(current_data, file)
                return "Data written to the file."
            except Exception as e:
                return f"Error writing to file: {str(e)}"
            
    def get_value(self, key):
        """Gets the value of the given key. Returns it.

        Args:
            key (JSON): The JSON key.

        Returns:
            Any: String with error, or the data at the value.
        """
        try:
            return self.data[key]
        except KeyError:
            return f"Key '{key}' not found in JSON data."
        
    def set_value(self, key, value):
        """Sets the value in cache of the given key. SHOULD BE USED WITH A write_json IMMEDIATLY AFTER.

        Args:
            key (JSON): The JSON key.
            value (Any): The value to write at the given key.

        Returns:
            String: The success/exception message.
        """
        try:
            self.data[key] = value
            return "Value set successfully."
        except Exception as e:
            return f"Error setting value: {str(e)}"
        

def get_jason_filepath_from_sister_folder(filename):
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, '..', 'jasons', filename)
    return json_file_path