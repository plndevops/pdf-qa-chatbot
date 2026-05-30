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

<h1>PDF Q&A Chatbot - CI/CD Test</h1>

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

    if question.lower() in pdf_text.lower():
        answer_text = "Found in PDF"
    else:
        answer_text = "Answer not found in uploaded document."

    return HTML.format(answer=answer_text)
