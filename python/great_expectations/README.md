![img_2.png](ge_img.png)

## Great Expectation Code Examples 
This folder contains examples for getting started with a project where you would implement tests using great expectations framework.<br><br>
Great Expectations is a shared, open standard for data quality. It helps data teams eliminate pipeline debt, through data testing, documentation, and profiling.

### Notable Features
- Rich pre-built Expectations which are extensible
- Tests are docs and docs are tests
- Automated data profiling
- Batteries-included data validation

### Example Datasets: There are 2 example datasets (under `data` folder) that can be used for writing tests for:<br> 
- Github Stats
- Citibike Extension

1. ### Install
* A working Python install
* pip package installer for Python
* Create and active a virtual environment using:
```shell
pyenv_project_setup.sh great_expectations
```
* Basic familiarity in using a Jupyter notebook

2. ### Setup
Run the following command to initialize Great Expectations deployment. It will create a folder called great_expectations and build the directory structure and the necessary configuration files inside it:

```shell
great_expectations init
```

3. ### Connect to Data
- Run the following command:
```shell
great_expectations datasource new
```
- Change the name of the datasource to `github_stats_datasource`

4. ### Implement a test
- 4.1. Prepare a test suite
```shell
great_expectations suite new
```
- 4.2. Find a suitable built-in expectation
- 4.3. Create an expectation
- 4.4. Run the test

5. ### Edit suite
```shell
great_expectations suite edit <suite_name>
```

### Resources
- [Python Library to write tests independently](https://pypi.org/project/great-expectations/)
- [Documentation](https://docs.greatexpectations.io/docs/)
- [Data Docs](https://docs.greatexpectations.io/docs/terms/data_docs/)
- [Docker Images](https://docs.greatexpectations.io/docs/guides/miscellaneous/how_to_use_the_great_expectation_docker_images/)
- [Expectations Gallery](https://greatexpectations.io/expectations/)