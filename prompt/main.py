import boto3
import json

prompt = """

  Explain me how I can Make Vidyashilp University academic excellence in the field of cyber security. Because I want to integrate it with data science and artificial intelligence.
  
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt": "[INST]" + prompt + "[/INST]]",
    "max_gen_lemgth": 512,
    "temperature": 0.5,
    "top_p": 0.8,
}

body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"

response=bedrock.invoke_model(
  body=body,
  modelID=model_id
  accept="application/json"
  contentType="application/json"
)

response_body=json.loads(response.get("body").read())
response_text=responsebody['generation']
print(response_text)
