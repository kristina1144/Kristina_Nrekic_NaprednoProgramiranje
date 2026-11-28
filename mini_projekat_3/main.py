"""Mali API za obracun cijene hotelskog smjestaja."""

import os
from secrets import compare_digest
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field

app = FastAPI(title="Rezervacije API", version="1.0.0")
api_kljuc_header = APIKeyHeader(name="X-API-Key", auto_error=False)


class ZahtjevCijene(BaseModel):
    noci: int = Field(ge=1, le=30)
    cijena_noci: float = Field(gt=0, allow_inf_nan=False)
    popust: float = Field(default=0.0, ge=0, le=1, allow_inf_nan=False)


class OdgovorCijene(BaseModel):
    iznos: float


def provjeri_kljuc(kljuc: Annotated[str | None, Depends(api_kljuc_header)]) -> None:
    ocekivani = os.getenv("API_KEY")
    if not ocekivani:
        raise HTTPException(status_code=503, detail="API kljuc nije podesen")
    if kljuc is None or not compare_digest(kljuc, ocekivani):
        raise HTTPException(status_code=401, detail="Neispravan API kljuc")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/cijena", response_model=OdgovorCijene)
def izracunaj(z: ZahtjevCijene, _: Annotated[None, Depends(provjeri_kljuc)]) -> OdgovorCijene:
    iznos = z.noci * z.cijena_noci * (1 - z.popust)
    if not (float("-inf") < iznos < float("inf")):
        raise HTTPException(status_code=422, detail="Iznos je van dozvoljenog opsega")
    return OdgovorCijene(iznos=round(iznos, 2))
