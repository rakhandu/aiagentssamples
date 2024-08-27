
import sys
# adding llms to the system path, make sure to configure the file azureopenai in llms folder with end point details
sys.path.append('C:\\proddev\\research\\aiagentssamples\\llms\\')
import azureopenai

import autogen
from autogen.coding import LocalCommandLineCodeExecutor

# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "cache_seed": 41,  # seed for caching and reproducibility
        "config_list": azureopenai.config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        # the executor to run the generated code
        "executor": LocalCommandLineCodeExecutor(work_dir="coding"), # the working directory for the executor create tmp files
    },
)
# the assistant receives a message from the user_proxy, which contains the task description
chat_res = user_proxy.initiate_chat(
    assistant,
    message="""Get the last 3 month stock price performance of MSFT stock.""",
    summary_method="reflection_with_llm",
)