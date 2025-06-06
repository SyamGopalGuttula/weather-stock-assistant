from langgraph_app.graph import graph

if __name__ == "__main__":
    query = input("Ask me anything: ")
    result = graph.invoke({"input": query})
    print("\nResult:\n", result["result"])
