FROM python:3.12-slim AS builder

# Install curl (needed for uv installer)
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency files only
COPY backend/pyproject.toml backend/uv.lock* ./

# Sync dependencies (build the Python environment)
RUN uv sync --frozen

# Copy project files after dependencies
COPY backend/ /app

# Optional: re-sync to ensure latest project requirements are installed
RUN uv sync --frozen

# Final image
FROM python:3.12-slim

# Copy uv binary
COPY --from=builder /root/.local/bin/uv /usr/local/bin/uv

# Copy Python environment from builder
COPY --from=builder /root/.local /root/.local

# Set PATH to include uv environment
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy project files
COPY --from=builder /app /app


# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
