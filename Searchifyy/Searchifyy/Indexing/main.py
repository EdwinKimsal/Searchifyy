# Import(s)
import os
from indexing import fix_data, inverse_index, combo_counter
import time


# Main function
def main():
    # Customizable variables
    in_dir = "Output"
    out_dir = "Output"
    in_file = "basic.csv"
    out_file = "inverse_index.csv"

    # Set paths
    cwd = os.getcwd()
    in_path = os.path.join(cwd, in_dir, in_file)
    out_path = os.path.join(cwd, out_dir, out_file)

    # Start time
    start = time.time()

    # Call proper functions
    # fix_data(in_path, out_path)
    # inverse_index(in_path, out_path)
    # combo_counter(in_path, out_path)

    # Get time elapsed
    end = time.time()
    elapsed_time = end - start
    print(f"{elapsed_time} seconds")


# Call main function
main()