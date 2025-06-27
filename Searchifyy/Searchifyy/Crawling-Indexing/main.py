# Import(s)
import os
import time

# Custom function import(s)
from sitemap import sitemap_links

# Main function
def main():
    # Custom variables
    in_file = "sitemaps"
    out_file = "all"

    # Start time
    start = time.time()

    # Paths
    cwd = os.getcwd()
    sitemaps_txt_path = os.path.join(cwd, "Input", f"{in_file}.txt")
    output_txt_path = os.path.join(cwd, "Output", f"{out_file}.txt")

    # Call proper function
    sitemap_links(sitemaps_txt_path, output_txt_path) # Sitemap function

    # Get time elapsed
    end = time.time()
    elapsed_time = end - start
    print(elapsed_time)


# Call main function
main()