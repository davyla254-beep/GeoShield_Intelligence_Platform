# Contributing to GeoShield Intelligence Platform

Thank you for your interest in contributing to the GeoShield Intelligence Platform.

GeoShield is an Artificial Intelligence and Geospatial Intelligence platform focused on disaster intelligence, environmental monitoring, infrastructure analysis, and decision support. Every contribution should maintain high engineering standards, security, and code quality.

---

# Development Workflow

Development follows the GitHub Issue workflow.

Each feature begins as an Issue.

Workflow:

Backlog

↓

Next Sprint

↓

In Progress

↓

Review

↓

Testing

↓

Completed

No development should begin without an associated GitHub Issue.

---

# Branch Strategy

Main Branch

```
main
```

Contains stable production-ready code.

Feature Branches

```
feature/satellite-manager

feature/gis-engine

feature/dashboard

feature/api

feature/ai-engine
```

Bug Fixes

```
bugfix/fire-detection

bugfix/authentication

bugfix/dashboard
```

Documentation

```
docs/readme-update

docs/api-guide
```

---

# Commit Message Standard

Commit messages should be short and descriptive.

Examples

```
Add satellite manager

Implement GIS spatial engine

Improve disaster intelligence

Fix authentication bug

Optimize database queries

Update API documentation
```

Avoid messages such as

```
Update

Done

Fix

Changes

Test
```

---

# Coding Standards

Python

* Follow PEP 8
* Use descriptive variable names
* Write modular functions
* Avoid duplicated code
* Document public functions

Example

```
calculate_risk_score()

download_satellite_assets()

detect_flood_extent()
```

Instead of

```
calc()

temp()

test()
```

---

# Documentation

Every new module should include documentation where appropriate.

Major features should be reflected in

* README
* ARCHITECTURE
* API documentation
* CHANGELOG

---

# Testing

New functionality should include appropriate tests.

Testing includes

* Unit Tests

* Integration Tests

* API Tests

* Spatial Validation

* AI Model Validation

---

# Pull Requests

Every Pull Request should

* solve one clearly defined problem

* compile successfully

* pass tests

* include documentation updates if required

Large unrelated changes should not be combined into one Pull Request.

---

# Code Review

Before merging, verify

* code quality

* naming consistency

* architecture consistency

* documentation completeness

* security considerations

---

# Repository Structure

Major directories

```
backend/

frontend/

dashboard/

core/

engines/

connectors/

database/

models/

satellites/

data/

docs/

api/

assets/
```

Each module should have a clearly defined responsibility.

---

# Security

Do not commit

* API Keys

* Passwords

* Tokens

* Secrets

* Large raw datasets

* Temporary outputs

Sensitive information must remain outside version control.

---

# Geographic Data

Large GIS datasets should not be committed directly into Git.

Recommended storage

* Cloud Storage

* Object Storage

* External Data Repository

Only lightweight sample datasets should be included in the repository.

---

# Artificial Intelligence

AI modules should

* produce reproducible outputs

* be explainable

* log important decisions

* support future model improvements

---

# Professional Conduct

Contributors are expected to

* communicate respectfully

* document their work

* follow project standards

* maintain professionalism

---

# Maintainer

Project Maintainer

**David Omondi Ouma**

GeoShield Intelligence Platform
