# Clone the repository

In Powershell, navigate to a location on your file system where you want to keep your work.  

```
cd C:\path\to\project\directory
```

Then, clone this repository. This will create a local copy of this tutorial along with all the scripts and sample data.

```
git clone https://github.com/annakirkpatrick/presage-ngram-tutorial.git
```

# Set up folder structure

To keep things organized, the scripts use a data folder with the following  subfolders:
```
data
- raw
- intermediate
- model
```

These folders are used for the following:

- `raw` is where you will put your training text files.
- `intermediate` holds various intermediate results from text preprocessing.
- `models` holds the N-gram models

To create these folders, we will navigate to the scripts directory:
```
cd presage-ngram-tutorial\scripts
```
Then run `create_data_dirs.py`:
```
python .\create_data_dirs.py
```