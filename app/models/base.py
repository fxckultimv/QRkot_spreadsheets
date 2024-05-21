from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, CheckConstraint
from const import REPRESENTATION

from app.core.db import Base


class PreBaseDonationCharity(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint(
            'invested_amount >= 0 and full_amount >= invested_amount'
        ),
        CheckConstraint('full_amount > 0'),
    )

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    def repr(self):
        return REPRESENTATION.format(
            full_amount=self.full_amount,
            create_date=self.create_date,
            invested_amount=self.invested_amount,
            close_date=self.close_date if self.close_date else ' --- '
        )
