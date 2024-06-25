FROM python:3.9-slim
COPY . ./app
WORKDIR /app
RUN pip3 install -r reqruirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501"]
