# Quarto Tutorial

A hands-on guide to getting started with Quarto, the open-source scientific and technical publishing system.

## What is Quarto?

Quarto is a publishing system for creating scientific and technical content. It allows you to:

- Author with Jupyter notebooks or plain markdown
- Create dynamic content with Python, R, Julia, and Observable
- Publish to HTML, PDF, MS Word, ePub, and more
- Build websites, blogs, presentations, and books

## Setup

Before you begin, make sure Quarto is installed:

```bash
# Check if Quarto is installed
quarto --version

# If not installed, download from https://quarto.org/docs/get-started/
# or use your package manager
```

### Windows
Download the installer from https://quarto.org/docs/get-started/downloads.html

### macOS
```bash
brew install --cask quarto
```

### Linux
Download from https://quarto.org/docs/get-started/downloads.html or use:
```bash
wget https://quarto.org/scripts/quarto.sh
bash quarto.sh
```

## Quick Start Tutorial

### 1. Creating Your First Document

Create a new Quarto document with command:

```bash
quarto create project my_first_doc --type article
```

### 2. Basic Document Structure

Create a markdown file (`example.qmd`). Here's a template:

```
---
title: "My First Quarto Document"
author: "Your Name"
date: today
format: html
---

## Introduction

This is your first Quarto document!

## Add Code Cells

```
```{python}
print("Hello, Quarto!")
```
```

### 3. Rendering Your Document

To generate the output:

```bash
quarto render example.qmd
```

This creates an `example.html` file you can open in your browser.

### 4. Publishing to Different Formats

Quarto lets you target multiple formats from the same source:

```yaml
---
title: "Multi-Format Document"
format:
  html:
    theme: cosmo
  pdf:
    latex-engine: xelatex
---
```

Render with:
```bash
quarto render example.qmd
```

### 5. Creating a Website

Create a Quarto website:

```bash
quarto create site my-website --blank-structure
```

The site will be organized with:
- `_quarto.yml` - site configuration
- `index.qmd` - home page
- `content/` - your pages

### 6. Using Jupyter Notebooks

Quarto renders standard Jupyter notebooks with enhanced features:

```bash
quarto render notebook.ipynb
```

## Advanced Features

### Code Folds and Panels

```yaml
format:
  html:
    code-fold: true
    fig-width: 8
    fig-height: 6
```

### Citations and References

Create a `bibliography.bib` file and reference it in your document with `@citationKey`.

### Callouts

```markdown
::: {.callout-note}
This is an important note!
:::
```

## Next Steps

- Learn more: https://quarto.org/docs/guide/
- Examples: https://quarto.org/docs/gallery/
- Community help: https://github.com/quarto-dev/quarto-cli/discussions
- Report issues: https://github.com/quarto-dev/quarto-cli/issues

## License

This tutorial is licensed under MIT.
