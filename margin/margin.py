from PyPDF2 import PdfFileReader, PdfFileWriter
from tqdm import tqdm
import os
import glob

def margin(directory):
    dirlen = len(directory)
    pdflist = glob.glob(os.path.join(directory,"*.pdf"))
    
    for pdfs in pdflist:
        filename = pdfs[dirlen:-4]
        print(f'adding margin to {filename}..')
             
        with open(pdfs, 'rb') as f:
            p = PdfFileReader(f)
            number_of_pages = p.getNumPages()
            writer = PdfFileWriter()
            margin = 175
            print(f'margin: {margin}')
            for i in tqdm(range(number_of_pages)):
                page = p.getPage(i)
                new_page = writer.addBlankPage(
                    page.mediabox.getWidth() + 2 * margin,
                    page.mediabox.getHeight() + 2 * margin
                )
                new_page.mergeScaledTranslatedPage(page, 1, margin-(margin*0.5), margin)

            with open(f'{directory}/output{filename}_margin.pdf', 'wb') as f:
                writer.write(f)


if __name__ == '__main__':
    directory = '/Users/jonghyunlee/Desktop/Scrapbook/margin'
    margin(directory)