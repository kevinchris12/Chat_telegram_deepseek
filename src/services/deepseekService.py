import re
from openai import OpenAI

class DeepSeekChat:
  def __init__(self, port, model="DeepSeek-R1-Distill-Qwen-1.5B"):
    self.client = OpenAI(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")
    self.model = model
    self.default_filter = re.compile(r'.*?</think>\s*', flags=re.DOTALL)
    self.conversation_history = []

  def chat(self, mensaje_usuario, filtro=None, temperature=0.6, add_to_history=True):
    if filtro is None:
      filtro = self.default_filter
        
    messages = [
      {"role": "system", "content": "You are a helpful assistant. If you don't know something only say, I don't know"},
      {"role": "system", "content": "If I don't ask you something answer me with an OK"},
      *self.conversation_history,
      {"role": "user", "content": mensaje_usuario}
    ]
    
    response = self.client.chat.completions.create(
      model=self.model,
      messages=messages,
      temperature=temperature,
      stream=False
    )

    respuesta = response.choices[0].message.content
    respuesta_limpia = re.sub(filtro, '', respuesta, flags=0).strip()
    
    if add_to_history:
      self.conversation_history.extend([
        {"role": "user", "content": mensaje_usuario},
        {"role": "assistant", "content": respuesta_limpia}
      ])
    
    return respuesta_limpia
  
  def reset_history(self):
    self.conversation_history = []