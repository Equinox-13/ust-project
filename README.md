# ust-project

The project is part of the UST Global technical assignment.

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Overview

The repository contains 2 programs:

- Function that generates numbers using a generator which can be divisible by 5 and 7

- Function that interleaves 2 strings

## Directory Structure
- **ust-project/**
  - `inputs/input.txt`: Contains sample inputs
  - `main.py`: Main script file to execute both the programs.
  - `program1.py`: Contains program1 to generate numbers divisible by 5 and 7.
  - `program2.py`: Contains program2 to interleave 2 strings 
  - `test_functions.py`: Contains unit tests for both the programs
  - `README.md`: Project overview, installation, and usage details.
  - `.gitignore`: Specifies intentionally untracked files to ignore in version control.

## Installation
Clone the repository:

```bash
git clone https://github.com/Equinox-13/ust-project 
cd ust-project
```

## Usage
Execute the main.py with default sample inputs.

```bash
python main.py
```
Output:

```commandline
Output from program 1: 0,35,70
Output from program 2: A1A2A3A4567
```

- To provide custom inputs update the `inputs/input.txt` file

## Testing
Run the unit tests using the unittest module 

```bash
python -m unittest test_functions.py
```

