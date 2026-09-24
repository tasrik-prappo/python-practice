system_tools = ["web_search","code_interpreter","calculator"]

request_payload = {
    "user_id":1092,
    "model":"claude-3.5-sonnet",
    "tools":system_tools,
    "max_tokens":2048
}

system_tools.append("image_generator")

print(f"User {request_payload["user_id"]} requested model {request_payload["model"]} with {len(request_payload["tools"])} tools available.")