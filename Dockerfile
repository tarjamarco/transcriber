# -------------------------------
# 1. Base Image
# -------------------------------
FROM python:3.10-slim

# -------------------------------
# 2. System Dependencies
# -------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# 3. Working Directory
# -------------------------------
WORKDIR /app

# -------------------------------
# 4. Copy App Files
# -------------------------------
COPY transcribe_flask.py /app/
COPY requirements.txt /app/

# -------------------------------
# 5. Install Python Dependencies
# -------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------
# 6. Expose Flask Port
# -------------------------------
EXPOSE 5000

# -------------------------------
# 7. Run Flask Server
# -------------------------------
CMD ["python", "transcribe_flask.py"]
