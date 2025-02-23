# Use Miniconda base image
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Install Python 3.10 explicitly
RUN conda create -n myenv python=3.10 -y

# Activate Conda environment and upgrade pip
RUN /bin/bash -c "source activate myenv && pip install --upgrade pip setuptools wheel"

# Copy application files
COPY . /app

# Install dependencies inside the Conda environment
RUN /bin/bash -c "source activate myenv && pip install 'numpy<2' -r /app/requirements.txt"

# Set default command
CMD ["/bin/bash", "-c", "source activate myenv && python app.py"]
