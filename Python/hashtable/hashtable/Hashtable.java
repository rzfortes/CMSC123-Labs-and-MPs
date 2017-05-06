import java.util.LinkedList;

public class Hashtable {
	
	String closedHashing_htable[] = new String[10];
	LinkedList<String> openHashing_htable[] = new LinkedList[10];

	// default constructor
	public Hashtable() {
		// closed hashing
		for(int i = 0; i < closedHashing_htable.length; i++) {
			closedHashing_htable[i] = null;
		}
		
		// open hashing
		for(int i = 0; i < openHashing_htable.length; i++) {
			openHashing_htable[i] = new LinkedList<String>();
		}
	}
	
	public int hash_function(int i) {
		int h = i % closedHashing_htable.length;
		return h;
	}
	
	// ----------------------- OPEN HASHING ----------------------
	public int openHashing_size() {
		return openHashing_htable.length;
	}
	
	public void openHashing_print() {
		for(int i = 0; i < openHashing_htable.length; i++) {
			System.out.print("Index " + i + ": ");
			for(int y = 0; y < openHashing_htable[i].size(); y++) {
				System.out.print(openHashing_htable[i].get(y) + " ");
			}
			System.out.println();
		}
	}
	
	public void openHashing_insert(int item) {
		int h_index = hash_function(item);
		openHashing_htable[h_index].add(String.valueOf(item));
	}
	
	public void openHashing_search(int item) {
		int h_index = hash_function(item);
		for(int i = 0; i < openHashing_htable[h_index].size(); i++) {
			if(openHashing_htable[h_index].get(i).equals(String.valueOf(item))) {
				System.out.println(item + " found in index " + h_index);
				return;
			}
		}
		System.out.println(item + " does not exists.");
	}
	
	public void openHashing_delete(int item) {
		int h_index = hash_function(item);
		openHashing_htable[h_index].remove(String.valueOf(item));
	}
	
	
	//	----------------------- CLOSED HASHING ----------------------
	public int closedHashing_size() {
		return closedHashing_htable.length;
	}
	
	public void closedHasing_print() {
		for(int i = 0; i < closedHashing_htable.length; i++) {
			System.out.println("Index " + i + ": " + closedHashing_htable[i]);
		}
	}
	
	public void closedHashing_insert(int item) {
		int h_index = hash_function(item);
		if(closedHashing_htable[h_index] == null || closedHashing_htable[h_index] == "inf") {
			closedHashing_htable[h_index] = String.valueOf(item);
		} else {
			// move on to the next until you see an available seat
			for(int i = (h_index + 1); i <= closedHashing_htable.length; i++) {
				// need to wrap around
				if(i == closedHashing_htable.length) {
					i = 0;
				}
				// place here
				if(closedHashing_htable[i] == null) {
					closedHashing_htable[i] = String.valueOf(item);
					break;
				}
			}
		}
	}
	
	public void closedHashing_search(int item) {
		int h_index = hash_function(item);
		if(closedHashing_htable[h_index].equals(String.valueOf(item))) {
			System.out.println(item + " found in index: " + h_index);
		} else {
			// search until you see the item or null
			for(int i = (h_index + 1); i <= closedHashing_htable.length; i++) {
				// need to wrap around
				if(i == closedHashing_htable.length) {
					i = 0;
				}
				// place here
//				System.out.println("index " + i + htable[i] + " equals " + String.valueOf(item));
				if(closedHashing_htable[i] == null) {
					System.out.println(item + " does not exists. ");
					break;
				}
				else if(closedHashing_htable[i].equals(String.valueOf(item))) {
					System.out.println(item + " found in index: " + i);
					break;
				} 
			}
		}
	}
	
	public void closedHashing_delete(int item) {
		int h_index = hash_function(item);
//		System.out.println("h_index: " + h_index + " item: " + htable[h_index]);
		if(closedHashing_htable[h_index].equals(String.valueOf(item))) {
			
			closedHashing_htable[h_index] = "inf";
		} else {
			// search until you see the item or null
			for(int i = (h_index + 1); i <= closedHashing_htable.length; i++) {
				// need to wrap around
				if(i == closedHashing_htable.length) {
					i = 0;
				}
				// place here
				if(closedHashing_htable[i] == null) {
					System.out.println(item + " does not exists. " + i);
					break;
				}
				else if(closedHashing_htable[i].equals(String.valueOf(item))) {
					closedHashing_htable[i] = "inf";
					break;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Hashtable h1 = new Hashtable();
//		System.out.println("Hashtable's size: " + h1.size());
//		System.out.println("BEFORE");
//		h1.closedHashing_insert(39);
//		h1.closedHashing_insert(14);
//		h1.closedHashing_insert(81);
//		h1.closedHashing_insert(112);
//		h1.closedHashing_insert(77);
//		h1.closedHashing_insert(27);
//		h1.closedHashing_insert(78);
//		h1.closedHashing_insert(64);
//		h1.closedHashing_insert(51);
//		h1.print();
//		System.out.println("AFTER");
//		h1.closedHashing_delete(64);
//		h1.closedHashing_delete(51);
//		h1.print();
//		System.out.println("2nd AFTER");
//		h1.closedHashing_search(112);
//		h1.closedHashing_search(64);
//		h1.closedHashing_search(1111);
		// ---------------------------------------------
//		System.out.println(h1.openHashing_size());
		System.out.println("BEFORE");
		h1.openHashing_insert(39);
		h1.openHashing_insert(14);
		h1.openHashing_insert(81);
		h1.openHashing_insert(6);
		h1.openHashing_insert(112);
		h1.openHashing_insert(77);
		h1.openHashing_print();
		System.out.println("AFTER");
		h1.openHashing_insert(27);
		h1.openHashing_insert(78);
		h1.openHashing_insert(64);
		h1.openHashing_print();
		h1.openHashing_search(78);
		h1.openHashing_search(90);
		System.out.println("2nd AFTER");
		h1.openHashing_delete(39);
		h1.openHashing_delete(112);
		h1.openHashing_delete(64);
		h1.openHashing_print();
	}
	
}
