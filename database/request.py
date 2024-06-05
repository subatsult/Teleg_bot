from database.models import *
from sqlalchemy import select, update, insert, delete

async def get_departments():
    async with async_session() as session:
        result = await session.scalars(select(Department))
        return result
    
