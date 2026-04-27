from router.route import route_post_to_bots
from content_engine.graph import build_graph

def main():
    post = "AI is replacing humans and billionaires are getting richer while society suffers"

    # Phase 1: Routing
    bots = route_post_to_bots(post)
    print("Matched Bots:", bots)

    # Personas
    personas = {
        "A":" artificial intelligence, machine learning, OpenAI, automation, software development, AI replacing jobs, future technology",
        "B": "I believe tech is destroying society and I am critical of AI and billionaires.",
        "C": "I care about markets, trading, ROI, and financial outcomes."
    }

    print("\n GENERATED POSTS:\n")

    for bot_id in bots:
        graph = build_graph()

        state = {
            "bot_id": bot_id,
            "persona": personas[bot_id]
        }

        print("STATE:", state)

        result = graph.invoke(state)

        print(f"\n--- Bot {bot_id} ---")
        print(result)


if __name__ == "__main__":
    main()