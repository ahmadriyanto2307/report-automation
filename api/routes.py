from fastapi import APIRouter
from api.models import ProcessRequest

router = APIRouter()


@router.get("/")
def root():
    return {
        "status": "OK",
        "project": "Report Automation"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/process")
def process(req: ProcessRequest):
    return {
        "success": True,
        "type": "dashboard",
        "data": {
            "management_cpu": "8%",
            "dataplane_cpu": "4%"
        }
    }