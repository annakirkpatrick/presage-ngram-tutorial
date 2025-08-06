# Selecting training data

Your training data must be in plain text format with utf-8 encoding.  It may be in one big txt file or many smaller files. 

In picking training data, consider the following: 
* Good training data will be as close as possible to the type of text the user wants to generate with the system. A corpus of the user's own writing is ideal. If using other text, consider style and vocabulary when picking training text.
* Data should represent the breadth of the intended use. For example, I'm using Presage for personal and professional written communication, as well as technical writing. It wouldn't make sense for me to use a language model trained only on my Github issues and comments. (Though the sample data is exactly this, my real language model incorporates several other data sources such as emails and school assignments.)
* Data should not include text (especially repeated text) that is not going to be entered with the assistive tech system. For example, email signatures should be removed before using emails as training data. The cleaning scripts included with this tutorial do include options for removing urls, email addresses, and social media handles. So, it's OK if your training data has these.
* In general, more data is better, as long as it is high-quality.  To give a little more guidance:
  * I saw diminishing returns for data beyond about a million characters, or about 1Mb of utf-8 encoded text. 
  * I saw substantial improvements over the included English-language N-gram model with only about 200,000 characters of training data. So, building a custom model for a user may still be very valuable with smaller training datasets.

# Optional: Set some data aside for testing

If you just want to build a model from your training corpus and don't intend to experiment with different training text or parameter values, you can skip this section.

Presage has tools that you can use to assess the quality of your models and other parameters. If you want to make use of these, you might consider one of the following strategies:

1. If you're training on a large corpus of text from the user, consider setting aside (preferably a random) 10-30% of the data as "testing" data. Use the remaining data for training the N-gram model.
2. If you only have a small amount of text written by the user and intend to incorporate other training data sources, consider using the text written by the user as testing data and only training on other sources. The user-supplied testing data can help you identify the best training data.
3. If you're creating a new N-gram model to support a new language, consider setting aside (preferably a random) 10-20% of the data as "testing" data. Use the remaining data for training the N-gram model.

# Put your training text in the right spot 

Make sure your training text data is in one or more plain text files, and copy those files into `data\raw`.

Alternatively, if you want to run through this tutorial with the provided sample training text, copy the contents of `sample_data` into `data\raw`.

# Combining training data

In many cases, your training data will be in multiple plain text files. This step combines all the data into a single plain text file.

The `text_merge.py` script takes two parameters: the input directory of plain text files, and an output file path where the concatenated text should be written.

For this tutorial, we'll read from `data\raw` and write to `data\intermediate\combined_text.txt`:
```
python .\scripts\text_merge.py .\data\raw .\data\intermediate\combined_text.txt
```

# Remove unwanted text elements
Strictly speaking, this step is optional, but it is recommend if your training data has any of the elements in the table below.

In most cases, there will be some parts of your text that you don't want to use as part of the training data for your N-gram model. 

By default, the `remove_unwanted_entities.py` script removes the following.

| Element | Example | Reason for removing |
| ------- | -------- | ------------------ |
| URLs | www.google.com | Usually not typed out (generally would use copy and paste or application-level autocomplete) |
| Reddit-style usernames | u/username | Usually not typed out (generally would use completion within Reddit UI) |
| @-style usernames | @username | Usually not typed out (generally would use completion within website UI) |
| email addresses | somebody@domain.com | Usually not typed out (generally would use copy and paste or application-level autocomplete) |
| contractions and possessives | haven't | Presage's N-gram  builder automatically strips out punctuation including apostrophes (and this isn't easily configurable). So, "haven't" is learned incorrectly as "haven" and "t". Note: Presage can learn contractions and possessives from user input. Additional note: A better way to handle contractions would probably be to expand them, e.g. haven't -> have not|

The script takes 2 arguments: an input file to read text from, and an output file to write text to.

To run the script:

```
python .\scripts\remove_unwanted_elements.py .\data\intermediate\combined_text.txt .\data\intermediate\cleaned_text.txt
```

Your training text is now ready to build an N-gram model.

# Notes on preprocessing:
A few notes:
- It is not necessary to remove punctuation from the training text. Presage's `text2ngram` tool (which we will use in the next step) handles this automatically.
- Similarly, we don't need to convert text to lower case. `Text2ngram` has an option to handle this for us.
- Strictly speaking, it is not necessary to combine the training text into one large file, as `text2ngram` will accept multiple input files. I've chosen to combine all training text because it makes both the text cleaning step and the actual N-gram training simplier to explain.

You are now ready to proceed to [Section 3: Model Training](./3_model_training.md).