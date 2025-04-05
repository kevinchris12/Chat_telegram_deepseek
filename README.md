# CHAT TELEGRAM DEEPSEEK

# Descripción
Chat en telegram que conecta al usuario con un modelo de deepseek. El chatbot tiene como modelo base el DeepSeek-R1-Distill-Qwen-1.5B. Se puede acceder al chatbot mediante telegram web o app.  

## Características
- Implementación de DeepSeek-R1-Distill-Qwen-1.5B como chatbot.
- Integración con Telegram para respuestas automáticas.
- Uso de archivo `.env` para configuración segura.
- Servidor basado en `Flask`.

## Estructura del Proyecto
```markdown
Chat_telegram_deepseek/
│-- DeepSeek-R1-Distill-Qwen-1.5B/          # Contiene los pesos del modelo de NLP para el chatbot
│-- src/
│   │-- config/                             # Configuraciones necesarias para el proyecto
│   │   │-- env.py                          # Carga de las variables de entorno
│   │-- controllers/                        # Manejadores de rutas
│   │   │-- webhookController.py            # Manejadores de rutas del webhook
│   │-- routes/                             # Rutas
│   │   │-- webhookRoutes.py                # Rutas del webhook
│   │-- services/                           # Lógica del negocio y funciones principales
│   │   │-- deepseekService.py              # Funciones relacionadas con Deepseek
│   │   │-- messageHandler.py               # Manejador de mensajes de entrada del usuario
│   │   │-- telegramService.py              # Funciones relacionadas con telegram
│   │-- app.py                              # Flujo principal de la aplicación
│   │-- deepseekServer.py                   # Arranca el servidor con el modelo de Deepseek
│-- .env                                    # Variables de entorno
│-- .env_example                            # Descripción de las variables de entorno
│-- .gitignore                              # Archivos a ser ignorados en el repositorio
│-- README.md                               # Documentación del proyecto
```

## Ambiente
- Sistema Ubuntu 22.04
- Entorno virtual conda con python = 3.10

## Entorno virtual
Instalar en el entorno virtual las siguientes librerías

1. Instalar SGLang: 
   ```sh
   pip install uv
   uv pip install "sglang[all]>=0.4.4.post3" --find-links https://flashinfer.ai/whl/cu124/torch2.5/flashinfer-python
   ```

2. Instalar Dotenv: 
   ```sh
   conda install conda-forge::python-dotenv
   ```

3. Instalar Flask: 
   ```sh
   conda install anaconda::flask
   ```

4. Instalar Ngrok: 
   ```sh
   python3 -m pip install ngrok
   ```

## Creación del Bot en Telegram
En el buscador de Telegram, dentro de la app o version web, colocar @BotFather. Esto abrirá un chatbot para administrar los bots de Telegram. Colocando /start se muestran los comandos que se pueden utilizar. 

- Colocar /newbot para crear un bot en Telegram
- Pedirá crearle al bot un name y un username
- Se generará un Token que será necesario para la comunicación con la API de Telegram.  
- Además, se generará un chat en telegram que tiene como usuario el bot que acabamos de crear. 

## Guía para configurar el proyecto
1. Crear un bot en Telegram

2. Clonar el repositorio del proyecto

3. Dentro de la carpeta del proyecto clonar el repositorio con los pesos del modelo de deepseek:
   ```sh
   git clone https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
   ```

4. Crear dentro de la carpeta del proyecto el archivo `.env`. Colocar las variables de entorno necesarias en el archivo `.env`. Guiarse del archivo `.env_example`.

## Uso
Con el entorno virtual creado previamente
### Ejecutar el Servidor de Deepseek
   ```sh
   python src/deepseekServer.py
   ```
El servidor con el modelo de deepseek se ejecutará y estará listo para recibir mensajes del usuario.

### Ejecutar la aplicacion
En otra terminal
   ```sh
   python src/app.py
   ```
La aplicación permitirá conectar los mensajes enviados desde telegram hacia el servidor donde corre el modelo de deepseek. 

## Referencias
- SGL: https://docs.sglang.ai/backend/send_request.html
- Guia para usar Deepseek V3 con SGLang: https://github.com/sgl-project/sglang/tree/main/benchmark/deepseek_v3
- Deepseek API docs: https://api-docs.deepseek.com/
- Guia de uso Deepseek V3: https://github.com/deepseek-ai/DeepSeek-V3/tree/main
- Pesos del modelo DeepSeek-R1-Distill-Qwen-1.5B: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
- Variaciones del modelo DeepSeek-R1: https://huggingface.co/deepseek-ai/DeepSeek-R1
- Github DeepSeek-R1: https://github.com/deepseek-ai/DeepSeek-R1
- Telegram Bot API: https://core.telegram.org/bots/api
- Guia para crear un chatbot en Telegram: https://core.telegram.org/bots/tutorial
- Guia para crear un bot en Telegram: https://core.telegram.org/bots/features#creating-a-new-bot
- NGROK: https://dashboard.ngrok.com/get-started/setup/python


