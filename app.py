from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import fitz

app = FastAPI()

pdf_path = "data/test.pdf.pdf"

doc = fitz.open(pdf_path)

pdf_text = ""

for page in doc:
    pdf_text += page.get_text()

HTML = """
<html>
<head>
<meta charset="UTF-8">
<title>PDF Q&A Chatbot</title>
</head>
<body>

<h1>PDF Q&A Chatbot</h1>

<form method="post">
<input type="text" name="question" style="width:400px">
<input type="submit">
</form>

<p><b>Answer:</b> {answer}</p>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML.format(answer="")

@app.post("/", response_class=HTMLResponse)
async def ask(question: str = Form(...)):

    answer_text = "Answer not found in uploaded document."

    lines = pdf_text.split("\n")

    for i, line in enumerate(lines):
        if question.lower() in line.lower():

            if i + 1 < len(lines):
                answer_text = lines[i + 1]

            break

    return HTML.format(answer=answer_text)
