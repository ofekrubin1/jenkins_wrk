import os
import zipfile

# Define array
files = ['a', 'b', 'c', 'd']

# Function to create txt files
def create_txt_files():
    for file in files:
        with open(f'{file}.txt', 'w') as f:
            pass

# Function to create zip files
def create_zip_files(version):
    for file in files:
        with zipfile.ZipFile(f'{file}_{version}.zip', 'w') as zipf:
            zipf.write(f'{file}.txt', arcname=f'{file}.txt')

# Function to check if all txt files exist
def check_txt_files_exist():
    for file in files:
        if not os.path.exists(f'{file}.txt'):
            return False
    return True

# Function to check if all zip files exist
def check_zip_files_exist(version):
    for file in files:
        if not os.path.exists(f'{file}_{version}.zip'):
            return False
    return True

# Main function
def main():
    version = os.environ.get('VERSION')
    if version is None:
        print("VERSION environment variable is not set.")
        return

    create_txt_files()
    if not check_txt_files_exist():
        print("Not all txt files created.")
        return

    create_zip_files(version)
    if not check_zip_files_exist(version):
        print("Not all zip files created.")
        return

    print("All txt and zip files created successfully.")

if __name__ == "__main__":
    main()