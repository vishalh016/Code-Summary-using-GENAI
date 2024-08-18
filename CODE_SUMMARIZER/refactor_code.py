import ast
import os


def extract_code_and_functions(file_path):
    """Extracts code and functions from a Python script.

    Args:
        file_path (str): Path to the Python script.

    Returns:    
        str: Extracted code and functions combined.
    """

    with open(file_path, 'r') as f:
        code = f.read()

    tree = ast.parse(code)

    # Define helper functions for handling function definitions and calls
    def visit_function_def(node):
        """Handles encountered function definitions.

        Extracts the function code and stores it.
        """
        function_code = ast.unparse(node)
        return function_code

    def visit_call(node):
        """Handles encountered function calls.

        Recursively extracts the code of called functions defined within the script.
        """
        if isinstance(node.func, ast.Name):
            function_name = node.func.id
            if function_name in function_defs:
                yield function_defs[function_name]  # Yield for generator-like approach

    # Extract function definitions and calls
    function_defs = {}
    visitor = ast.NodeVisitor()
    visitor.visit_FunctionDef = visit_function_def
    visitor.visit_Call = visit_call
    extracted_code = (visitor.visit(tree) or []) + [code]  # Handle empty generator

    # Combine extracted functions and main script code
    return '\n'.join(extracted_code)


def main():
    """Prompts user for input and output file paths, calls extraction function."""

    file_path = input("Enter the path to the Python script: ")
    if not os.path.exists(file_path):
        print("File not found.")
        return

    extracted_code = extract_code_and_functions(file_path)

    output_file = input("Enter the output file name: ")
    with open(output_file, 'w') as f:
        f.write(extracted_code)

    print("Code and functions extracted to:", output_file)


if __name__ == "__main__":
    main()
