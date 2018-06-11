/**********************************************************/
//created by: Kelcy Gooch
//Date February 10, 2017
//Compiled and Test using Java version "1.8.0_221"
//Bugs(Explainations below): Server does not output to file
///////////////////////////: Server does not close connection after sending packets back to client
///////////////////////////: Has not been tested on Pluto
/*********************************************************/
import java.net.*;
import java.io.*;
import java.util.*;
import java.lang.*;

public class server {
    public static void main(String[] args) throws IOException {

        //Error Check to make sure correct arguments are given in the command line
        if (args.length != 1) {
            System.err.println("Usage: java Server <port number>");
            System.exit(1);
        }

        int portNumber = Integer.parseInt(args[0]);

        //Creates random integer to be used as the transport socket
        Random ran = new Random();
        int newPortNumber = ran.nextInt(65535) + 1024;

        //Opens the initial Server Socket
        try (
            ServerSocket initserverSocket =
                new ServerSocket(Integer.parseInt(args[0]));
            Socket clientSocket = initserverSocket.accept();
            PrintWriter out =
                new PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(
                new InputStreamReader(clientSocket.getInputStream()));
        )
        {
            String signal;
            signal = in.readLine();
            System.out.println(signal);
            int signalnum = Integer.parseInt(signal);
            if (signalnum == 123){
              System.out.println("Negotiation detected. Selected the following random port: " + newPortNumber);
            }
            out.println(newPortNumber);
            initserverSocket.close();

            // Opens the UDP socket for data transport
            DatagramSocket serverSocket = new DatagramSocket(newPortNumber);
            byte[] receiveData = new byte[4];
            byte[] sendData = new byte[4];
            while(true)
            {
              //Recieves the packet from the client
              DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
              serverSocket.receive(receivePacket);

              String sentence = new String(receivePacket.getData());

              InetAddress IPAddress = receivePacket.getAddress();
              int port = receivePacket.getPort();

              //Capitalizes the given packet
              String capitalizedSentence = sentence.toUpperCase();
              sendData = capitalizedSentence.getBytes();

              //Packs new data and sends to client
              DatagramPacket sendPacket =
                new DatagramPacket(sendData, sendData.length, IPAddress, port);
              serverSocket.send(sendPacket);
              }
              } catch (IOException k) {
                  System.out.println("Exception caught when trying to listen on port "
                    + portNumber + " or listening for a connection");
                  System.out.println(k.getMessage());
                }
        }
}
/* Attempted to write the output to file using FileWriter, BufferedWriter, and
PrintWriter. Was able to write some to file but the stream disconnected after a
few writes. Unsure as to why. */
