package homework1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.*;

import org.apache.commons.io.FileUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

/*
* ----------------------------
* Homework 1
* Start with a URL
* Download Documents located atthe URL
* Find all links
* for each links repeat step 1
* -----------------------------
* Homework 2
* Integrate Extractor in Crawler
* Consider Issues and trade-offs
* Write extractor
* Extract files
* Extract Meta data and relavent data
* Store Data
* Run Extractor
 * Data Dump
* Read from Local Storage
* Display
* JSON
*
 * */

class Node {

	private String url;
	private int level;

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public int getLevel() {
		return level;
	}

	public void setLevel(int level) {
		this.level = level;
	}

}

public class BFS {

	ArrayList<Node> mainList;
	int depth;
	String searchQuery;

	public BFS(int depth, String corpus) {

		// create a new mainList
		mainList = new ArrayList<Node>();
		this.depth = depth;

		// create a default node
		Node node = new Node();
		node.setUrl(corpus);
		node.setLevel(0);

		// add default node to list
		mainList.add(node);
	}

	public static void main(String[] args) throws IOException {

		int depth = Integer.parseInt(args[0]);
		BFS bfs = new BFS(depth, args[1]);

		if (depth < 0) {
			System.out.println("Invalid Depth");
		} else if (depth == 0) {
			System.out.println(args[1]);
		} else {

				Document doc = Jsoup.connect(args[1]).get();

				System.out.println("Depth : " + depth);
				System.out.println("Url : " + args[1]);

				bfs.searchQuery = "";
				bfs.crawl();
				bfs.printQueue();
				bfs.extract();

/*					if (args[2].equals("-e")) {
						bfs.extract();
					}*/

		}
	}

	public void crawl() throws IOException {

		// variable to iterate through mainList
		int count = 0;

		while (mainList.get(count).getLevel() < depth && mainList.size() < 1000) {

			System.out.println("Results found :" + mainList.size());

			try {
				ArrayList<Node> childList = getChild(mainList.get(count));
				for (Node node : childList) {
					mainList.add(node);// adding to main list
					System.out.println(node.getLevel() + ":" + node.getUrl() + " added to main ");
				}
			} catch (Exception ex) {
				// ex.printStackTrace();
				continue;
			}

			// increment mainList iterator
			count++;
		}
	}

	public ArrayList<Node> getChild(Node node) throws IOException {

		ArrayList<Node> nodeList = new ArrayList<Node>();

		Document doc = Jsoup.connect(node.getUrl()).get();
		Elements links = doc.select("a[href]");

		// make nodes for each links
		for (Element link : links) {

			Node node1 = new Node();
			node1.setUrl(link.attr("abs:href").toString());
			node1.setLevel(node.getLevel() + 1);

			// Check for duplicates
			Boolean isDuplicate = false;
			for (Node n : mainList) {
				if (n.getUrl().equals(node1.getUrl())) {
					isDuplicate = true;
				}
			}
			for (Node n : nodeList) {
				if (n.getUrl().equals(node1.getUrl())) {
					isDuplicate = true;
				}
			}
			if (!isDuplicate) {
				nodeList.add(node1);// adding to locallist
			}

		}
		return nodeList;
	}

	public void checkForDuplicate(Node node) {
		if (!mainList.contains(node)) {
			mainList.add(node);
		}
	}

	public void printHtml(Node node) throws IOException {
		Document doc = Jsoup.connect(node.getUrl()).get();
		System.out.println(doc);
	}

	public void extract() {

		Document doc;
		File f;

		try {

			for (Node node : mainList) {

				doc = Jsoup.connect(node.getUrl()).get();
				String[] urlSplit = node.getUrl().split("/");
				String fileName = urlSplit[urlSplit.length - 1];
				f = new File("Storage/" + fileName + ".html");
				FileUtils.writeStringToFile(f, doc.outerHtml(), "UTF-8");
			}

		} catch (Exception ex) {

		}
	}

	public void getMetaData(Node node) {
		try {

			Document doc = Jsoup.connect(node.getUrl()).get();
			String loc = doc.location();
			System.out.println(loc);
			String title = doc.title();
			System.out.println(title);

		} catch (Exception ex) {

		}
	}

