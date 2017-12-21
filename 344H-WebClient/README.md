# [2017-12-15] Challenge #344 [Hard] Write a Web Client
Today's challenge is simple: write a web client from scratch. Requirements:

* Given an HTTP URL (no need to support TLS or HTTPS), fetch the content using a GET request
* Display the content on the console (a'la curl)
* Exit

For the challenge, your requirements are similar to the HTTP server challenge - implement a thing you use often from scratch instead of using your language's built in functionality:

* You may not use any of your language's built in web client functionality or any third party library or tool. E.g. you can't use Python's `urllib`, `httplib`, or a third-party module like `requests` or `curl`. Same for any other language and their built in features; you may also not shell out to something like `curl` (e.g. no `system("curl %s", url))`. 
* Your program should use string processing calls to dissect the URL (again, you cannot use any of the built in functionality like Python's `urlparse` module or Java's `java.net.URL`, or third-party URL parsing libraries like HTParse).
* Your program should support non-standard ports (for instance http://server.io:8080/).
* Your program does NOT need to support TLS or SSL. 
* Your program should use low level `socket()` calls (or equivalent) to connect to the server, and make a well-formatted HTTP/1.1 request. That's the whole point of the challenge!

## Source
https://www.reddit.com/r/dailyprogrammer/comments/7jzy8k/20171215_challenge_344_hard_write_a_web_client/

## Notes
I used the following links to understand the HTTP format and how to specify a HTTP Get request:

https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
https://www.jmarshall.com/easy/http/

I used the Python manual pages for the socket module to understand how to properly use sockets.
