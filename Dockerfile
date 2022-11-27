FROM Python:3.10.5
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY task.py .
CMD ["python", "task.py"]