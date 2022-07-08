# Registrar (CLI)

<!-- A Python CLI program for registrar scraping -->

A scraping and parsing tool for my university registrar, written in **Python** and used via the **command line**.

> This repository was largely rebuilt from an already-existing codebase (_also developed by me_), which did not have a Git history. As such, some commits may appear to be artificial or unusual.

## Packages

- Python 3.9
- Requests
- Beautiful Soup 4

## Difference(s) from original

- Offset cookie handling to `requests.Session` object instead of tracking manually
- Code organized into different classes for [_an attempt at_] clarity
