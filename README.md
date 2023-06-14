# Distributed Computing with Python - MapReduce exercises illustrating Kappa & Lambda Architectures

📚 A course brought to you by the [Data Minded Academy].

## Context

These are the exercises used in the course *Data Pipeline Part 2 at DSTI*.  
The course has been developed by instructors at Data Minded. The
exercises are meant to be completed in the lexicographical order determined by
name of their parent folders. That is, exercises inside the folder `b_foo`
should be completed before those in `c_bar`, but both should come after those
of `a_foo_bar`.

## Course objectives

- Understand the fundamentals of distributed data processing and its application in Big Data Analytics.
- Apply data processing techniques to solve real-world problems in various domains.
- Develop critical thinking and problem-solving skills for designing scalable and efficient data processing systems

## Intended audience

- Familiar with Python and MapReduce paradigm.

## Approach

Lecturer first sets the foundations right for Lambda and Kappa Architectures.

There is a high degree of participation expected from the students: they
will need to write code themselves and reason on topics, so that they can
better retain the knowledge.

Note: this course is not about writing the code possible. There are
many ways to skin a cat, in this course we show one (or sometimes a few), which
should be suitable for the level of the participants.

## Getting started

### Prerequisites
Open a new terminal and make sure you're in the `lambda-kappa-MapReduce` directory. Then, run:

```bash
pip install -r requirements.txt
```

This will install any dependencies you might need to run this project in your virtual environment.


## Exercises

### Simple Map, Filter, Reduce exercises

* Write a function that takes a list of numbers and returns a list with double of each number.  
* Write a function that takes a list of numbers and returns a list with only the even numbers.  
* Write a function that takes a list of strings and returns a list with the strings in uppercase. 
* Write a function that takes a list of numbers and returns the sum of the numbers. 
* Write a function that takes a list of strings and returns a list with the length of each string. 
* Write a function that takes a list of numbers and returns a list with only the numbers greater than 5. 
* Write a function that takes two lists of numbers of the same size and returns a list with the sum of the elements from the two lists at the same position. 
* Write a function that takes a list of numbers and returns a list with only the odd numbers. 
* Write a function that takes a list of numbers and returns the average of the numbers.

source code: [map_filter_reduce.py](exercises/a_simple_map_filter_reduce/map_filter_reduce.py)

In case you want to practice lambda functions, there these 10 exercises that you can solve before moving on to the next 
section: [lambda_exercises.py](exercises/a_simple_map_filter_reduce/lambda_exercises.py)

### Word Count
Write a program using the MapReduce paradigm to count the occurrences of each word in the file.

Implement:
* Map function: split the text into individual words and emit key-value pairs
* Reduce function: aggregate the counts for each word

source file: [text.txt](exercises/resources/text.txt)

source code: [word_count](exercises/b_word_count/word_count.py)

### Log Analysis
Design a MapReduce solution to extract the occurrences of different log levels (INFO, WARNING, ERROR)

source file: [logs.txt](exercises/resources/logs.txt)

source code: [log_level_count.py](exercises/c_log_analytics/log_level_count.py)

### Sales Analysis
Use MapReduce to calculate:
* total sales per product.
* 5 top-selling products (top 5 product, highest quantity sold).

source file: [sales.csv](exercises/resources/sales.csv)

source codes:
* [total_sales_product.py](exercises/d_sales_analysis/total_sales_product.py)
* [top_selling_products.py](exercises/d_sales_analysis/top_selling_products.py)


### EXTRA

Have a look at [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) (Elastic MapReduce). It will be useful for the next classes 
and your evaluation project. You can start playing with it by following this tutorial: [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html)


[Data Minded Academy]: https://www.dataminded.academy/
