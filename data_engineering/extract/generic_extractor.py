import pandas as pd
from sqlalchemy.orm import DeclarativeMeta

from .database import get_session


class GenericExtractor:

    def extract(
        self,
        model: DeclarativeMeta,
    ) -> pd.DataFrame:

        session = get_session()

        try:

            query = session.query(model)

            dataframe = pd.read_sql(
                query.statement,
                session.bind,
            )

            return dataframe

        finally:

            session.close()