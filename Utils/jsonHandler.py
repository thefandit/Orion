import json

class jsonHandler:
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