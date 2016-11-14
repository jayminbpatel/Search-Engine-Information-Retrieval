import java.io.IOException;
import java.util.*;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class BFS {
	private Queue queue;

	public BFS(String corpus){
				
		Node node = new Node();
		node.setUrl(corpus);
		node.setLevel(0);
		
		if(!corpus.equals(null)){
			queue = new Queue();
			queue.push(node);
		}
	}
	public void crawl() throws IOException{
		//parse html and get all links
		int count = 0;
		
		while(queue.getArray().get(count).getLevel()<3){
			
			try{
				ArrayList<Node> childList = getChild(queue.getArray().get(count));
				for(Node node : childList){
					System.out.println(node.getUrl() +":"+node.getLevel());
					queue.push(node);//adding to main list

							Object o = null;
							if(queue.getArray().contains(o)){
								
							}
							else{
								
							}

				}
				count++;
			}
			catch(Exception ex){
				System.out.println("Error # ");
				continue;
			}

			if(queue.getArray().size()>823){System.out.println("queue size: "+queue.getArray().size());}
		}
		System.out.println("Crawling done");
	}
	public ArrayList<Node> getChild(Node node) throws IOException{
		ArrayList<Node> nodeList = new ArrayList<Node>();

			Document doc = Jsoup.connect(node.getUrl()).get();
			Elements links = doc.select("a[href]");
			
			//make nodes for each links
			for (Element link : links) {
				//System.out.println(link.attr("abs:href").toString());
				Node node1 = new Node();
				node1.setUrl(link.attr("abs:href").toString());
				//node1.setLevel(1);
				node1.setLevel(node.getLevel()+1);
				//queue.getArray().add(node1);//adding to main list
				nodeList.add(node1);//adding to locallist
			}

		return nodeList;
	}
	public void printHtml(Node node) throws IOException{
		Document doc = Jsoup.connect(node.getUrl()).get();
		System.out.println(doc);	
	}
	public void printQueue(){
		System.out.println("Hi");
		ArrayList<Node> allElements = queue.getArray();
		System.out.println(allElements.size());
		
		for(Node node1 : allElements){
			System.out.println(node1.getLevel()+"::"+node1.getUrl());
		}
	}
}
