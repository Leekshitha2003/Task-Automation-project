import os
import shutil

def organize_files(directory):
    """
    Organizes files in the given directory into subfolders based on their file types.

    Args:
        directory (str): The path to the directory to organize.
    """
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Check if the directory is empty
    if not os.listdir(directory):
        print(f"The directory '{directory}' is empty.")
        return

    # Scan through the files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1][1:].lower()  # Exclude the dot

        if not file_extension:
            file_extension = "no_extension"

        # Create a folder for the file type if it doesn't exist
        target_folder = os.path.join(directory, file_extension)
        os.makedirs(target_folder, exist_ok=True)

        # Move the file to the corresponding folder
        try:
            shutil.move(filepath, os.path.join(target_folder, filename))
        except Exception as e:
            print(f"Error moving file '{filename}': {e}")

    print(f"Files in '{directory}' have been organized.")

# Replace 'your_directory_path_here' with the path to the directory you want to organize
if __name__ == "__main__":
    directory_path = input("Enter the directory path to organize: ").strip()
    organize_files(directory_path)
