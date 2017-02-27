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

> > PWD - shows current working directory path
mkdir - creates a directory
rmdir - deletes a directory
touch filename - creates an empty file with the name filename
rm filename - removes a file with the filename filename
mv oldfilename newfilename - renames a file with filename oldfilename to filename newfilename
ls -a - lists all files including hidden files
ls -ld .??* -     /* lists only hidden files
cp filename directoryname/ - copys a file with filename into directory with directoryname
cat > filename.txt - creates a txt file with filename filename and can stream in text. close with ctrl D
man cmdname - displays the manual for a cmd with name command name

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

> > ls lists the contents of a directory
ls -a lists all the contents of a directory
ls -l lists in long format. outputs a total sum of the file sizes
ls -lh lists in long format with unit suffixes for file size
ls -lah lists all contents in long format with unit suffixes for file sizes
ls -t sorts with most recently modified displayed first
ls -Glp lists in long format with colorized output and appends a / to directory names

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -1
ls -t
ls -l
ls -G
ls -a
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs splits an input list into sublists for a command to be executed on it
find . -name '*.c' | xargs grep 'stdlib.h'
*/ This will look up file ending with .c that have stdlib.h inside of them

 

