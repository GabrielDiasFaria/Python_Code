import pyttsx3
import PyPDF2

from googletrans import Translator

translator = Translator()
result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

book = open(r'C:\Users\gabri\Documents\GitHub\Python\AudioBook\book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(14, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    result = translator.translate(text, src='en', dest='pt')
    speaker.say(result.text)
    speaker.runAndWait()