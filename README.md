# PDF Q&A Chatbot

A simple PDF Question Answer Chatbot built using FastAPI and PyMuPDF.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- PyMuPDF
- Nginx
- systemd
- AWS EC2

## Deployment

- FastAPI running on port 8000
- Nginx reverse proxy on port 80
- systemd service for auto-start

## Run Locally

pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000

#testing
## GitHub Actions Testing
