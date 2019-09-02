# CMU_dict

<br/>

###### Convert an English utterance into pronunciation using [CMU pronouncing dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).



<br/>

###### Files:

cmu_dict.txt --> CMU pronouncing dictionary

LJ_metadata.txt --> the metadata of [LJspeech](https://keithito.com/LJ-Speech-Dataset/)

LJ_output.txt --> the output of LJspeech metadata

text.txt --> another file containing the utterances. If the utterances contain the word beyond the dictionary, it will not be changed.

output.txt --> the output of the text.txt

process.py --> the py file

<br/>

###### How to use:

1. if you want to convert the metadata of LJspeech, LJ_output.txt will be found in the same  catalogue.

```python
python process.py --mode LJ
```

  

2. if you want to convert another text file, output.txt will be found in the same catalogue.

```python
python process.py --mode text
```











