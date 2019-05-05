# About this project 

## Goals of the project

This project was one of my first explorations into Python. It showed me how powerful Python really was and helped me learn some key aspects of the language. I have a vested 
interest in Networks as well, because I find Computer Security to be an intriguing topic, I decided to pursue this project to learn more. 

What better way to learn about security than creating your own end to end encryption tool. I had lots of fun making it. The source code is attached in the main repository. 

## Thought process

I wanted to make a encryption function that could be decrypted at the other end. How could I do this? Encryption requires that the plain-text be masked in some way. I 
thought of arrays and how if we could represent the word in an array and loop through that array changing each of the characters via some hashing function, you could 
encrypt the message/password. 

That was great because the converse is also true. Using an array and the same hashing function, you could reverse the encryption. Awesome. 

Now the issue was to come up with a hashing function. 

Well one way to do this is to convert the characters in the array to ASCII and apply a mathematical function as a hashing. That's what I decided to do. Python made it 
really easy, there are functions like _ord()_ which throw each character into ASCII and the _list()_ function which automatically turns strings into char arrays. Crazy 
right?  

## What I learned?

- Hashing functions 
- Encryption 
- Computer Security 
- Python 
- Lists 
- ASCII 

## What I used?

Python

PyCharm IDE 



