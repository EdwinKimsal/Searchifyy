# Import(s)
import os
import time

# Custom function import(s)
from crawl import sitemap_links, map_links, combine


# Main function
def main():
    # Custom variables
    sitemap_in_file = "sitemaps"
    map_in_file = "maps"
    out_file = "all"
    extra_file = "extra"
    depth = 2 # Must be greater than or equal to 1 (whole number)
    max_sleep = 3 # Must be greater than or equal to 0 (whole number)

    # Start time
    start = time.time()

    # Paths
    cwd = os.getcwd()
    sitemaps_txt_path = os.path.join(cwd, "Input", f"{sitemap_in_file}.txt")
    maps_txt_path = os.path.join(cwd, "Input", f"{map_in_file}.txt")
    output_txt_path = os.path.join(cwd, "Output", f"{out_file}.txt")
    extra_txt_path = os.path.join(cwd, "Output", f"{extra_file}.txt")

    # # Reset output text file (OPTIONAL)
    # with open(output_txt_path, "w") as f:
    #     pass

    # Reset extra text file (OPTIONAL)
    with open(extra_txt_path, "w") as f:
        pass

    # Call proper functions
    # sitemap_links(sitemaps_txt_path, output_txt_path) # Sitemap function
    map_links(maps_txt_path, extra_txt_path, depth, max_sleep) # Mapping function
    # combine(output_txt_path, extra_txt_path) # Combine function

    # Get time elapsed
    end = time.time()
    elapsed_time = end - start
    print(f"{elapsed_time} seconds")


# Call main function
main()