	public void dump(File dir) {

		try {

			String filePath = "C:/Users/MilinDesktop/Storage";

			File folder = new File(filePath);
			File[] listOfFiles = folder.listFiles();
			String path;
			String line = null;
			for (File fl : listOfFiles) {
				///
				BufferedReader bufferedReader = new BufferedReader(new FileReader(fl));

				StringBuffer stringBuffer = new StringBuffer();

				while ((line = bufferedReader.readLine()) != null) {

					stringBuffer.append(line).append("\n");
				}

				System.out.println(stringBuffer);
			}

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public void printQueue() throws IOException {
		try {

			for (Node node1 : mainList) {
				System.out.println(node1.getLevel() + ":" + node1.getUrl());
				// getMetaData(node1);
			}
			
			try {
			      //create a buffered reader that connects to the console, we use it so we can read lines
			      BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

			      //read a line from the console
			      String lineFromInput = in.readLine();

			      //create an print writer for writing to a file
			      PrintStream out = new PrintStream(new FileOutputStream("output.txt"));
			      System.setOut(out);
			      System.out.println(out);

			      //output to the file a line
			      out.println(lineFromInput);

			      //close the file (VERY IMPORTANT!)
			      out.close();
			   }
			      catch(IOException e1) {
			        System.out.println("Error during reading/writing");
			   }
		} catch (Exception ex) {

		}
	}
}





/*
 * package homework1;
 * 
 * import java.io.File; import java.io.IOException; import java.util.*;
 * 
 * import org.apache.commons.io.FileUtils; import org.jsoup.Jsoup; import
 * org.jsoup.nodes.Document; import org.jsoup.nodes.Element; import
 * org.jsoup.select.Elements;
 * 
 * class Node {
 * 
 * private String url; private int level; public String getUrl() { return url; }
 * public void setUrl(String url) { this.url = url; } public int getLevel() {
 * return level; } public void setLevel(int level) { this.level = level; }
 * 
 * } public class BFS {
 * 
 * public static void main(String[] args) throws IOException{
 * 
 * int depth = Integer.parseInt(args[0]); BFS bfs = new BFS(depth, args[1]);
 * 
 * System.out.println(depth); System.out.println(args[1]);
 * 
 * bfs.crawl(); bfs.printQueue(); bfs.extract(); }
 * 
 * ArrayList<Node> mainList;
 * 
 * int depth;
 * 
 * public BFS(int depth, String corpus){ //create a new mainList mainList = new
 * ArrayList<Node>(); this.depth = depth; //create a default node Node node =
 * new Node(); node.setUrl(corpus); node.setLevel(0);
 * 
 * mainList.add(node); }
 * 
 * public void crawl() throws IOException{
 * 
 * //variable to iterate through mainList int count = 0;
 * 
 * while( mainList.get(count).getLevel() <= depth && mainList.size() < 300){
 * //System.out.println(count+" : count"); try{ ArrayList<Node> childList =
 * getChild(mainList.get(count)); for(Node node : childList){
 * mainList.add(node);//adding to main list //System.out.println(node.getLevel()
 * +":"+node.getUrl()+" added to main "); } } catch(Exception ex){
 * ex.printStackTrace(); continue; }
 * 
 * //increment mainList iterator count++; } } public ArrayList<Node>
 * getChild(Node node) throws IOException{
 * 
 * ArrayList<Node> nodeList = new ArrayList<Node>();
 * 
 * Document doc = Jsoup.connect(node.getUrl()).get(); Elements links =
 * doc.select("a[href]");
 * 
 * //make nodes for each links for (Element link : links) {
 * //System.out.println(link.attr("abs:href").toString()); Node node1 = new
 * Node(); node1.setUrl(link.attr("abs:href").toString()); //node1.setLevel(1);
 * node1.setLevel(node.getLevel()+1); //queue.getArray().add(node1);//adding to
 * main list
 * 
 * //Check for duplicates Boolean isDuplicate = false; for(Node n : mainList){
 * if(n.getUrl().equals(node1.getUrl())){ isDuplicate = true; } } for(Node n :
 * nodeList){ if(n.getUrl().equals(node1.getUrl())){ isDuplicate = true; } }
 * if(!isDuplicate){ nodeList.add(node1);//adding to locallist } } return
 * nodeList; }
 * 
 * 
 * public void printQueue(){ int count = 0; for(Node node1 : mainList){
 * System.out.println(count++ + ") Level: " + node1.getLevel()+", Link: "
 * +node1.getUrl()); } }
 * 
 * 
 * public void extract() throws IOException{
 * 
 * Document doc; File f; File f1 = new File(
 * "C:/Users/Jaymin/Downloads/CS454(Search Engine)/cs454-winter-2016-master/Storage"
 * );
 * 
 * // Dump all existing files dump(f1);
 * 
 * for(Node node : mainList){ doc = Jsoup.connect(node.getUrl()).get(); String[]
 * urlSplit = node.getUrl().split("/"); String fileName =
 * urlSplit[urlSplit.length-1];
 * 
 * //Store all files f = new File("Storage/"+fileName+".html"); try {
 * FileUtils.writeStringToFile(f, doc.outerHtml(), "UTF-8"); } catch (Exception
 * e) {
 * 
 * } } }
 * 
 * void dump(File dir) { for (File file: dir.listFiles()) { if
 * (file.isDirectory()) dump(file); file.delete(); } }
 * 
 * }
 */