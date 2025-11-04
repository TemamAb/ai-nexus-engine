FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend

# Copy frontend files
COPY dashboard/package.json dashboard/package-lock.json ./
RUN npm ci --silent

COPY dashboard/ ./
RUN npm run build

FROM python:3.11-slim AS backend-builder
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r ainexus && useradd -r -g ainexus ainexus

# Copy Python dependencies from builder
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend-builder /usr/local/bin /usr/local/bin

# Copy application code
COPY src/ ./src/
COPY core/ ./core/
COPY config/ ./config/
COPY contracts/ ./contracts/

# Copy built frontend
COPY --from=frontend-builder /app/frontend/dist ./static

# Create necessary directories
RUN mkdir -p /app/logs /app/data && \
    chown -R ainexus:ainexus /app

# Switch to non-root user
USER ainexus

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Environment variables
ENV PYTHONPATH=/app/src
ENV ENVIRONMENT=production
ENV DAILY_PROFIT_TARGET=250000
ENV CAPACITY=100000000

# Start command
CMD ["python", "src/main.py"]
