python_import_studies

data_test:       Data used for testing, development, and debugging. Usually small or synthetic data.
data_production: Data used for production
use the symlink data to point to either data_test or data_production
Even though in data_production and data_test, files may have the same name, they may have different content.
This is because data_test is used for testing and development, and data_production is used for production.
- python_import_studies :: Experiment to understand how to deal with Python import with Jupyter code cell with VS Code
