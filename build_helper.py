import os
import sys


fHEAD = 'assets/head.html'
fHEADER = 'assets/header.html'
fFOOTER = 'assets/footer.html'


def copy_part(source, target_fp):
    assert(os.path.exists(source)), 'Cannot find input file: ' + source
    with open(source, 'r') as fin:
        for line in fin:
            target_fp.write(line)


def main(source, target):
    assert(os.path.exists(source)), 'Sourcefile does not exist: ' + source

    with open(target, 'w') as fout:
        fout.write('<!DOCTYPE html>\n')
        fout.write('<html lang="en">\n')
        copy_part(fHEAD, fout)
        fout.write('<body>\n')
        fout.write('<div class="contents">\n')
        copy_part(fHEADER, fout)
        fout.write('<div class="detail">\n')
        copy_part(source, fout)
        fout.write('</div> <!-- class="detail" -->\n')
        copy_part(fFOOTER, fout)
        fout.write('</div> <!-- class="contents" -->\n')
        fout.write('</body>\n')
        fout.write('</html>\n')

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
