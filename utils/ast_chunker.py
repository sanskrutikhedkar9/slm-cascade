# utils/ast_chunker.py

import ast


def extract_code_chunks(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    lines = source.splitlines()

    chunks = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):

            start_line = node.lineno - 1
            end_line = node.end_lineno

            code = "\n".join(
                lines[start_line:end_line]
            )

            chunks.append({
                "type": "function" if isinstance(node, ast.FunctionDef) else "class",
                "name": node.name,
                "code": code,
                "start": start_line,
                "end": end_line,
                "path": file_path
            })

    return chunks