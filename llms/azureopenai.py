import os
os.environ["AZURE_OPENAI_API_KEY"] = "XXXXXX"   #replace the XXXXXX with the API key of Azure Open AI you deployed

config_list = [
    {
        "model": "model_name", #replace the model_name with the model name of Azure Open AI you deployed
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "base_url": "https://{resource}.openai.azure.com/", #replace the {resource} with the resource name of Azure Open AI
        "api_version": "2024-02-15-preview",
        "api_type": "azure",
    }
]