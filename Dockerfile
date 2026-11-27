# 1. Select the Python base image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies first
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the application files
COPY . .

# 6. Document the application port
EXPOSE 5001

# 7. Start the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
