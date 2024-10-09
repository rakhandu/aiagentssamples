
#learn more about the prompt examples - https://platform.openai.com/docs/examples
class PromptExamples:

    system_explain_code = "You will be provided with a piece of code, and your task is to explain it in a concise way."
    user_sample_code = """
    def sum_of_two_numbers(a, b):
        return a + b

    # Example usage:
    result = sum_of_two_numbers(3, 5)
    print(result)  # Output: 8
    """

    system_prompt = "You will be provided with a prompt and your task is to complete it."


    system_tweet_analyst = "You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative."
    user_tweet = "I love the new features of this phone! It's amazing!"

    #include details in your query to get better response from the model
    prompt_query_bad = "Write code to calculate the Fibonacci sequence."
    prompt_query_good = "Write a Csharp function to efficiently calculate the Fibonacci sequence. Comment the code liberally to explain what each piece does and why it's written that way."


export = PromptExamples()