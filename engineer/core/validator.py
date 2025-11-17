import ast

class Validator:
    def check(self, output):
        for art in output.get("artifacts", []):
            if art["type"] == "file" and art["path"].endswith(".py"):
                try:
                    ast.parse(art["content"])
                except SyntaxError as e:
                    return {"status": "error", "reason": f"Error en {art['path']}: {e}"}
        return output
