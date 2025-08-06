# Introduction and Background

This repository contains a tutorial for building N-gram language models for use with Presage, along with some helpful scripts and sample data.

## What is Presage?

[Presage](https://presage.sourceforge.io/) is a predictive text entry system used by multiple open-source assistive technology projects, including [Optikey](https://optikey.org/) and [ACAT](https://www.intel.com/content/www/us/en/developer/tools/open/acat/overview.html).

Note that Presage combines multiple statistical methods for making predictions, and this tutorial only covers the N-gram models. The [Presage FAQ](https://github.com/Manouchehri/presage/blob/master/FAQ]) indicates that regenerating N-gram models is likely the best way to improve predictive performance.

## Why would I want to train my own language models?

There are  a few reasons you might want to train your own N-gram language models for Presage.

1. You want to use Presage in a language other than English, Spanish, or Italian.

2. You want to improve the performance of Presage on English (or Spanish or Italian) text. Either in general or for a specific user or domain.

The English language N-gram model included with Presage is based on a single novel, _The Picture of Dorian Gray_ by Oscar Wilde, which was published in 1890. The choice of such an old novel was surely deliberate to avoid any copyright issues, but it also means that neither the writing style nor the vocabulary are representative of most present-day writing.  By choosing training text which is more representative of the intended use case (e.g. the user's own past writing), substantial performance gains can be achieved.

As an example, using some of my recent emails as benchmark text, the English language model distributed with Presage achieves a Keystroke Savings Rate (KSR) of 41%. When I trained a custom model on my own writing, I was able to achieve a KSR of 61% on that same benchmark text. This means that, on average, it will take 58 keystrokes to produce 100 characters of text with the old model but only 39 keystrokes to produce those same 100 characters with my new model.  (For more details on testing model performance, please see [Section 4 of the tutorial](./tutorial/4_model_testing.md).)

# Repository structure and getting started

Top-level directories are as follows: 
- `tutorial` contains numbered markdown files comprising the tutorial. These can be viewed on Github or locally (using a local markdown viewer).
- `scripts` contains Python scripts for data preprocessing. These are used in the tutorial.
- `sample_data` contains some sample data that you can use to run through the tutorial before using your own training data.  The sample data is plain text files containing my own issue posts and comments from the Optikey Github repository.
- `sample_config_files` contains two simple configuration files for Presage, useful for testing the performance of your models. Do not use these configurations for actual assistive technology applications.

To get started, go to [the Prerequisites file](tutorial/0_prerequisites.md).