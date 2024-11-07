FROM python:3.12-slim
WORKDIR /api
COPY api.py read_clean_data.py model.pkl CollegeDistance.csv requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "api.py"]