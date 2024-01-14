import os
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

class CommandPrompt:
    def __init__(self):
        self.current_directory = os.getcwd()

    @execution_time_decorator
    def ls(self):
        directories = [name for name in os.listdir(self.current_directory) if os.path.isdir(os.path.join(self.current_directory, name))]
        for directory in directories:
            print(directory)

    @execution_time_decorator
    def cd(self, folder_name):
        new_directory = os.path.join(self.current_directory, folder_name)
        if os.path.isdir(new_directory):
            self.current_directory = new_directory
        else:
            raise Exception("Directory not found")

    @execution_time_decorator
    def cd_back(self):
        parent_directory = os.path.dirname(self.current_directory)
        if parent_directory != self.current_directory:
            self.current_directory = parent_directory
        else:
            raise Exception("Already at the root directory")

    @execution_time_decorator
    def create_folder(self, folder_name):
        new_folder_path = os.path.join(self.current_directory, folder_name)
        os.makedirs(new_folder_path)

    @execution_time_decorator
    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.current_directory, folder_name)
        os.rmdir(folder_path)

    @execution_time_decorator
    def rename_folder(self, old_name, new_name):
        old_folder_path = os.path.join(self.current_directory, old_name)
        new_folder_path = os.path.join(self.current_directory, new_name)
        os.rename(old_folder_path, new_folder_path)

    @execution_time_decorator
    def view_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                print(file.read())
        else:
            raise Exception("File not found")

# Example usage
cmd = CommandPrompt()
cmd.ls()  # List directories in the current folder
cmd.cd('FolderName')  # Change to a specific folder
cmd.cd_back()  # Go back to the parent folder
cmd.create_folder('NewFolder')  # Create a new folder
cmd.delete_folder('FolderToDelete')  # Delete a folder
cmd.rename_folder('OldFolderName', 'NewFolderName')  # Rename a folder
cmd.view_file('example.txt')  # View the contents of a file
