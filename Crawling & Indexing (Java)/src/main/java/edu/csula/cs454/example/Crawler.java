package edu.csula.cs454.example;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class Crawler {
		
	public static void main(String[] args) throws IOException {
		
		Document doc = Jsoup.connect("http://en.wikipedia.org/").get();
		String htmlString = doc.toString();
		
		//System.out.println(htmlString);
		
        Elements links = doc.select("a[href]");

		 print("\nLinks: (%d)", links.size());
	        for (Element link : links) {
	            print(" * a: <%s>  (%s)", link.attr("abs:href"), trim(link.text(), 35));
	        }
	
	}
	
    private static void print(String msg, Object... args) {
        System.out.println(String.format(msg, args));
    }
	
    private static String trim(String s, int width) {
        if (s.length() > width)
            return s.substring(0, width-1) + ".";
        else
            return s;
    }
	
	
	
	
}
	
	/*
	public static void main(String[] args) {
		URL url;
		InputStream is = null;
		BufferedReader br;
		String line;

		try {
			url = new URL("http://www.stackoverflow.com/");
			is = url.openStream(); // throws an IOException
			br = new BufferedReader(new InputStreamReader(is));

			while ((line = br.readLine()) != null) {
				System.out.println(line);
			}
		} catch (MalformedURLException mue) {
			mue.printStackTrace();
		} catch (IOException ioe) {
			ioe.printStackTrace();
		} finally {
			try {
				if (is != null)
					is.close();
			} catch (IOException ioe) {
				// nothing to see here
			}
		}
	}*/

