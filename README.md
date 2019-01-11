# Human Randomness Project
People are notoriously bad at generating random numbers. While this is a problem for algorithms that rely on the "true" randomness of numbers for their security or effectiveness, there is great value in being able to generate or predict human-like random numbers. Applications span from anticipating human behavior, to generating human-like music, to many more fields.

## The datasets

The two main datasets I am currently working towards are strings of human generated digits (0-9), and mental coin flips ('t' or 'h'). All datasets are entered at the keyboard of a laptop or desktop computer. The digit strings are further divided into three categories: 

- one finger (the index finger of the dominant hand)
- two fingers (both index fingers)
- all fingers (all fingers of both hands. "keyboard smashing", if you will)

The datasets were compiled with Amazon Mechanical Turk. The exact batch output data is found in the raw_data folder.

## Future direction
There are three directions I would like to take this project, including:

- Generating human-like sequences. This can be trivially accomplished with an rnn I believe.
- Person identification. People make their randomness differently, and it has been [shown](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3632045/) that this could be used for identification. Replicating this experiment with ML instead of their tests would be interesting to see if a reasonable improvement can be made.
	- update: tried this trivially with two 30 char digit-strings, half the examples with both from the same person, and half from different people. A simple classifier could not get more than 60% without overfitting. *need more data!!!!*
	- More meaningful with the current dataset is an example to differentiate robotic random numbers from human random numbers, which the same classifier could accomplish with ~80% accuracy. 
- Making these projects accessible like in [random.org](http://random.org)

