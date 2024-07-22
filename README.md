

# Advanced Programming Course Project

**Instructor:** Prof. Dr. Tobias Schaffer

This repository is part of the Advanced Programming course in the A.I. for Smart Sensors and Actuators program. The exercises are sourced from [Google's Python Course](https://developers.google.com/edu/python/) and focus on coding standards, best practices, and version control using Git.

## Project Overview

**Date Written:** July 2024

**Purpose:** This code was written to complete the assignments for the Advanced Programming course, aimed at improving proficiency in Python, understanding coding standards, and practicing effective version control with Git.

**Author:** [Your Name] (optional)

## Installation Instructions

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/your-repository-name.git
   ```
2. **Navigate to the Project Directory:**
   ```sh
   cd your-repository-name
   ```
3. **Ensure Python 3.11.9 is installed.**

4. **Install Required Libraries:**
   ```sh
   pip install -r requirements.txt
   ```

## Instructions for Running the Scripts

### wordcount.py
1. Change to the appropriate directory.
2. Execute the script with one of the following commands in the terminal:
   - To count all words: `.\google-python-exercises\basic\wordcount.py --count <filename>`
   - To count the top 20 words: `.\google-python-exercises\basic\wordcount.py --topcount <filename>`
   
   Examples:
   ```sh
   .\google-python-exercises\basic\wordcount.py --count alice.txt
   .\google-python-exercises\basic\wordcount.py --topcount small.txt
   ```

### mimic.py
1. Change to the appropriate directory.
2. Run the following command in the terminal:
   ```sh
   .\google-python-exercises\basic\mimic.py <filename>
   ```

   Examples:
   ```sh
   .\google-python-exercises\basic\mimic.py alice.txt
   .\google-python-exercises\basic\mimic.py small.txt
   ```

### babynames.py
1. Change to the appropriate directory.
2. Run the script with the `--summaryfile` argument using the following command in the terminal:
   ```sh
   .\google-python-exercises\babynames\babynames.py --summaryfile <filename>
   ```

   Examples:
   ```sh
   .\google-python-exercises\babynames\babynames.py --summaryfile baby2006.html
   .\google-python-exercises\babynames\babynames.py --summaryfile baby1998.html
   ```

## Tasks to Complete
- [x] Complete `string1.py`
- [x] Complete `string2.py`
- [x] Complete `list1.py`
- [x] Complete `list2.py`
- [x] Complete `wordcount.py`
- [x] Complete `mimic.py`
- [x] Complete `babynames.py`

### Excluded Tasks
- `copyspecial`
- `logpuzzle`

## Version Information
- **Python Version:** 3.11.9
- **Libraries Used:**
  - sys
  - os
  - re

## Git Commit Guidelines
- Use present tense and imperative language.
- Make small and precise commits.
- Examples of good commit messages:
  - `Add project files`
  - `Implement word count functionality`
  - `Fix bug in mimic.py`

## Contribution Guidelines
- Comment your code where necessary.
- Use Markdown styling in the README.md file.
- Focus on creating a meaningful commit history.

## Submission Deadline
- **21.07.24**

