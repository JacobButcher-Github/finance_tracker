# STL
from datetime import date

# UV/PDM
import pydantic


class Expenditure(pydantic.BaseModel):
    id: int
    date: date
    category: str
    amount: float
