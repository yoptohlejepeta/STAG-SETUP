from fastapi import HTTPException
from redis import Redis
from .settings import Settings

settings = Settings()
r = Redis(
    host=settings.redis.host, port=settings.redis.port, db=settings.redis.db
)


def get_ticket():
    ticket = r.get("stagUserTicket")
    
    if not ticket:
        raise HTTPException(status_code=401, detail="User ticket not found in cache")

    return ticket.decode("utf-8")
