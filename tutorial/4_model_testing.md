# Why test your model?

Once you've finished the model training in the prior step, you could just hand the model to the intended user and ask them how well it works.

But, if you want to experiment with different training text, different text preprocessing, or different  Presage parameters, then you will want a better way to asssess the performance of your models and configurations.  Presage provides a tool for this: `presage_simulator`.

# Understanding `presage_simulator.exe`

The application `presage_simulator.exe` is a command-line tool included with Presage. It measures performance of Presage (in a specified configuration and with  specified N-gram models) on a given reference benchmark text.  

The executable `presage_simulator.exe` is located in the `bin` directory of your Presage installation. On my computer, the full path is `C:\Program Files\presage\bin\presage_simulator.exe`.



## What does performance mean?

Presage defines performance in terms of a Keystroke Savings Rate (KSR), which describes how many keystrokes are required to write the benchmark text (as a proportion of the required keystrokes without Presage). KSR is calculated as follows:

$$\text{KSR}=\left(1-\frac{k_i + k_s}{k_n}\right) \times 100$$

where 
- $`k_i`$ is the number of actual typed keystrokes (these are the characters used to generate suggestions),
- $`k_s`$ is the number of keystrokes required to select suggestions, and
- $`k_n`$ is the number of keystrokes required to type the text with no prediction.

## Config files

When running Presage as part of an assistive technology application, Presage will read a configuration file, generally located in either your user directory or in the Presage install installation directory. (See the [Presage FAQ](https://github.com/Manouchehri/presage/blob/master/FAQ) for details.)

### The problem with using the default configuration file for testing

The default Presage configuration uses multiple predictors to predict and complete words. These are:
- A `DefaultAbbreviationExpansionPredictor` which expands explicitly-defined abbrevations. 
- A `DefaultSmoothedNgramPredictor` which makes predictions based on N-gram models like the ones we have been building in this tutorial.
- A `UserSmoothedNgramPredictor` which uses an N-gram built from the user's past input to make predictions.  By default, this model is continuously updated with new user input.
- A `DefaultRecencyPredictor` which uses (only) recent user input to make predictions.  This predictor does not learn from user input in a persistent way.

It's important to understand that Presage uses multiple predictors and that we are only creating a model for one of them. If we try to test our models using the default configuration, we are running our new N-gram model, but we are also running the `UserSmoothedNgramPredictor`, which learns from the benchmark text itself. Therefore, running the same benchmark multiple times in a row will give different results!

To address these issues, I have created configuration files that only use a subset of the predictors.  These are located in the `sample_config_files` directory, and full usage instructions are below.

Also, note that these configuration files are intended for testing purposes only. While they would technically work in an assistive technology application, the default Presage configuration will almost always be better.

## Command-line options

The tool `presage_simulator.exe`requires one command-line argument: the benchmark text.  

It also supports several useful options:
- `--config` allows you to specify a configuration file. As explained above, this is usually necessary to get meaningful results.
- `--insensitive` specifies to run the simulation while ignoring case.
- `--quiet` and `--silent` both suppress the printing of the simulation to the terminal. This is usually desirable.
- `--help` and `--version` print the appropriate messages to the terminal.


# Testing your models

## Picking benchmark text
To run `presage_simulator.exe` you must first select some benchmark text.

The benchmark text should be:
- In a plain text file.
- Similar to the text that the user actually wants to write. Ideally, the benchmark text would be something written by the intended user.
- Not included in the training text.

In general, larger  a benchmark text should give a more complete picture of Presage's performance, but it will also take much longer to run. Personally, I ended up using about 25kB of my own writing as benchmark text. This gave nearly identical results when compared to a much larger 120kB benchmark.

## Selecting and modifying a config file

In order to generate  meaningful and repeatable test results, I recommend picking one of the configuration files in `sample_config_files`:

 - `ngram_only.xml` tests the N-gram model in isolation, without any added complexity of other predictors.
 - `ngram+recency.xml` tests the N-gram along with the (non-learning) recency predictor. This is slightly more representative of real-world use, but the results may be harder to interpret. 

 In practice,  I've seen quite similar results from these two configurations. For the rest of these instructions, I will assume you're using `ngram_only.xml`, but setting up simulations with the other configuration is very similar.

  Modifications to `ngram_only.xml`:
  - Required:  Change the path on line 22 to be the path to the db file you generated in step 3.
  - Optional: Change number of suggestions on line 40 to be the number of suggestions available to the user in the assistive technology tool. If you don't know (or you're building a model for multiple users/use cases), then you can leave the Presage default value of 11.

  ## Run `presage_simulator.exe`

  In general, this will look like
  ```
  C:\path\to\presage\bin\presage_simulator.exe --insensitive -- silent --config .\sample_config_files\ngram_only.xml benchmark_text.txt
  ```

  On my machine, the full command is
  ```
  C:\Program` Files\presage\bin\presage_simulator.exe --insensitive --silent --config .\sample_config_files\ngram_only.xml .\data\benchmark_text.txt
  ```

  This command may take several minutes to run, depending on the size of your benchmark text. When it completes, it will give you the KSR, which is a measure of the model's performance.