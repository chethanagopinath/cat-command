# wc-command

### Description
From `man wc`:

> wc -- word, line, character, and byte count

> The wc utility displays the number of lines, words, and bytes contained in each input file, or standard input (if no file is specified) to the standard output. A line is defined as a string of characters delimited by a <newline> character. Characters beyond the final <newline> character will not be included in the line count.

> A word is defined as a string of characters delimited by white space characters. White space characters are the set of characters for which the iswspace(3) function returns true. If more than one input file is specified, a line of cumulative counts for all the files is displayed on a separate line after the output for the last file.

### Command examples in demo
```shell
ccwc -c test.txt
ccwc -w test.txt
ccwc -l test.txt
ccwc test.txt
```
(have also partly implemented `ccwc -m test.txt` other than whats on the demo)

### Demo
![wc-command (1)](https://github.com/chethanagopinath/unix-commands-in-python/assets/10332729/5b847d43-d2d7-4a41-9c2c-0f96991c3427)

