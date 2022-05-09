# OSI Model

The Open Systems Interconnect (OSI) model is a conceptual framework that describes networking or telecommunications systems as seven layers, each with its own function and different protocols. In order to accomplish successful communication b/w computers or networks of different architectures, OSI Model was introduced. 

The layers help network pros visualize what is going on within their networks and can help network managers narrow down problems (is it a physical issue or something with the application?), as well as computer programmers (when developing an application, which other layers does it need to work with?). Tech vendors selling new products will often refer to the OSI model to help customers understand which layer their products work with or whether it works “across the stack”.

Let us look at the 7 layers starting from the top-down .

7. Application(software)
Application layer provides services for networking applications with the help of protocols to perform user activities. It is where the application and user communicates. Eg.Application protocol such as SMTP is used if you are sending an email.  

6. Presentation 

This layer receives data from Application layer in the form of collectors and numbers. It formats the data in a way that the receiving application can understand it. It performs translation, data-compression(reduces size of file) and also encryption/decryption if needed.

5. Session

This layer helps in setting up and managing connections enabling sending and receiving of data, followed by termination of sessions/connections. Authentication and authorization are performed in this layer.

4. Transport 
Transport layer controls the reliability of communication through Segmentation (addition of the source and destination port numbers), flow control and error control. This layer adds the transport protocols such as TCP(Transmission control protocol) and UDP (User Datagram Protocol). TCP is used for error handling and sequencing to ensure no data is lost. 

3. Network 
Network layer works for the transmission of the received data segments from 1 computer to another located in different networks. Data units in the network layer are called 'packets'. Functions of this layer include Logical (IP) addressing, routing and path determination. At this stage, the source and destination IP address are added to the data. 


2. Data link
At this layer, the physical addresses are added to the data. The MAC address of the router and the source MAC (Media access control) address of the host is added to the data. This is the source and destination MAC addresses. 


1. Physical 
This is the lowest layer of the OSI Model. It is concerned with electrically or optically transmitting raw unstructured data bits across the network from the physical layer of the sending device to the physical layer of the receiving device. It's key responsibility is to carry the data across physcial hardware such as ethernet cables. Eg. Cables and network interface cards.

So as we send data, each layer will add it's own bit of information. This process is called encapsulation. When we hit the physical layer, the data is transmitted over to the receiving device. The receiving device then starts to decapsulate the data. Data from application layer has been segmented by transport layer; placed into packets by network layer; and framed by data link layer. 

# TCP/IP Model# (TCP stands for Transmission Control Protocol and IP stands for Internet Protocol).

TCP/IP is used to standardize computer networking, even if the computers are from different manufacturers. It is a practical and concise version of the OSI model. It contains four layers, unlike seven layers in the OSI model. 

4. Application
It is closest to the end user. It allows users to interact with other software application. Example of the application layer is an application such as file transfer, email, remote login, etc. Functions of application layer includes identifying communication partners, determining resource availability, synchronizing communication, allowing users to log on to a remote host, providing email services, offering distributed database sources and access global information.

3. Transport
Transport layer builds on the network layer in order to provide data transport from a process on a source system machine to a process on a destination system. It determines how much data should be sent where and at what rate. It helps ensure that data units are delivered error-free and in sequence. Transport layer helps you to control the reliability of a link through flow control, error control, and segmentation or de-segmentation.


2. Internet
It is also known as a network layer. The main work of this layer is to send the packets from any network, and any computer till they reach the destination irrespective of the route they take. Protocols that belong to the network layer are Routing protocols, Multicast group management and Network-layer address assignment.


1. Network access (Data link) 
The physical layer is the place where data is transmitted and received across the physical network. A network interface device, usually a line card, adaptor or port is used to connect the physical wires or fibers to the computer so that it can communicate with other computers. This network interface is assigned an address from the Internet Layer so that it can communicate with devices on other networks.


## Exercise
- The OSI model and its uses.
- The TCP/IP model and its uses.

### Sources
- [OSI Model Explained](https://www.youtube.com/watch?v=vv4y_uOneC0)
- [OSI Model Explained with example](https://www.youtube.com/watch?v=LANW3m7UgWs)
- [TCP/IP Model Explained](https://www.guru99.com/tcp-ip-model.html#:~:text=TCP%2FIP%20Model%20helps%20you,allow%20communication%20over%20large%20distances)
- [OSI vs TCP model](file:///Users/sabarishkandasamysekar/Downloads/TCP_IP%20vs%20OSI%20Model_%20What%E2%80%99s%20the%20Difference_.html)


### Overcome challanges
This exercise had a lot of theortical study and it was interesting to read. 

### Results
- OSI model

![NTW-01OSIstack](../../../00_includes/ntw/ntw-01/i1)

- Working of the OSI model

![NTW-01OSIstack](../../../00_includes/ntw/ntw-01/i2)

- Differences between OSI and TCP/IP Model

![NTW-01OSIstack](../../../00_includes/ntw/ntw-01/i2)


![NTW-01OSIstack](../../../00_includes/ntw/ntw-01/i3)



