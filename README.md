# TexWordCount
The most accesible current method of producing a word count for ```.tex``` files is copying the entire document into an external website which will then process the file. This process can waste a lot of time, and can often not be transparent to the novice user. The programme presented here allows for fast and effient computation of a word count locally, by linking the file to a counting Python script. Additionally, the script has been laid out in such a way as to allow easy editing by even a novice Python user, of which commands and functions they do not wish to be included in the count.

##Getting Started

Clone the repository:
```
git clone https://github.com/JosephPB/TexWordCount
```

##Usage

The programme works by running the Python script followed by the name of the file the user wishes to count:

```
python latexcount.py test.tex
```
and outputs the wordcount to ```wordcount.txt```.

The programme comes with a small shell file ```count.sh```, in which the user can replace ```test.tex``` with their desired file name, to allow for even faster implementation.

That's it!
