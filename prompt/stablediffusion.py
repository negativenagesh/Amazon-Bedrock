import boto3
import json
import base64
import os

prompt = """

  Generate a 4k image of a white cat with a brown background. and a brown cat with a white background. 

"""

prompt_template = [{"text": prompt, "weight": 1}]
bedrock = boto3.client(service_name='bedrock-runtime')
payload = {
    "text_prompts": prompt_template,
    "cfg_scale": 10,
    "speed": 0,
    "steps": 50,
    "width": 1024,
    "height": 1024
}

body = json.dumps(payload)
model_id = 'stability.stable-diffusion-xl-v0'
response = bedrock.invoke_model(body=body,
                                modelId=model_id,
                                accept="application/json",
                                contentType="application/json")

response_body = json.loads(response.get('body').read())
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get('base64').encode('utf-8')
image_bytes = base64.b64decode(image_encoded)
