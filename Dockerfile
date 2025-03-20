# Imagen base
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Exponer el puerto
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
