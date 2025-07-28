# Selecting training data

Your training data must be in plain text format.  It may be in one big txt file or many smaller files. 

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

1. If you're training on a large corpus of text from the user, consider setting aside (preferably a random) 10-20% of the data as "testing" data. Use the remaining data for training the N-gram model.
2. If you only have a small amount of text written by the user and intend to incorporate other training data sources, consider using the text written by the user as testing data and only training on other sources. The user-supplied testing data can help you identify the best training data.
3. If you're creating a new N-gram model to support a new language, consider setting aside (preferably a random) 10-20% of the data as "testing" data. Use the remaining data for training the N-gram model.

# Combining training data

In many cases, your training data will be in multiple plain text files. This step combines all the data into a single plain text file.



