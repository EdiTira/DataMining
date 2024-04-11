from process.process_text import process_text
import xml.etree.ElementTree as ET


def process_document(file_path, stop_words):
    tree = ET.parse(file_path)
    root = tree.getroot()

    title = root.find('.//title').text or ""
    paragraphs = root.findall('.//text//p')
    text = " ".join([p.text for p in paragraphs if p.text])

    combined_text = title + " " + text

    freq_vector = process_text(combined_text, stop_words)

    topics = [elem.attrib['code'] for elem in root.findall(".//codes[@class='bip:topics:1.0']/code")]

    return freq_vector, topics
