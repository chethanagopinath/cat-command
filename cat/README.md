# cat-command

### Description
From `man cat`:

> cat -- concatenate and print files

> The cat utility reads files sequentially, writing them to the standard output. The file operands are processed in command-line order. If file is a single dash (`-') or absent, cat reads from the standard input...

### Command examples in demo
```shell
ccat test.txt
head -n1 test.txt | ccat -
ccat test.txt test2.txt
head -n3 test.txt | ccat -n
```

## demo
![cat-command (3)](https://github.com/chethanagopinath/cat-command/assets/10332729/e9f98b94-6f8e-4fcd-b234-a317b8197323)



