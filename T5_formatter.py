from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the model and tokenizer from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("yanagriw/Code-Formatter")

# Move model to CUDA if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Define a test input (unformatted code)
unformatted_code = "def square(x):return x*x"

# Tokenize the input and generate the formatted output
inputs = tokenizer(unformatted_code, return_tensors="pt").to(device)
outputs = model.generate(**inputs)

# Decode and print the formatted code
formatted_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Formatted code:\n", formatted_code)
