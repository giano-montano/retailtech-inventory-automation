# RetailTech Inventory Agent

## 1. Project Context

RetailTech S.A. is an appliance retail company with:

* 25 stores nationwide.
* More than 50,000 active SKUs.
* 3 main distribution centers: Lima, Arequipa, and Trujillo.
* A legacy ERP system with limited API access.
* Manual inventory reconciliation processes.
* A team of 8 operations analysts.

The goal of this project is to build an AI agent with Claude Code that helps automate inventory management and analysis tasks.

## 2. Agent Objective

The agent should help with:

* Analyzing inventory data.
* Identifying products with critical stock levels.
* Generating inventory reports.
* Suggesting replenishment quantities.
* Generating inventory and supplier alerts.
* Analyzing inventory patterns and trends.
* Consolidating inventory KPIs to support decision-making.

The agent's recommendations must be based on the available data and the business rules defined in this document.

## 3. Technology Stack and Data Sources

Main technologies and data formats:

* CSV for inventory data and data exports.
* Excel for information coming from existing business processes.
* SQLite 3 for system data exports.
* Claude Code as the automation agent.

The ERP should be treated as an external data source. The agent will primarily work with exported data and should not assume direct access to the ERP APIs.

## 4. Data Structure

The expected main data files are:

* `data/inventario.csv`: current stock by store.
* `data/ventas.csv`: sales history for the last 12 months.
* `data/proveedores.csv`: supplier information.
* `data/ordenes.csv`: issued purchase orders.
* `data/inventario_muestra.csv`: sample inventory data used for the initial exercises.

Input files must be treated as source data.

## 5. Business Rules

### Minimum Stock

The reference minimum stock level is 20% of the average monthly sales.

A product should be considered below the minimum stock level when:

`current_stock < 0.2 × average_monthly_sales`

### Lead Time

Supplier lead times normally range from 7 to 21 days, depending on the product category.

### ABC Classification

Products should be prioritized according to their inventory value:

* Class A: products representing more than 70% of the inventory value.
* Class B: products representing between 20% and 70%.
* Class C: products representing less than 20%.

### Review Frequency

* Class A products: reviewed daily.
* Class B and C products: reviewed weekly.

### Inventory Reconciliation

When comparing different inventory sources, a discrepancy greater than 2% should be considered significant and reported for review.

## 6. Conventions

### Files

* Input data must be stored in `data/`.
* Generated results must be stored in `output/`.
* Generated filenames should be descriptive.
* When appropriate, include the date or timestamp in generated report filenames.

### Data

* Do not assume that a missing value means zero.
* Validate columns and data types before performing calculations.
* Preserve the original units of measurement.
* Report any inconsistencies found in source files.

### Reports

Reports should include, when applicable:

* Executive summary.
* Affected products or categories.
* Relevant metrics.
* Prioritization.
* Actionable recommendations.
* Generation date.

## 7. Important Constraints

* DO NOT modify source files located in `data/` directly.
* DO NOT overwrite original data.
* All reports and generated results must be stored in `output/`.
* Email alerts must be simulated using `.log` files; do not send real emails.
* Do not invent information that is not present in the data or business rules.
* If required data is missing, explicitly state what is missing.
* Ask for confirmation before performing destructive or irreversible operations.

## 8. Inventory Analysis Workflow

When an inventory analysis is requested:

1. Identify the relevant data files.
2. Inspect their structure and validate the available columns.
3. Validate data quality before performing calculations.
4. Apply the business rules defined in this document.
5. Prioritize the results according to their potential impact.
6. Generate the corresponding output files in `output/`.
7. Show the user a summary of the main findings.
8. Clearly distinguish between observed data and generated recommendations.

## 9. Recommendation Criteria

When data is available, replenishment recommendations should consider:

* Current stock.
* Average sales.
* Days of inventory coverage.
* Minimum stock level.
* Supplier lead time.
* ABC priority.
* Stockout risk.

Every recommendation should briefly explain why the product was prioritized.

## 10. Commands and Common Operations

The project may include commands for:

* Generating a critical inventory report.
* Generating stock alerts.
* Generating purchase order suggestions.
* Reconciling inventory across stores and data sources.
* Generating an inventory KPI dashboard.

All commands must follow the rules and constraints defined in this document.

## 11. General Principles

Always prioritize:

1. Data integrity.
2. Result traceability.
3. Compliance with business rules.
4. Clear and understandable reports.
5. Actionable recommendations.

If a user request conflicts with an explicit constraint in this document, identify the conflict before modifying source data or performing a potentially destructive operation.
