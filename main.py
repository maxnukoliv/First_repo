import os

def hex_binary_invert(input_file, output_file):
    
    try:
        # proverka
        if not os.path.exists(input_file):
            print(f"Error: The file '{input_file}' does not exist.")
            return

        # otkrivaem v binary
        with open(input_file, 'rb') as infile:
            data = infile.read()

        # delaem binary inver
        inverted_data = bytes(~byte & 0xFF for byte in data)

        # delaem output
        with open(output_file, 'wb') as outfile:
            outfile.write(inverted_data)

        print(f"HEX Binary Invert operation completed. Output saved to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
#result
if __name__ == "__main__":
    input_path = ("/storage/emulated/0/Android/data/com.godku.project/files/89bb4eb5637df3cd96c463a795005065").strip()
    output_path = ("/storage/emulated/0/Output/89bb4eb5637df3cd96c463a795005065").strip()

    hex_binary_invert(input_path, output_path)
