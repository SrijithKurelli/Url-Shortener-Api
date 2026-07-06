from sqlalchemy.orm import Session
from app.models.url import Url
from app.utils.generator import generate_short_code
from datetime import datetime, timezone

def create_short_url(db: Session, original_url: str):

    short_code = generate_short_code()
    existing = db.query(Url).filter(Url.short_code == short_code).first()
    while existing is not None:
        short_code = generate_short_code()
        existing = db.query(Url).filter(Url.short_code == short_code).first()

    new_url = Url(original_url=original_url,short_code=short_code)

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url

def get_original_url(db: Session, short_code: str):

    url = (db.query(Url).filter(Url.short_code == short_code).first())

    if url is None:
        return None

    url.click_count += 1
    url.last_accessed_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(url)

    return url

def get_url_analytics(db: Session,short_code: str):
    url = (db.query(Url).filter(Url.short_code == short_code).first())
    if url is None:
        return None

    return url