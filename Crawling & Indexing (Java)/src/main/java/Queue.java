import java.util.ArrayList;

public class Queue {

	private ArrayList<Node> array;
	private int start;
	private int end;
	
	//Constructor
	public Queue(){this.start = -1; this.end = -1;array = new ArrayList<Node>();}
	
	//Getters and Setters
	public ArrayList<Node> getArray(){ return this.array; }
	public void setArrray(ArrayList<Node> arr){ this.array = arr; }
	public int getStart(){ return start; }
	public void setStart(int start){ this.start = start; }
	public int getEnd(){ return end; }
	public void setEnd(int end){ this.end = end; }
	
	//operations
	public void push(Node node){
		if(start==-1 && end==-1){
			start=0;end=0;
			array.add(node);
		}
		else{
			array.add(node);
			end = array.size()-1;
			//System.out.println(node.getUrl()+" added to Queue at "+end);
		}
	}
	public String pop(){
		if(start == -1 || end == -1){
			return "Queue Empty";
		}
		Node returnNode = array.get(start);
		array.set(start, null);
		return returnNode.getUrl();
	}
	
}
