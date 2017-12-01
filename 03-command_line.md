# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> `pwd`

> `mkdir -p DIR`

> * remove non-empty dir
>> `rm -rf DIR`
> * remove empty dir
>> `rmdir DIR`

> `touch FILE`

> `touch -r REFERENCE_FILE FILE`

> `rm -f FILE`

> `mv OLD_NAME NEW_NAME`

> `ls -a`

> `cp -p SRC_PATH DST_FILE_OR_DIR`

> * Locate certain Python files; e.g. lesson_something_.py:
>> `find . -name 'lesson*.py'`

> * Kill a running Python script; e.g. my_script.py
>> `pkill -f 'python.*my_script.py'`


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>List all regular files in the current dir

>List all files (regular + .hidden) in the current dir

>List all regular files, long format
>List all regulat files, long format with size in B(ytes), K(Bytes), M(Bytes), etc. whichever appropriate

>Like the above, include hidden files

>List sorted by the modification timestamp, newest first

>List using colors, in long format, with trailing / after dir names

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>* List all files on long format on chronological order
>> `ls -alrt`

>* Display special chars in file names as escape sequences
>> `ls -b`


---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

```
 NAME
      xargs -- construct argument list(s) and execute utility
 
 SYNOPSIS
      xargs [-0opt] [-E eofstr] [-I replstr [-R replacements]] [-J replstr]
            [-L number] [-n number [-x]] [-P maxprocs] [-s size]
            [utility [argument ...]]
 
 DESCRIPTION
      The xargs utility reads space, tab, newline and end-of-file delimited
      strings from the standard input and executes utility with the strings as
      arguments.
```

>Example: list file names containin a specific pattern
>
>`find . -name '*.txt' | xargs -n 20 grep -l PATTERN`
>
>xargs will batch the output from find into groups of 20 files at a time. This
>is more efficient than 
>
>`find . -name '*.txt' -exec grep -l PATTERN '{}' ';'` 
>
>which would invoke grep for each file and more robust than
>
>```grep PATTERN `find . -name '*.txt'````
>
>because the command substitution output may exceed the maximum number/size of
>arguments (there could be millions of files).

 

