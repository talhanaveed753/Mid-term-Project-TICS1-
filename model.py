from pydantic import BaseModel
from datetime import date
from typing import Optional


# Define the Expense class which inherits from Pydantic's BaseModel
# This class represents the data structure of an expense record
class Expense(BaseModel):
    id: int
    date: date
    category: str
    amount: float
    description: str


# Define the ExpenseRequest class for handling the data when adding or updating expenses
# This class is similar to Expense but tailored for incoming HTTP request validation
class ExpenseRequest(BaseModel):
    date: date
    category: str
    amount: float
    description: Optional[str] = None
