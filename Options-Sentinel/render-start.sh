#!/usr/bin/env bash
# Exit on error
set -o errexit

# Create database tables based on SQLAlchemy models before starting the server
python -c "
import sys
try:
    from database.database import engine, Base
    from database import models
    Base.metadata.create_all(bind=engine)
    print('Database tables verified/created successfully.')
except Exception as e:
    print(f'Warning: Database auto-migration encountered an issue: {e}', file=sys.stderr)
    print('Continuing with server startup...', file=sys.stderr)
"

# Start the FastAPI server
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
