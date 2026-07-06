from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.url import UrlCreate, UrlResponse, UrlAnalytics 
from app.services.url_service import create_short_url, get_original_url,get_url_analytics
from app.core.config import BASE_URL

router = APIRouter()

@router.post("/shorten", response_model=UrlResponse)
def shorten_url(request: UrlCreate,db: Session = Depends(get_db)):
    new_url = create_short_url(db=db,original_url=str(request.url))
    return UrlResponse(short_code=new_url.short_code,short_url=f"{BASE_URL}/{new_url.short_code}")

@router.get("/analytics/{short_code}",response_model=UrlAnalytics)
def get_analytics(short_code: str,db: Session = Depends(get_db)):
    url = get_url_analytics(db=db,short_code=short_code)
    if url is None:
        raise HTTPException(status_code=404,detail="Short URL not found")
    return UrlAnalytics(
    original_url=url.original_url,
    short_code=url.short_code,
    click_count=url.click_count,
    created_at=url.created_at,
    last_accessed_at=url.last_accessed_at,
)

@router.get("/{short_code}")
def redirect_to_original(short_code: str,db: Session = Depends(get_db)):

    url = get_original_url(db=db,short_code=short_code)

    if url is None:
        raise HTTPException(status_code=404,detail="Short URL not found")

    return RedirectResponse(url=url.original_url,status_code=307)