from great_expectations.dataset import (
    PandasDataset,
    MetaPandasDataset,
)
from datetime import datetime


class MyCustomPandasDataset(PandasDataset):
    _data_asset_type = "MyCustomPandasDataset"

    @MetaPandasDataset.column_map_expectation
    def expect_column_values_to_not_be_future_date(self, column):
        return column.map(lambda x: datetime.strptime(x, "%d-%b-%Y") <= datetime.today())
