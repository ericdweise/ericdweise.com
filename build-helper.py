import os
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
print(f'{input_file} + header.html + footer.html > {output_file}')

HEADERFILE = 'assets/header.html'
FOOTERFILE = 'assets/footer.html'

with open(input_file, 'r') as fin:
    with open(output_file, 'w') as fout:
        for line in fin:
            if 'HEADER' in line:
                with open(HEADERFILE, 'r') as fhead:
                    for hline in fhead:
                        fout.write(hline)
            elif 'FOOTER' in line:
                with open(FOOTERFILE, 'r') as ffoot:
                    for fline in ffoot:
                        fout.write(fline)
            else:
                fout.write(line)
