from pathlib import Path
import sys

def combine_text_files(input_dir: str, output_file: str) -> None:
    """
    Reads all .txt files from input_dir and writes their contents to
    output_file in alphabetical order, separated by a newline.
    """
    input_path = Path(input_dir)
    output_path = Path(output_file)

    txt_files= sorted(input_path.glob("*.txt"))
    with output_path.open("w", encoding="utf-8") as outfile:
        for txt_file in txt_files:
            with txt_file.open("r", encoding="utf-8") as infile:
                # This print statement is helpful if one of the input files is corrupted 
                # or has an unsupported character.
                # At least you know which file to look at!
                print(f"Reading file: {txt_file}")
                outfile.write(infile.read())
                # add a blank line between files, for (human) readability 
                # and to ensure there is always whitespace between words
                outfile.write("\n") 

if __name__ == "__main__":


    if len(sys.argv) < 3:
        print("Usage: python text_merge.py input_dir output_file")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]

    combine_text_files(input_directory, output_file)
