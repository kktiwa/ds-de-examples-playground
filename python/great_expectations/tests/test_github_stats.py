import great_expectations as ge
import pandas as pd
from custom_expectations.expect_column_values_to_not_be_future_date import MyCustomPandasDataset


def test_clones_is_not_null():
    source_github_stats_df = pd.read_csv("../data/github_stats.csv")
    ge_github_stats_df = ge.from_pandas(source_github_stats_df)
    expect = ge_github_stats_df.expect_column_values_to_not_be_null(column="clones")
    assert expect.success


def test_repo_name_should_contain():
    ge_github_stats_df = ge.read_csv("../data/github_stats.csv")
    expect = ge_github_stats_df.expect_column_values_to_match_regex(column="repo_name", regex="[qxf2/]+")
    assert expect.success


def test_fork_value_to_be_increasing():
    ge_github_stats_df = ge.read_csv("../data/github_stats.csv")
    ge_github_stats_df.sort_values(by="forks", inplace=True, ascending=True)
    expect = ge_github_stats_df.expect_column_values_to_be_increasing(column="forks")
    assert expect.success


def test_date_should_not_be_future():
    ge_github_stats_df = ge.read_csv("../data/github_stats.csv", dataset_class=MyCustomPandasDataset)
    expect = ge_github_stats_df.expect_column_values_to_not_be_future_date(column="date")
    assert expect.success
