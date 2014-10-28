package ios.ac.cn;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class UndirectedGraphNode {
	int label;
	List<UndirectedGraphNode> neighbors;

	UndirectedGraphNode(int x) {
		label = x;
		neighbors = new ArrayList<UndirectedGraphNode>();
	}
};

public class CloneGraph {
	private Map<UndirectedGraphNode, UndirectedGraphNode> cloneNodes = new HashMap<>();

	public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
		if (node == null) {
			return null;
		}

		if (cloneNodes.containsKey(node)) {
			return cloneNodes.get(node);
		} else {
			UndirectedGraphNode cloneN = new UndirectedGraphNode(node.label);

			cloneNodes.put(node, cloneN);

			for (UndirectedGraphNode e : node.neighbors) {
				cloneN.neighbors.add(cloneGraph(e));
			}
			return cloneN;
		}
	}

	public static void main(String[] args) {
		UndirectedGraphNode n0 = new UndirectedGraphNode(0);
		UndirectedGraphNode n1 = new UndirectedGraphNode(0);
		UndirectedGraphNode n2 = new UndirectedGraphNode(0);
		n0.neighbors.add(n1);
		n0.neighbors.add(n2);
		new CloneGraph().cloneGraph(n0);
	}
}