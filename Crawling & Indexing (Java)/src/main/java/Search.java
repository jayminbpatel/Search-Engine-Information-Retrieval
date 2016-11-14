import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class Search {
	public static void main(String[] agrs) throws IOException{
		
		String searchQuery = "How";
		
		String url = "http://milinjoshi.xyz/";
		
		BFS bfs = new BFS(url);
		bfs.crawl();
			bfs.printQueue();

	}
}
