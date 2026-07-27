from datetime import datetime

import pandas as pd


class PipelineReport:

    def __init__(self):

        self.steps = []

    def add_step(

        self,

        step,

        rows,

        status,

        execution_time,

    ):

        self.steps.append(

            {

                "step": step,

                "rows": rows,

                "status": status,

                "execution_time_sec": execution_time,

                "timestamp": datetime.now(),

            }

        )

    def save(self):

        df = pd.DataFrame(self.steps)

        df.to_excel(

            "pipeline_report.xlsx",

            index=False,

        )

        print()

        print(df)