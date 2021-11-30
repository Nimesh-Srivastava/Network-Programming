# TCP Chat Room

This is a program to create your own private chat room over the internet.<br>
It uses TCP, hence the name.<br>

***
:warning: **This is a private room, but the data transmission is not encrypted. Be careful what you say and who you talk to.**
***

To host the room, edit the `server.py` to fill in the correct ip address and port number.

For people to join, edit the `client.py` with correct ip address and port number, and send it to people.

There is no limit to the number of people joining the server, however there is a limit on the length<br>
of text message (it is of 1024 Bytes) that can be sent.

**Admin is the only one who can kick and ban other users.**

### Screenshot of working system :
Left side denotes the server, right side denotes 2 clients<br>
<br>
![Screenshot 2021-11-30 at 7 27 31 PM](https://user-images.githubusercontent.com/30381993/144060659-b588a4a1-b843-40ef-b8f9-e555d7c49bef.png)
