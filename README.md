# Sales Data Analyzer

In this project, I worked with a small sales dataset and used Python, Pandas, and Matplotlib to understand the data and find useful information from it.

The goal was to take transaction data from a CSV file and turn it into simple business insights and visualizations.

## What it does

The analyzer looks at things such as:

* Total number of orders
* Total quantity of products sold
* Total sales
* Average order value
* Sales by product
* Sales by category
* Best-selling products
* Daily sales
* Highest and lowest sales dates
* Customer spending
* Payment methods
* Top 5 products

It also creates charts to make some of the results easier to understand.

The program generates a `report.txt` file containing the main results of the analysis.

## Tools I used

* Python
* Pandas
* Matplotlib
* CSV
* File handling

## Project structure

```text
sales_data_analyzer/
│
├── data/
│   └── sales.csv
│
├── analyzer.py
│
├── report.txt
│
└── README.md
```

## How it works

The program first reads the sales data from the CSV file.

Then I use Pandas to inspect, calculate, group, filter, and sort the data to find useful information.

Matplotlib is used to create visualizations from the analyzed data.

Finally, the important results are written to `report.txt`.

The basic workflow is:

```text
sales.csv
    ↓
Pandas
    ↓
Data Analysis
    ↓
Matplotlib
    ↓
Visualizations
    ↓
report.txt
```

## What I learned

This project helped me practice using Pandas on a different type of dataset compared to my first project.

I practiced:

* Reading CSV data
* Inspecting a dataset
* Creating calculated columns
* Using `groupby()`
* Filtering data
* Sorting results
* Working with dates
* Finding unique values
* Aggregating data
* Creating bar and line charts with Matplotlib
* Writing results to a text file

I also got more practice thinking about what information might actually be useful from a dataset instead of only calculating numbers.

## Dataset

The dataset used in this project is sample sales data created for learning purposes. It does not contain real customer or business information.

## Possible improvements

There are still many things I could improve in this project, for example:

* Add more visualizations
* Improve the generated report
* Add error handling
* Allow different CSV files to be analyzed
* Make the analysis more reusable
* Build a simple interface in the future

For now, the main goal of this project was to practice taking a dataset from start to finish and turning it into useful information.
