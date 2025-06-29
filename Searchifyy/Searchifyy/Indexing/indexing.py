"""
This file contains the functions used to index the crawled data
"""

# Import(s)
import string
import csv
import ast


# Function to fix links by removing unwanted data and putting it into a CSV file
def fix_data(in_file, out_file):
    # List of required characters
    required_char = [char for char in string.ascii_lowercase + string.digits + "/"]

    # Create file with field names
    field_names = ["link", "fixed_link", "length_link"]
    with open(out_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()

        # Open in_file and iterate through each line (link)
        with open(in_file, "r") as f:
            for link in f:
                # Strip unimportant data
                link = link.strip("\n")
                fixed_link = link.lower()
                fixed_link = fixed_link.strip("https://www")
                fixed_link = fixed_link.replace(".com", "")
                fixed_link = fixed_link.replace(".php", "")
                fixed_link = fixed_link.replace(".org", "")
                fixed_link = fixed_link.replace(".asp", "")

                # Iterate through each character and get rid of non-required char
                for char in fixed_link:
                    if char not in required_char:
                        fixed_link = fixed_link.replace(char, "/")

                # Make fixed_link a list separated by /
                fixed_link = fixed_link.split("/")

                # Remove all elements from fixed_link that are less than two char long
                fixed_link = [ele for ele in fixed_link if len(ele) >= 2]

                # Find length of wanted data
                length_link = sum(len(ele) for ele in fixed_link)

                writer.writerow({"link":link, "fixed_link":fixed_link, "length_link":length_link})


# Function to create inverse index
def inverse_index(in_file, out_file):
    # Create a blank dictionary to store words
    word_index = {}

    # Open CSV file
    with open(in_file, "r") as f:
        # Create a list for every line
        reader_obj = csv.reader(f)
        next(reader_obj)  # Skips the first line (header row)

        # Iterate through each line and get needed elements
        for line in reader_obj:
            site = line[0]
            words = ast.literal_eval(line[1])

            # Add site appropriately to word index
            for word in words:
                if word in word_index.keys():
                    word_index[word].append(site)
                else:
                    word_index[word] = [site]

    # Open output file
    with open(out_file, "w", newline="") as f:
        # Set header
        field_names = ["word", "sites"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()

        # Add each word and its sites as a row
        for key, value in word_index.items():
            writer.writerow({"word":key, "sites":str(value)}) # Write data row


# Function to count the combinations in letters
def combo_counter(in_file, out_file):
    pass