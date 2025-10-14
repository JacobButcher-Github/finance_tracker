# STL
from datetime import date

# UV/PDM
import pydantic


class Income(pydantic.BaseModel):
    date: date
    gross: float
    k401: float
    fed_tax: float
    ss_tax: float
    medicare_tax: float
    state_tax: float
    other_income: float
    net_income: float
    total_tax: float
    tax_percent_income: float
