from sglang.utils import wait_for_server, print_highlight, terminate_process
from sglang.utils import launch_server_cmd
from config import env

# This is equivalent to running the following command in your terminal
# python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B-Instruct --host 0.0.0.0

# Ejecutando servidor local con el modelo de deepseek
server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model ./DeepSeek-R1-Distill-Qwen-1.5B --trust-remote-code
""", host = "0.0.0.0", port = env.PORT_DEEPSEEK
)

wait_for_server(f"http://localhost:{port}")