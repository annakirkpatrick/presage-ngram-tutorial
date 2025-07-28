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

# Repository structure and getting started
