# Angry Pickle

This repository demonstrates how the Python [pickle](https://docs.python.org/3.5/library/pickle.html) module can be exploited.

**TL;DR:** 

"Never unpickle data received from an untrusted or unauthenticated source."

~ [Python's pickle module documentation](https://docs.python.org/3.5/library/pickle.html)

## Usage
1. Write exploited pickle

    ```python
    # create an exploited pickle that will run the 'ls' command when the pickle is read
    python3 angry_pickle_writer.py
    ```

2. Read exploited pickle

    ```python
    # read the exploited pickle... notice that it will run the 'ls' command when reading the pickle
    python3 angry_pickle_reader.py
    ```

## Resources
- [https://blog.nelhage.com/2011/03/exploiting-pickle/](https://blog.nelhage.com/2011/03/exploiting-pickle/) - This blog was very helpful in explaining how a pickle can be exploited in Python.  The code in this repository was inspired by this article.
- [https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf](https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf) - This is a good discussion related to the expoloitation of the pickle framework.
