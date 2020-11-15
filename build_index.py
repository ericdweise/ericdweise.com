import os
import sys
from html.parser import HTMLParser
from re import sub

from build_helper import copy_part
from build_helper import fHEAD
from build_helper import fHEADER
from build_helper import fFOOTER


TOC_ENTRY = '''
<div class="thought-toc-elt">
    <div class="date">DATE</div>
    <div class="blog-summary">
        <h3><a href="PATH">TITLE</a></h3>
        <p>SUMMARY</p>
        <p class="tags">TAGS</p>
    </div> <!-- blog-summary -->
</div> <!-- thought-toc-elt -->
'''



class MyHTMLParser(HTMLParser):
    metadata = {
            'date': '',
            'title': '',
            'summary': '',
            'keywords': ''}

    attrs_wanted = ['date', 'title', 'summary', 'keywords']

    def handle_starttag(self, tag, attrs):
        if tag != 'meta':
            return

        name = attrs[0][1]
        if name in self.attrs_wanted:
            if len(attrs) >= 2:
                if len(attrs[1]) >= 2:
                    self.metadata[name] = attrs[1][1]


def main(directory):
    print('Making index page for ' + directory)

    outfile = os.path.join(directory, 'index.html')
    print('Index will be in ' + outfile)

    pages = {}

    for root, _, files in os.walk(directory):
        for f in files:

            if '.stub' in f:
                continue

            if not f.endswith('.html'):
                continue

            html_file = os.path.join(root,f)

            if html_file == outfile:
                print('  skipping ' + outfile + ' as it will be overwritten')
                continue

            print('  Adding ' + html_file)

            with open(html_file, 'r') as fp:
                parser = MyHTMLParser()
                parser.feed(fp.read())

                while parser.metadata['date'] in pages.keys():
                    parser.metadata['date'] += ' '

                pages[parser.metadata['date']] = {
                        'title': parser.metadata['title'],
                        'summary': parser.metadata['summary'],
                        'keywords': parser.metadata['keywords'],
                        'path': '/' + html_file}


    html_contents = ''
    dates = list(pages)
    for date in sorted(dates, reverse=True):
        entry = TOC_ENTRY

        entry = sub('DATE', date, entry)
        entry = sub('PATH', pages[date]['path'], entry)
        entry = sub('TITLE', pages[date]['title'], entry)
        entry = sub('SUMMARY', pages[date]['summary'], entry)

        tags = sub(', ', ' #', pages[date]['keywords'])
        entry = sub('TAGS', '#' + tags, entry)

        html_contents += entry

    with open(outfile, 'w') as fout:
        fout.write('<!DOCTYPE html>\n')
        fout.write('<html lang="en">\n')
        copy_part(fHEAD, fout)
        fout.write('<body>\n')
        fout.write('<div class="contents">\n')
        copy_part(fHEADER, fout)
        fout.write('<div class="detail">\n')
        fout.write(html_contents)
        fout.write('</div> <!-- class="detail" -->\n')
        copy_part(fFOOTER, fout)
        fout.write('</div> <!-- class="contents" -->\n')
        fout.write('</body>\n')
        fout.write('</html>\n')


if __name__ == '__main__':
    directory = sys.argv[1]
    main(directory)
