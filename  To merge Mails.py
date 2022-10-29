{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0  \
# Python program to mail merger\
# Names are in the file names.txt\
# Body of the mail is in body.txt\
\
# open names.txt for reading\
with open("names.txt", 'r', encoding='utf-8') as names_file:\
\
    # open body.txt for reading\
    with open("body.txt", 'r', encoding='utf-8') as body_file:\
\
        # read entire content of the body\
        body = body_file.read()\
\
        # iterate over names\
        for name in names_file:\
            mail = "Hello " + name.strip() + "\\n" + body\
\
            # write the mails to individual files\
            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:\
                mail_file.write(mail)\
}