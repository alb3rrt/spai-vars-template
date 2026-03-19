from spai.config import SPAIVars

vars = SPAIVars()

message = vars["MESSAGE"]
max_items = vars["MAX_ITEMS"]
some_data = vars["some_data"]

if not isinstance(message, str):
    raise TypeError("MESSAGE must be a string")

if not isinstance(max_items, (int, float)):
    raise TypeError("MAX_ITEMS must be numeric")

print("MESSAGE:", message)
print("MAX_ITEMS:", max_items)
print("some_data:", some_data)
