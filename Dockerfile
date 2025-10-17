# -----------------------------------------------------------
# WildRydes Flask App Container - Ravi Kiran Koti
# Student ID: 101002870
# -----------------------------------------------------------

# 1. Use official Python base image
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy project files into the container
COPY . /app

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose port 5000 for Flask
EXPOSE 5000

# 6. Run the web app
CMD ["python", "app.py"]
