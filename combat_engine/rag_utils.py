def merge_thread_context(parent_post, comment_history, human_reply):
    # Join all previous comments into a single string (newline separated)
    history = "\n".join(comment_history)

    # Build a formatted block combining parent post, thread history, and latest human reply
    return f"Parent: {parent_post}\nThread:\n{history}\nHuman: {human_reply}"
