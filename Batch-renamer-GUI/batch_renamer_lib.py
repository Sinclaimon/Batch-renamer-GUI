class BatchRenamer:
    def __init__(self):
        pass

    def rename_files(self, directory, new_name_format):
        """
        Rename files in the specified directory based on the new name format.
        
        :param directory: The directory containing files to rename.
        :param new_name_format: The format for the new file names.
        """
        import os

        # List all files in the directory
        files = os.listdir(directory)
        for index, filename in enumerate(files):
            # Construct new file name
            new_name = new_name_format.format(index=index, original=filename)
            # Get full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_file, new_file)

    def validate_new_name_format(self, new_name_format):
        """
        Validate the new name format string.
        
        :param new_name_format: The format string to validate.
        :return: True if valid, False otherwise.
        """
        # Check if the format string contains placeholders
        return '{index}' in new_name_format or '{original}' in new_name_format