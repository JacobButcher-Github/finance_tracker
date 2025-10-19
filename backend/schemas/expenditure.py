# STL
from datetime import date

# UV/PDM
import pydantic


class expenditure(pydantic.BaseModel):
    id: int
    date: date
    category: str
    amount: float
