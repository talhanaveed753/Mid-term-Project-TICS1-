from fastapi import APIRouter, Path, HTTPException, status
from model import Expense, ExpenseRequest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

expense_router = APIRouter()

# In-memory list to store expenses; in a production application, this would likely be a database
expense_list = []
max_id: int = 0


# Route to add a new expense, returning the created expense data
@expense_router.post("/expenses", status_code=status.HTTP_201_CREATED)
async def add_expense(expense: ExpenseRequest) -> dict:
    global max_id
    max_id += 1

    # Create a new Expense instance with the incremented ID and data from the request
    newExpense = Expense(id=max_id, **expense.dict())
    expense_list.append(newExpense)
    json_compatible_item_data = jsonable_encoder(newExpense)
    return JSONResponse(content=json_compatible_item_data)


# Route to get all expenses, returning the list of expenses
@expense_router.get("/expenses")
async def get_expenses() -> dict:
    json_compatible_item_data = jsonable_encoder(expense_list)
    return JSONResponse(content=json_compatible_item_data)


# Route to get a specific expense by its ID
@expense_router.get("/expenses/{id}")
async def get_expense_by_id(id: int) -> dict:
    for expense in expense_list:
        if expense.id == id:
            return {"expense": expense}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The expense with ID={id} is not found.",
    )


# Route to update an existing expense by its ID
@expense_router.put("/expenses/{id}")
async def update_expense(expense: ExpenseRequest, id: int) -> dict:
    for x in expense_list:
        if x.id == id:
            x.date = expense.date
            x.category = expense.category
            x.amount = expense.amount
            x.description = expense.description
            return {"message": "Expense updated successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The expense with ID={id} is not found.",
    )


# Route to delete an existing expense by its ID
@expense_router.delete("/expenses/{id}")
async def delete_expense(id: int) -> dict:
    for i in range(len(expense_list)):
        if expense_list[i].id == id:
            expense_list.pop(i)
            return {"message": f"The expense with ID={id} has been deleted."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The expense with ID={id} is not found.",
    )
