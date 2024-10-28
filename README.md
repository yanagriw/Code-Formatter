# Code Formatter (Python)
 
In this project, we aim to build a code formatting model using the `T5-small` architecture, 
trained on the Python subset of the `CodeSearchNet` dataset. The objective is to create a 
sequence-to-sequence model that can learn to automatically format unstructured or poorly 
formatted Python code snippets. Using T5-small allows us to leverage an efficient, transformer-based 
language model to predict proper spacing, line breaks, and indentation, making code more readable 
and maintainable.

## Example
Original code: `defcheck_even(n):return n%2==0`

Formatted code: `def check_even(n): return n % 2 == 0`

The model achieves this by introducing errors in the dataset, primarily by removing spaces, which enables it to learn and correct formatting.

## Project Structure
- `train_model.ipynb`: This notebook is used for training the model. After training, the model is saved to the Hugging Face Hub.
- `T5_formatter.py:` This script downloads the trained model from Hugging Face and allows for direct usage in formatting code snippets.