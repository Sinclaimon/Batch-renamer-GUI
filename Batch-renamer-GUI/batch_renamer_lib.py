import os
import logging
import shutil
import collections.abc as collections


class BatchRenamer:
    def __init__(self, 
                 filepath          = None,
                 copy_files        = False,
                 filetypes         = None,
                 strings_to_find   = None,
                 string_to_replace = '',
                 prefix            = None,
                 suffix            = None):
        self.filepath          = filepath
        self.copy_files        = copy_files
        self.filetypes         = filetypes
        self.strings_to_find   = strings_to_find
        self.string_to_replace = string_to_replace
        self.prefix            = prefix
        self.suffix            = suffix

        self.initialize_logger()


    def initialize_logger(self, print_to_screen = False):
        """
        Creates a logger

        Args:
            print_to_screen: for printing to screen as well as file
        """

        ###############
        # Basic Setup #
        ###############
        app_title = 'Test'
        version_number = '1.0.0'
        # get the path the script was run from, storing with forward slashes
        source_path = os.path.dirname(os.path.realpath(__file__))
        # create a log filepath
        logfile_name = f'{app_title}.log'
        logfile = os.path.join(source_path, logfile_name)

        # tell the user where the log file is
        print(f'Logfile is {logfile}')

        # more initialization
        self.logger = logging.getLogger(f'{app_title} Logger')
        self.logger.setLevel(logging.INFO)
        
        ###############################
        # Formatter and Handler Setup #
        ###############################
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.INFO)
        # formatting information we want (time, self.logger name, version, etc.)
        formatter = logging.Formatter(f'%(asctime)s - %(name)s {version_number} - '
                                    '%(levelname)s - %(message)s')
        # setting the log file format
        file_handler.setFormatter(formatter)
        # clean up old handlers
        self.logger.handlers.clear()

        # add handler
        self.logger.addHandler(file_handler)

        # allowing to print to screen
        if print_to_screen:
            # create a new "stream handler" for logging/printing to screen
            console = logging.StreamHandler()
            self.logger.addHandler(console)
            # setting the print log format
            console.setFormatter(formatter)

        self.logger.info('Logger Initiated')


    def get_renamed_file_path(self, existing_name, string_to_find, string_to_replace, 
                              prefix, suffix):
        # Logging
        self.logger.info("Getting renamed file path for: " + existing_name)
        
        # Making string_to_find a list if it isn't already
        if not isinstance(string_to_find, collections.Collection) or isinstance(string_to_find, str):
            string_to_find = [string_to_find]

        if not string_to_find:
            self.logger.warning("string_to_find is empty. No replacements made")

        self.logger.info("number of strings to replace: " + str(len(string_to_find)))

        # Split the existing name into base name and extension
        base_name, extension = os.path.splitext(existing_name)

        # Replacing all strings in string_to_find with string_to_replace
        for find_str in string_to_find:
            self.logger.debug(f"Replacing '{find_str}' with '{string_to_replace}'")
            base_name = base_name.replace(find_str, string_to_replace)

        # Adding prefix and suffix
        new_name = prefix + base_name + suffix + extension

        return new_name

    def get_files_with_extension(self, folder_path, extension):
        # Making sure the folder exists first
        if not os.path.isdir(folder_path):
            self.logger.error("Folder path does not exist")
            return []
        
        self.logger.info("Getting files with extension: " + extension + " in folder: " + folder_path)

        # Getting all files in the folder
        folder_files = next(os.walk(folder_path))[2]

        # List to store all the files with the correct extension
        matching_files = []

        # Iterating through all the files in the folder
        for file in folder_files:
            self.logger.debug("Working on file: " + file)
            
            # Remove the dot from the extension
            file_extension = os.path.splitext(file)[1][1:]  
            self.logger.debug("File extension string only: " + file_extension)

            if file_extension == extension:
                matching_files.append(file)
                self.logger.info("Added a matching file: " + file)

        if not matching_files:
            self.logger.warning(f"No files found with extension: {extension}")

        return matching_files

    def rename_file(self, existing_name, new_name, copy=False):
        if not os.path.exists(existing_name):
            self.logger.warning(f"File {existing_name} does not exist. Skipping.")
            return

        try:
            if copy:
                shutil.copy(existing_name, new_name)
                self.logger.info(f"Copied file from {existing_name} to {new_name}")
            else:
                os.rename(existing_name, new_name)
                self.logger.info(f"Renamed file from {existing_name} to {new_name}")
        except Exception as e:
            self.logger.error(f"Failed to rename/copy file to {new_name}: {e}")

    def rename_files_in_folder(self, folder_path, extension, string_to_find,
                               string_to_replace, prefix, suffix, copy=False):
        matching_files = self.get_files_with_extension(folder_path, extension)
        for file in matching_files:
            existing_name = os.path.join(folder_path, file)
            new_name = self.get_renamed_file_path(file, string_to_find, 
                                                  string_to_replace, prefix, suffix)
            new_name = os.path.join(folder_path, new_name)
            self.logger.debug(f"Renaming file from {existing_name} to {new_name}")
            self.rename_file(existing_name, new_name, copy)

def main():
    renamer = BatchRenamer()
    
    # Logger
    renamer.initialize_logger(True)
    renamer.logger.info('Logger Initiated')


if __name__ == '__main__':
    main()