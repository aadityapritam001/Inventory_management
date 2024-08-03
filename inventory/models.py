from sqlalchemy import Column, String, Boolean, UUID, ARRAY, Integer, Float
import uuid
from database.db import  Base
from sqlalchemy import inspect

class inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID, primary_key = True, index = True)
    name = Column(String, nullable= False, index = True)
    item_code = Column(String, nullable= True)
    quantity = Column(Integer, nullable = False, default=0)
    rate = Column(Float, nullable = False)
    cost_price = Column(Float, nullable =True)
    description = Column(String, nullable = True)
    is_available = Column(Boolean, default= False)

    def to_dict(self) -> dict:
        """Convert the model to a dictionary.

        :return: Dictionary of the model
        :rtype: dict
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class invoice(Base):
    __tablename__= "invoice"

    id = Column(UUID, primary_key = True, index = True)
    item_id = Column(UUID, foreign_key = True, index = True)
    item_names = Column(String, foreign_key = True, index = True)
    customer_name = Column(String, nullable= False, index = True)
    total_amount = Column(Float, nullable = False)
    discounts = Column(Float, nullable = True)

    def to_dict(self) -> dict:
        """Convert the model to a dictionary.

        :return: Dictionary of the model
        :rtype: dict
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
