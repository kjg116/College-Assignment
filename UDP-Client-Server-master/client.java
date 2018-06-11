/**********************************************************/
//created by: Kelcy Gooch
//Date: February 10, 2017
//Bugs (Explainations below): The last packet sent to sever is incorrect
/*********************************************************/
import java.io.*;
import java.net.*;
import java.util.*;
import java.lang.*;

public class client {
    public static void main(String[] args) throws IOException {

        //Error Check to make sure correct arguments are given in the command line
        if (args.length != 3) {
            System.err.println(
                "Usage: java Client <host name> <port number> <filename>");
            System.exit(1);
        }

        String hostName = args[0];
        int portNumber = Integer.parseInt(args[1]);
        String filename = args[2];

        //Opens inital Client Socket for Negotiation
        try (
            Socket initClientSocket = new Socket(hostName, portNumber);
            PrintWriter out =
                new PrintWriter(initClientSocket.getOutputStream(), true);
            BufferedReader in =
                new BufferedReader(
                    new InputStreamReader(initClientSocket.getInputStream()));
            BufferedReader stdIn =
                new BufferedReader(
                    new InputStreamReader(System.in));
        ) {
          System.out.println();
          //Sends Negotiation code to server
          out.println("123");
          // Recieves New Port Number
          String newPort = in.readLine();
          System.out.println("Random Port: " + newPort);
          System.out.println();
          int newPortNumber = Integer.parseInt(newPort);
          //Closes initial socket
          initClientSocket.close();

          //Initializes UPD Socket
          DatagramSocket clientSocket = new DatagramSocket();

          InetAddress IPAddress = InetAddress.getByName(hostName);

          byte[] sendData = new byte[4];
          byte[] receiveData = new byte[4];

          //Initializes file reader
          FileReader reader = new FileReader(filename);
          int c = 0;
          String packet = "";
          int count = 1;

          //Starts file reader
          while((c = reader.read()) != -1){
            // Packs 4 Character from file
            if(count % 4 != 0){
              packet = packet.concat(Character.toString((char) c));
              count++;
            } else {
                //Sends Packed Data to Server
                packet = packet.concat(Character.toString((char) c));
                sendData = packet.getBytes();

                //Creates new Datagram Packet
                DatagramPacket sendPacket =
                  new DatagramPacket(sendData, sendData.length, IPAddress, newPortNumber);
                clientSocket.send(sendPacket);

                //Initializes to recieve acknowledgement from server
                DatagramPacket receivePacket =
                  new DatagramPacket(receiveData, receiveData.length);
                clientSocket.receive(receivePacket);

                //Prints modified Sentence to the screen
                String modifiedSentence =
                  new String(receivePacket.getData());
                System.out.println(modifiedSentence);

                packet = "";
                count++;
            }
          }

          //initializes last packet
          String lastpacket = packet;
          System.out.println(lastpacket);

          byte[] sendlastData = new byte[lastpacket.length()];

          sendlastData = lastpacket.getBytes();

          DatagramPacket sendlastPacket =
            new DatagramPacket(sendlastData, sendlastData.length, IPAddress, newPortNumber);
          clientSocket.send(sendlastPacket);

          DatagramPacket receivePacket =
            new DatagramPacket(receiveData, receiveData.length);
          clientSocket.receive(receivePacket);

          String modifiedSentence =
            new String(receivePacket.getData());
          System.out.println(modifiedSentence);

          // Closes client Socket
          clientSocket.close();

        } catch (UnknownHostException e) {
            System.err.println("Don't know about host " + hostName);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " +
                hostName);
            System.exit(1);
        }
    }
  }
/* The client sends "!ree" instead of "!" for the last packet. I am unsure why it does
this but I've tried to prevent it. */
