import requests
import gradio as gr

# ============================================================
# Ollama Configuration
# ============================================================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codeguru"


# ============================================================
# Generate Streaming Response
# ============================================================

def generate_response(prompt):

    final_prompt = f"""
You are CodeGuru, a Python coding assistant.

Instructions:
- Answer the user's current question only.
- Use Python unless another programming language is explicitly requested.
- Provide correct and executable code.
- Keep explanations concise.
- Do not answer previous questions.
- Format code using Markdown code blocks.

User question:
{prompt}
"""

    data = {
        "model": MODEL_NAME,
        "prompt": final_prompt,
        "stream": True
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=data,
            stream=True,
            timeout=300
        )

        if response.status_code != 200:
            yield f"**Ollama Error:** {response.text}"
            return

        # Store the generated response
        full_response = ""

        # Ollama returns JSON objects line by line
        for line in response.iter_lines():

            if line:

                try:
                    result = line.decode("utf-8")
                    result = __import__("json").loads(result)

                    # Get generated text
                    token = result.get("response", "")

                    full_response += token

                    # Send partial response to Gradio
                    yield full_response

                    # Stop when Ollama finishes
                    if result.get("done", False):
                        break

                except Exception as e:
                    yield f"{full_response}\n\nError processing response: {e}"
                    return

    except requests.exceptions.ConnectionError:
        yield (
            "**Connection Error**\n\n"
            "Could not connect to Ollama.\n\n"
            "Make sure Ollama is running with:\n\n"
            "```cmd\n"
            "ollama serve\n"
            "```"
        )

    except requests.exceptions.Timeout:
        yield "**Error:** Ollama took too long to respond."

    except Exception as e:
        yield f"**Unexpected Error:** {str(e)}"


# ============================================================
# Gradio Interface
# ============================================================

interface = gr.Interface(
    fn=generate_response,

    inputs=gr.Textbox(
        label="Prompt",
        lines=4,
        placeholder="Enter your coding question..."
    ),

    outputs=gr.Markdown(
        label="CodeGuru Response"
    ),

    title="CodeGuru AI",

    description=(
        "Local Python coding assistant powered by "
        "Ollama and the CodeGuru model."
    )
)


# ============================================================
# Start Application
# ============================================================

if __name__ == "__main__":
    interface.launch()