
def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("First line of text\n")
            file.write("Second line of text with a number: 12345\n")
            file.write("Third line of text\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        print("File creation and writing process completed.")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Reading file content:")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied while trying to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Fourth line of text\n")
            file.write("Fifth line of text with a number: 67890\n")
            file.write("Sixth line of text\n")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File appending process completed.")

if __name__ == "__main__":
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()
