Feedbacks :
---
* Try to store the data in a proper location. Some of your folder name eg. `python;pandas` is not a good name.
* Good that you saved the data by day but again the file name eg. `questionsofpython12_46_21.923203.json` does not look good.
* Try to have meaningful names for file and multiple files for each of the json instead of one json containing 1000 other jsons/
* Try to have proper column names in output files.

```python
cwd = os.getcwd()                           <- Not a good way.

newpath =  cwd + '//' + 'stackoverflow'     <- Use os.join instead.
```




