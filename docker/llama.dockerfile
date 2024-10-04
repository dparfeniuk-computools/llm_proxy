# Use a slim base image with Python
FROM python:3.12-slim

# Set up environment variables
ENV PYTHONUNBUFFERED=1

# Install necessary system dependencies
RUN apt-get update \
    && apt-get install -y build-essential git \
    libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone and build llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp /llama.cpp \
    && cd /llama.cpp \
    && make

WORKDIR /app/

# Copy the llama models into the container
COPY llama_models/ /app/llama_models/

# Expose the default llama-server port (8080)
EXPOSE 8080

# Run llama-server when the container starts
CMD ["/llama.cpp/llama-server", "-m", "/app/llama_models/Phi-3-mini-4k-instruct-q4.gguf", "--host", "0.0.0.0"]
