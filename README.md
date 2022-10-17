# Blockchain Ledger Application

## Description

In this application, we explore how to implement a simple blockchain ledger application. To do so, we will:

- Implement a data class named `Record`
- Modifiy an exisiting class named `Block`
- Implement a Streamlit application that allows us to create entries in our blockchain ledger

## Technologies

This example uses the following technologies:

- **pandas** - pandas is a software library written for the Python programming language for data manipulation and analysis. Please see [pandas documentation](https://pandas.pydata.org/) for more information.
- **dataclasses** - The `dataclasses` module provides a decorator and functions for implementing classes in Python.
- **hashlib** - This module implements a common interface to many different secure hash and message digest algorithms.
- **streamlit** - Streamlit is an open-source Python library that enables developers to quickly create web applications.

## Installation

The required libraries are stored in `requirements.txt`. To install the required libraries, do the following:

1. Open Terminal
2. Type `pip install -r requirements.txt`

## Usage

### Launching the Blockchain Ledger application

To launch the Blockchain Ledger application, perform the following steps:

1. Open Terminal.
2. Navigate to the location of `pychain.py`.
3. Enter `streamlit run pychain.py` at the Terminal prompt.
4. Verify that you can access the Blockchain Ledger application in your browser.

![Alt text](/images/pychain_app.png)

## Contributors

This sample application was authored by:

Quinn Wong (quinn.wong@gmail.com)
LinkedIn: https://www.linkedin.com/in/quinnwong/

## License

The MIT License (MIT)

Copyright (c) 2022 Quinn Wong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
