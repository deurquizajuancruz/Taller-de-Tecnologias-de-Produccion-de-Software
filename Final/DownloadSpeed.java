// package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

class Edge implements Cloneable {
	private Node origin, target;
	private long capacity, flow;

	public Edge(Node origin, Node target, long capacity) {
		this.origin = origin;
		this.target = target;
		this.capacity = capacity;
		this.flow = 0;
	}

	public Node getTarget() {
		return this.target;
	}

	public Node getOrigin() {
		return this.origin;
	}

	public long getCapacity() {
		return this.capacity;
	}

	public long getAvailableCapacity() {
		return this.capacity - this.flow;
	}

	public void sendFlow(long amount) {
		this.flow += amount;
	}

	public boolean isSaturated() {
		return this.capacity == this.flow;
	}

	public void increaseCapacity(long capacity) {
		this.capacity += capacity;
	}

	@Override
	public Edge clone() {
		try {
			return (Edge) super.clone();
		} catch (Exception e) {
			System.out.println(e.getMessage());
			return null;
		}
	}
}

class Node implements Cloneable {
	private String content;
	private List<Edge> adjacent;

	public Node(String content) {
		this.content = content;
		this.adjacent = new ArrayList<Edge>();
	}

	public Edge addAdjacent(Node adjacent, long weight) {
		Edge edge = new Edge(this, adjacent, weight);
		this.adjacent.add(edge);
		return edge;
	}

	public String getContent() {
		return this.content;
	}

	public List<Edge> getAdjacents() {
		return this.adjacent;
	}

	public Edge getEdgeTo(Node target) {
		return this.adjacent.stream().filter(edge -> edge.getTarget().equals(target)).findFirst().orElse(null);
	}

	public void addEdge(Edge edge) {
		this.adjacent.add(edge);
	}

	@Override
	public Node clone() {
		try {
			Node cloned = (Node) super.clone();
			cloned.adjacent = new ArrayList<Edge>();
			return cloned;
		} catch (Exception e) {
			System.out.println(e.getMessage());
			return null;
		}
	}
}

class Graph implements Cloneable {
	private List<Node> nodes;

	public Graph() {
		this.nodes = new ArrayList<Node>();
	}

	public void addNode(Node n) {
		this.nodes.add(n);
	}

	private List<Edge> dfs(Node current, Node target, List<Edge> path, HashSet<Node> visited) {
		if (current.equals(target)) {
			return new ArrayList<Edge>(path);
		}

		visited.add(current);

		for (Edge edge : current.getAdjacents()) {
			if (!edge.isSaturated() && !visited.contains(edge.getTarget())) {
				path.add(edge);
				List<Edge> result = dfs(edge.getTarget(), target, path, visited);
				if (result != null) {
					return result;
				}
				path.remove(path.size() - 1);
			}
		}
		return null;
	}

	public Node getNodeByContent(String content) {
		return this.nodes.stream().filter(node -> node.getContent().equals(content)).findFirst().orElse(null);
	}

	public long fordFulkerson(Node origin, Node target) {
		long maxFlow = 0;
		try {
			Graph residualGraph = (Graph) this.clone();
			Node residualOrigin = residualGraph.getNodeByContent(origin.getContent());
			Node residualTarget = residualGraph.getNodeByContent(target.getContent());
			List<Edge> path = residualGraph.dfs(residualOrigin, residualTarget, new ArrayList<Edge>(),
					new HashSet<Node>());
			while (path != null) {
				long pathCapacity = path.stream().mapToLong(edge -> edge.getAvailableCapacity()).min().orElse(0);
				maxFlow += pathCapacity;
				for (Edge edge : path) {
					edge.sendFlow(pathCapacity);
					Edge reverseEdge = edge.getTarget().getEdgeTo(edge.getOrigin());
					if (reverseEdge == null) {
						reverseEdge = edge.getTarget().addAdjacent(edge.getOrigin(), 0);
					}
					reverseEdge.increaseCapacity(pathCapacity);
				}
				path = residualGraph.dfs(residualOrigin, residualTarget, new ArrayList<Edge>(), new HashSet<Node>());
			}
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return maxFlow;
	}

	@Override
	public Graph clone() {
		Graph clonedGraph = new Graph();
		Map<String, Node> clonedNodes = new HashMap<>();
		try {

			for (Node node : this.nodes) {
				Node clonedNode = node.clone();
				clonedNodes.put(clonedNode.getContent(), clonedNode);
				clonedGraph.addNode(clonedNode);
			}

			for (Node node : this.nodes) {
				Node clonedNode = clonedNodes.get(node.getContent());
				for (Edge edge : node.getAdjacents()) {
					Node clonedOrigin = clonedNodes.get(edge.getOrigin().getContent());
					Node clonedTarget = clonedNodes.get(edge.getTarget().getContent());
					Edge clonedEdge = new Edge(clonedOrigin, clonedTarget, edge.getAvailableCapacity());
					clonedNode.addEdge(clonedEdge);
				}
			}
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}

		return clonedGraph;
	}
}

public class DownloadSpeed {
	public static void main(String[] args) {
		Graph myGraph = new Graph();
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String[] line = br.readLine().split("\\s+");
			int nodesAmount = Integer.parseInt(line[0]);
			int connectionsAmount = Integer.parseInt(line[1]);

			for (int i = 0; i < nodesAmount; i++) {
				myGraph.addNode(new Node(String.valueOf(i + 1)));
			}
			for (int i = 0; i < connectionsAmount; i++) {
				line = br.readLine().split("\\s+");
				myGraph.getNodeByContent(line[0]).addAdjacent(myGraph.getNodeByContent(line[1]),
						Integer.parseInt(line[2]));
			}
			System.out.println(myGraph.fordFulkerson(myGraph.getNodeByContent("1"),
					myGraph.getNodeByContent(String.valueOf(nodesAmount))));

		} catch (IOException e) {
			System.err.println(e.getMessage());
		}
	}
}
