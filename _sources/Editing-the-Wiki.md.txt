# Editing this Documentation

This documentation is built using [sphinx](https://www.sphinx-doc.org/en/master/) and the [myst](https://myst-parser.readthedocs.io/en/latest/) markdown
plugin. Both of these tools have excellent online documentation.

Sphinx is a widely-adopted structured documentation tool, which scales well even for very large projects - for example it 
is used to build [Python's documentation](https://docs.python.org/3/), the [Linux kernel documentation](https://docs.kernel.org/), and 
the [EPICS documentation](https://docs.epics-controls.org/en/latest/).

## Markdown

Markdown is the preferred format, although any format supported by sphinx can be used if needed for example ReST or MediaWiki may be useful if moving documentation from other sources.

For a 3-minute introduction to Markdown see ['Mastering Markdown'](https://guides.github.com/features/mastering-markdown/).

## Page Titles

A top-level heading (e.g. `#` markdown header) is used as the page title. **A page should only have one title** (at the top) - otherwise multiple links to that
page will appear in the navigation structure. Subsections within a page should use sub-headers like `##` or `###`.

The page title is independent from the filename of the markdown file - however, for clarity, choose to use similar titles and
filenames wherever possible.

## Adding & editing pages

For simple edits to existing pages, editing can be done via the github interface. There is an "edit on github" button at
the top of every page, which will take you to the relevant page in github to edit it.

For more complex changes, for example adding new pages, it is recommended to make the changes and test them locally, to make sure
that the navigation structure renders properly.

When adding new pages, carefully consider at what level in the hierarchy the new page should be inserted. In particular, be cautious
about adding pages at the very top level of the documentation - these can very quickly clutter the navigation.

Some sphinx `toctrees` (Table-of-contents trees) are listed explicitly, to promote a natural reading order. Where this is the case,
new pages will need to be added to the `toctree` in the document one level up from where the new page has been added - preserving a 
natural reading order. Sphinx will warn you (and fail the build) if you forget to do this.

## Building the wiki locally

Check out the wiki into `c:\instrument\dev\ibex_developers_manual`:

```shell
cd c:\instrument\dev
git clone https://github.com/ISISComputingGroup/ibex_developers_manual.git
```

Make a python virtual environment containing the wiki's dependencies:

```
cd c:\instrument\dev\ibex_developers_manual
c:\instrument\apps\python3\python.exe -m venv .venv
.venv\Scripts\activate
python -m pip install -e .
```

Build the wiki (rebuilding automatically on changes):

```
sphinx-autobuild doc _build
```

The local wiki will then be available at [http://localhost:8000](http://localhost:8000) in your browser.

If sphinx gets out of sync with changes, you can clear the cached build output and start again by running:

```
rmdir /s /q _build && sphinx-autobuild doc _build
```


## Adding DrawIO Diagram

Create new diagram

1. Visit [DrawIO](https://www.draw.io/) choose `device`
1. Create New Diagram, select type etc.
1. Edit diagram until you are happy
1. choose `File` -> `Export` -> `Png...`
1. Then make sure `Include a copy of my diagram` is ticked
1. Add it to the folder in git, next to the page which will use it

In wiki add to markdown using:

    ![alternative text](<image name>.png)

To edit this just open that png in `draw.io`.

## Images

To add images you need to check out the Wiki and add them manually. The images should go into a folder next to the page which will use them.

```shell
git add some/folder/test.png
git commit -m "Added an image to Using the Wiki page"
git push
```

You can then add the image in markdown using the URL `test.png`:

    ![alternative text](test.png)

## Mermaid Diagrams
Mermaid diagrams can be added using the following syntax (example):
````
```{mermaid}
---
title: Simple sample
---
stateDiagram-v2
    [*] --> Document
    Develop_software --> Document
    Document --> Develop_software
    Develop_software --> Test_software
    Test_software --> Crash
    Crash --> Develop_software
    Test_software --> [*]
```
````

will render as:
```{mermaid}
---
title: Simple sample
---
stateDiagram-v2
    [*] --> Document
    Document --> Develop_software
    Develop_software --> Document
    Develop_software --> Test_software
    Test_software --> Crash
    Crash --> Develop_software
    Test_software --> [*]
```


The Mermaid syntax is documented [here](https://mermaid.js.org/intro/syntax-reference.html).

## Spellchecking

The wiki has a built-in spellchecker, which will automatically run when a commit
is pushed to github.

To run the spellchecker locally, use:

```
sphinx-build -b spelling doc _build
```

There is an additional dictionary of allowed words in `doc/spelling_wordlist.txt`. This
is used for words which we know are spelt correctly, but are not in the default dictionary.

The word list can be kept in order by running `sort_word_list` (which will be available in
the python virtual environment). This is also enforced by CI, and can be checked locally by
running `pytest`. Both of these tools should be run from the top-level of an `ibex_developers_manual`
git checkout - the directory that contains `pyproject.toml`.

Sphinx is strict about capitalisation; where multiple spellings are valid, the word will
need to be added to the word list with each of the valid spellings. An exception is all-lowercase entries in the 
word list - these also allow a variant with an initial capital letter. 

Where a word or product has a preferred stylisation, for example **ActiveMQ** or **LabVIEW**, only that spelling 
should be added to the word list. Proper nouns should not have uncapitalised variants added to the word list.

## Admonitions

Sphinx supports various admonitions, which can be used to draw the reader's attention to
certain topics.

For example:

```
:::{tip}
This is a tip!
:::
```

Will render as:

:::{tip}
This is a tip!
:::

The list of supported admonitions is [on the MyST documentation](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html).

## Removing & deleting pages

When moving pages, it is helpful to add redirects to the new location, so that links external to the wiki continue to
work. To do this, we are using the [`sphinx-reredirects`](https://documatt.com/sphinx-reredirects/usage/) plugin.

When moving a page, add a redirect from the old location to the new location. When deleting a page, add a redirect to
the most suitable alternative documentation. The redirects are configured by the `redirects` key in `doc/conf.py`.
