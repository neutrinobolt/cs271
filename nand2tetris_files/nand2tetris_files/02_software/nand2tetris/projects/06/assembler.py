#! usr/bin/python3
"""
Translate .asm language into binary machine instructions.
Contains dictionaries for comp, dest and jump segments
"""

import sys

###############################################################################
# Dict functions

def comp_dict():
    """
    Generates dictionary of all comp keys.
    """
    keys = {
        "0"  : "0101010",
        "1"  : "0111111",
        "-1" : "0111010",
        "D"  : "0001100",
        "A"  : "0110000",
        "!D" : "0001101",
        "!A" : "0110001",
        "-D" : "0001111",
        "-A" : "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "A+D": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M"  : "1110000",
        "!M" : "1110001",
        "-M" : "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "M+D": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101",
    }
    return keys

def dest_dict():
    """
    Generates dictionary of all dest keys.
    """
    keys = {
        "null":"000",
        "M"   :"001",
        "D"   :"010",
        "DM"  :"011",
        "A"   :"100",
        "AM"  :"101",
        "AD"  :"110",
        "ADM" :"111",
    }

    return keys

def jump_dict():
    """
    Generates dictionary of all jump keys.
    """
    keys = {
        "null":"000",
        "JGT" :"001",
        "JEQ" :"010",
        "JGE" :"011",
        "JLT" :"100",
        "JNE" :"101",
        "JLE" :"110",
        "JMP" :"111",
    }

    return keys

###############################################################################
# String splicing functions

def parse(in_line: str) ->str:
    """
    Take raw string line and remove whitespace and comments
    """
    out_line = in_line.split("//")[0].strip()
    return out_line

def a_translate (line: str) ->str:
    """Translate an A_instruction string into a binary instruction string."""
    # Strip to address
    line = line.split("@")[1]
    # Check if address is a symbol (DO LATER)
    # Translate to 15-digit binary
    int_line = int(line)
    bin_line = f"{int_line:015b}"
    # print(bin_line)
    # Slap a 1 on front
    bin_line = "0" + bin_line
    return bin_line

def c_translate (line: str) -> str:
    """Translate a C_instruction string into a binary instruction string."""
    comps = comp_dict()
    dests = dest_dict()
    jumps = jump_dict()
    # Splice string into parts
    # Jump
    if ";" in line:
        jump = line.split(";")[1].strip(";")
        line = line.split(";")[0]
        # print(f"line: {line}")
    else:
        jump = "null"
    # print(f"jump: {jump}")
    # Comp
    if "=" in line:
        comp = line.split("=")[1].strip("=")
        # print(f"comp: {comp}")
        line = line.split("=")[0]
    else:
        comp = line
        # print(f"comp: {comp}")
    # Dest is remainder of line
    dest = line
    # print(f"dest: {dest}")
    # Set opening bits
    open_bits = "111"
    # Set comp bits (7)
    comp_bits = comps[comp]
    # print(f"comp_bits: {comp_bits}")
    # Set destination bits
    dest_bits = dests[dest]
    # print(f"dest_bits: {dest_bits}")
    # Set jump bits
    jump_bits = jumps[jump]
    # print(f"jump_bits: {jump_bits}")
    # Put it all together
    bin_line = open_bits + comp_bits + dest_bits + jump_bits
    # print(f"bin_line: {bin_line}")
    return bin_line

def bin_translate (line: str) -> str:
    """Redirects to correct translation function"""
    if line[0] == "@":
        bin_line = a_translate(line)
        return bin_line
    # Add L_instruction later
    # D_instruction
    bin_line = c_translate(line)
    return bin_line


###############################################################################
# Main

def main():
    """
    Takes .asm file of input name on terminal, outputs translated binary .hack
    file
    """

    # Extract lines from source file
    in_file_name = sys.argv[1]
    in_lines = []
    with open(in_file_name, "r", encoding="utf-8") as in_file:
        in_lines = in_file.readlines()

    # Strip whitespace and comments
    parsed_lines = []
    for line in in_lines:
        out_line = parse(line)
        if (out_line != "") & (out_line != "\n") :
            parsed_lines.append(out_line)
    print(f"parsed_lines: {parsed_lines}")

    # Translate lines into binary
    bin_lines = []
    for line in parsed_lines:
        bin_line = bin_translate(line)
        bin_lines.append(bin_line)
    print(f"bin_lines: {bin_lines}")

    # Open and write lines to ouptut file
    # Get file name
    out_file_name = in_file_name.split(".")[1]
    out_file_name = "." + out_file_name + ".hack"
    print(f"out_file: {out_file_name}")
    # Open/create outfile
    with open(out_file_name, "w", encoding="utf-8") as out_file:
        # Write in bin lines
        for line in bin_lines:
            out_file.writelines(line + "\n")

if __name__ == "__main__":
    main()
