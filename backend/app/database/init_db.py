from app.database.db import engine
from app.models.user import User
from app.models.threat import Threat

User.metadata.create_all(bind=engine)
Threat.metadata.create_all(bind=engine)

print("Database tables created.")
