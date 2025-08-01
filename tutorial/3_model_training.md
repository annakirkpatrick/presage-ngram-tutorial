# Training the N-gram model

Now that we have finished text preprocessing, we can actually train the N-gram model.

Start by locating where Presage is installed. Typically, the path will be something like `C:\Program Files\presage` (for 64-bit installations) or `C:\Program Files (x86)\presage` (for 32-bit installations).  

Note that, when you paste or type these paths into Powershell, you'll need to escape the space character with a backtick. Fon example, `C:\Program Files\presage` becomes ``C:\Program` Files\presage``.

We're going to run `text2ngram.exe` which is located in the `bin` directory.

Start by navigating to your project directory:
```
cd path\to\project\directory\presage_ngram_tutorial
```

By default, Presage uses N-grams of cardinality 1, 2, and 3. We'll start with  cardinality 1:
```
C:\path\to\presage\bin\text2ngram.exe --format sqlite --lowercase --output .\data\models\custom_n_gram.db -n 1 .\data\intermediate\cleaned_text.txt
```

Fill in the path to Presage on your computer. On my machine, the full command is:
```
C:\Program` Files\presage\bin\text2ngram.exe --format sqlite --lowercase --output .\data\models\custom_n_gram.db -n 1 .\data\intermediate\cleaned_text.txt
```

Then, we'll repeat for cardinalities 2 and 3, adding the `--append` option so we add on to the database. Cardinality 2:
```
C:\path\to\presage\bin\text2ngram.exe --format sqlite --lowercase --output .\data\models\custom_n_gram.db -n 2 --append .\data\intermediate\cleaned_text.txt
```
And cardinality 3:
```
C:\path\to\presage\bin\text2ngram.exe --format sqlite --lowercase --output .\data\models\custom_n_gram.db -n 3 --append .\data\intermediate\cleaned_text.txt
```

If you want to run all 3  cardinalities at once, you can use:
```
for ($n = 1; $n -le 3; $n++) {
    & "C:\path\to\presage\bin\text2ngram.exe" --format sqlite --lowercase --output .\data\models\custom_n_gram.db -n $n --append .\data\intermediate\cleaned_text.txt
}
```

If your goal is a custom N-gram model based on your custom training text, you can stop here. Your new model is `data\models\custom_n_gram.db`.  You might want to copy this into `presage\share` (which will require administrator permissions). Regardless of where you keep your db file, you will need to tell Presage to use it, preferably by using the UI of your assistive technology tool. For example, instructions for selecting an N-gram model (db file) in Optikey are [here](https://github.com/Optikey/Optikey/wiki/Next-word-prediction).

# Explanation of text2ngram options

I used several options with `text2ngram.exe` in the last section without explaining them.  Let's fix that.

The `--format` option specifies the output file format. We use `sqlite` because that is what Presage expects. The documentation claims that `tsv` should generate a plain text tab-separated values file, but, at least in my testing, this just generates an empty file.

The `--lowercase` option treats all text as lowercase when building the N-gram model.  This means that "Strawberry" is treated as the same word as "strawberry", which is what we want in most cases.  Most assistive technology tools have built-in ways to handle capitalization, so we're happy for Presage to only generate lowercase predictions.

The `--output` option specifies the output file name and location.

The `-n` option specifies the cardinality of the N-gram. Note that I've used the short-form `-n` because the long form `--ngrams` would not work for me.

The `--append` option should append to the existing output file, instead of overwriting it. However, in my testing, `text2ngram` seems to always append to the output file and never overwrite it. I've left the `--append` option in the commands both for clarity and because it's possible that `text2ngram` may behave as documented in other situations.  If you want to overwrite a db file, just delete it first.

In addition to the options used here, `text2ngram` also has `--help` and `--version` options which just print the corresponding information to the terminal.
