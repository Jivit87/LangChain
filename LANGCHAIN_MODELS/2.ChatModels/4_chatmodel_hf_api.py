from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # use Zephyr or another chat-friendly model
    task="text-generation",
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)