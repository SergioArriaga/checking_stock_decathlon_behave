# checking_stock_decathlon
With python and selenium we can check if there are stock in decathlon page for one item given in the URL. STOCK & PRICE

The test results will be negative if there is still no stock. As soon as there is product stock (item passed through URL) the tests result will be OK. The last step confirm the price of the product
A screenshot is saved in /screenshots to be checked later if you want

Examples URL:

- https://www.decathlon.es/es/p/bolsa-vela-tribord-5s/_/R-p-327336?mc=8601203&_adin=11551547647
- https://www.decathlon.es/es/p/rueda-abdominal-crosstraining-musculacion-ab-wheel/_/R-p-167411?mc=8660093&c=AZUL

## Acceptance test preparation

### Prerequisites

You have to change the url in the first step for the product that you want to check

- [Python 3.8 or newer (3.x)](https://www.python.org/downloads/).
- [pip](https://pypi.python.org/pypi/pip).
- [Virtualenv](https://pypi.python.org/pypi/virtualenv).

# **Execution**

#### Test case execution ussing BehaveRunner

After configuring the execution, to run test cases using BehaveRunner,
execute the following command in the test project root directory:

$> cd $PROJECT_HOME/

    $> behave features/ --tags ~@skip

With this command, you will execute:

- all \*.features implemented for backend
- Skipping all Scenarios tagged with "skip".
- using the Behave's configuration params defined
  in behave.ini config file

### Installing dependencies into a VirtualEnv

A Virtual Environment is an isolated working copy of Python which
allows you to work on a specific project without worry of affecting
other projects. It enables multiple side-by-side installations of
Python, one for each project.

1. Create a virtual environment somewhere
   _(virtualenv \$ACCEPTANCE_HOME/VENV)_.
2. Activate the virtual environment
   _(source \$ACCEPTANCE_HOME/VENV/bin/activate)_.
3. Install the requirements for the acceptance tests in the virtual
   environment _(pip install -r requirements.txt --allow-all-external)_.
4. Run acceptance tests.

### Output

All outputs of the executions will be located in the directory
`_output`. Output files could be:

- Logs files
- Evidence files

If you have any doubts, pls don't hesitate to contact me