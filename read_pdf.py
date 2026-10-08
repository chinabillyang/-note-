import pdfplumber

out = []
with pdfplumber.open(r'C:\Users\Administrator\Downloads\第1章.pdf') as pdf:
    for i, page in enumerate(pdf.pages, 1):
        txt = page.extract_text() or ''
        out.append(f'=== PAGE {i} ===')
        out.append(txt)
        out.append('')

with open(r'C:\Users\Administrator\AppData\Local\Temp\opencode\chapter1.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('done')
