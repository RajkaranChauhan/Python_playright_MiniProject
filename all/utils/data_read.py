import os


class DataRead:
    # Path to the text file
    file_path = os.path.join("utils", "data.txt")
    print(file_path)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    # parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
    # print("parent" + parent_dir)
    final_dir = os.path.join(script_dir ,"data.txt")
    # print("final_dir " + final_dir)
    # print((os.path.exists(final_dir)))

    def data_from_file( key):
        try:
            with open(DataRead.final_dir, "r") as file:
                for line in file:
                    # Strip whitespace and split key-value pairs
                    line = line.strip()
                    if "=" in line:
                        k, v = line.split("=", 1)  # Split on the first '='
                        if k.strip() == key:
                            return v.strip()
            return None  # Return None if the key is not found
        except FileNotFoundError:
            print(f"File not found: {DataRead.final_dir}")
            return None

# Main block to execute the script
if __name__ == "__main__":
    # Retrieve the value for the key 'pass'
    key_to_find = "pass"
    password = DataRead.data_from_file(key_to_find)
    print("***"+password)