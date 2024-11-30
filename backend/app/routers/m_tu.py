from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from typing import Optional, List
from datetime import datetime
from models.m_tu import M_TU  # Assuming M_TU is moved to models/m_tu.py
from db.engine import engine  # Assuming engine is created in db/engine.py

router = APIRouter()

@router.get("/", response_model=List[M_TU])
@router.get("/{TU_CIS}", response_model=M_TU)
def get_m_tu(TU_CIS: Optional[str] = None):
    with Session(engine) as session:
        if TU_CIS:
            statement = select(M_TU).where(M_TU.TU_CIS == TU_CIS)
            result = session.exec(statement).first()
            if not result:
                raise HTTPException(status_code=404, detail="M_TU not found")

            if result.ZALOZENO:
                try:
                    result.ZALOZENO = str(
                        datetime.strptime(result.ZALOZENO, "%Y%m%d%H%M%S.%f")
                    )
                except ValueError:
                    raise HTTPException(
                        status_code=500, detail="Error parsing datetime format"
                    )
            return result
        else:
            statement = select(M_TU)
            results = session.exec(statement).all()

            for record in results:
                if record.ZALOZENO:
                    try:
                        record.ZALOZENO = str(
                            datetime.strptime(record.ZALOZENO, "%Y%m%d%H%M%S.%f")
                        )
                    except ValueError:
                        raise HTTPException(
                            status_code=500, detail="Error parsing datetime format"
                        )
            return results
