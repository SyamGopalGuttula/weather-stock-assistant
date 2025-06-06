from langgraph_app.graph import graph

if __name__ == "__main__":
    print("Welcome to the LangGraph Multi-Agent Assistant!")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask me anything (weather, stock, news): ").strip()
        if query.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        result = graph.invoke({"input": query})
        print("\nResult:\n", result["result"], "\n")
