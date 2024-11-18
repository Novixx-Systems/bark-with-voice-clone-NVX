# create file:
# 0.wav|a
# 2.wav|a
# 4.wav|a
# ...
# 3144.wav|a

import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dmaker.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    with open(output_file, "w") as f:
        for i in range(0, 3145, 2):
            f.write(f"{i}.wav|a\n")

if __name__ == "__main__":
    main()