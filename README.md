# Human Randomness Project
People are notoriously bad at generating random numbers. While this is a problem for algorithms that rely on the "true" randomness of numbers for their security or effectiveness, there is great value in being able to generate or predict human-like random numbers. Applications span from guessing stock-market changes, to generating human-like music, and many more.

## The datasets

The two main datasets I am currently working towards are strings of human generated digits (0-9), and mental coin flips ('t' or 'h'). All datasets are entered at the keyboard of a laptop or desktop computer. The digit strings are further divided into three categories: 

- one finger (the index finger of the dominant hand)
- two fingers (both index fingers)
- all fingers (all fingers of both hands. "keyboard smashing", if you will)

## How we built them
Amazon Mechanical Turk is so cool guys. You give Amazon $2.50 and all of a sudden you have strangers generating quality "random" data for you. This raw data is found in the raw_data folder.
