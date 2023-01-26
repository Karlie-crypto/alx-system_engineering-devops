Project Name

0x04. Loops, conditions and parsing

Author's Details.

Name: Karlie Moyo

Email: karlieemoyo@gmail.com

Tel: +27 844775229

Requirements
Bash Scripts

    Allowed editors: vi, vim, emacs.
    All your files will be tested on Ubuntu 20.04 LTS.
    All your files should end with a new line.
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash.
    All your bash scripts must be executable.
    You are not allowed to use awk.
    Your Bash script must pass shellcheck without any error.
    The second line of all your Bash scripts should be a comment explaining what is the script doing.

Project Description.

Learn how to create SSH keys. What is the advantage of using #!/usr/bin/env bash over #!/bin/bash. How to use while, until and for loops. How to use if, else, elif and case condition statements. How to use the cut command. What are files and other comparison operators, and how to use them.

    0. Create a SSH RSA key pair - Create a RSA key pair. - 0-RSA_public_key.pub.
    1. For Best School loops - Write a Bash script that displays Best School 10 times. - 1-for_best_school.
    2. While Best School loop - Write a Bash script that displays Best School 10 times. - 2-while_best_school.
    3. Until Best School loop - Write a Bash script that displays Best School 10 times. - 3-until_best_school.
    4. If 9, say Hi! - Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line. - 4-if_9_say_hi.
    5. 4 bad luck, 8 is your chance - Write a Bash script that loops from 1 to 10 with the given requirements. - 5-4_bad_luck_8_is_your_chance.
    6. Superstitious numbers - Write a Bash script that loops from 1 to 20 with the given requirements. - 6-superstitious_numbers.
    7. Clock - Write a Bash script that displays the time for 12 hours and 59 minutes with the given requirements. - 7-clock.
    8. For ls - Write a Bash script that displays The content of the current directory in a list format where only the part of the name after the first dash is displayed with the given requirements. - 8-for_ls.
    9. To file, or not to file - Write a Bash script that gives you information about the school file with the given requirements. - 9-to_file_or_not_to_file.
    10. FizzBuzz - Write a Bash script that displays numbers from 1 to 100 with the given requirements. - 10-fizzbuzz.

    11. Read and cut - Write a Bash script that displays the content of the file /etc/passwd: username, id and home directory path for the user. - 100-read_and_cut.

    karlie@ubuntu$ cat /etc/passwd
    root:x:0:0:root:/root:/bin/bash
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    karlie@ubuntu$ ./100-read_and_cut
    root:0:/root
    daemon:1:/usr/sbin
    bin:2:/bin
    sys:3:/dev
    sync:4:/bin
    games:5:/usr/games
    man:6:/var/cache/man
    lp:7:/var/spool/lpd
    mail:8:/var/mail
    news:9:/var/spool/news

    12. Tell the story of passwd - Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS. - 101-tell_the_story_of_passwd.

    Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO

    13. Let's parse Apache logs - Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file. - 102-lets_parse_apache_logs.

    karlie@ubuntu$ ./102-lets_parse_apache_logs | tail -n 10
    185.130.5.207 301
    185.130.5.207 301
    

Collaborate

To collaborate, reach me through my email address Karlieemoyo@gmail.com
