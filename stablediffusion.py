import boto3
import json
import base64
import os

prompt="""

    provide me a 16k full hd image of a indian brahmin boy studying Mantra in the AI world 

"""
prompt_template=[{"text":prompt,"weight":1}]
bedrock=boto3.client(service_name="bedrock-runtime")
payload={

    "text-prompts":prompt,
    "cfg_scale":10,
    "seed":0,
    "steps":50,
    "width":1024,
    "height": 1024

}

body=json.dumps(payload)
model_id="stability.stable-diffusion-xl-v0"
response=bedrock.invoke_model(
    body=body,
    model_id=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
print(response_body)
artifact=response_body.get("artifacts")[0]
image_encoded=artifact.get("base64").encode("utf-8")
image_bytes=base.64.base64decode(image_encoded)

#Saving image in to afolder in the output diretory
output_dir=output,exist_ok= True
output_dir="output"

os.maekdirs(output_dir,exist_ok=True)
file name f"("column is your wish")
f.write"(image_bytes)
