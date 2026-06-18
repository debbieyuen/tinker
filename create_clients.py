import tinker
from tinker import types

# Entry point — reads TINKER_API_KEY from environment
service_client = tinker.ServiceClient()

# Training client (LoRA fine-tuning)
training_client = service_client.create_lora_training_client(
    base_model="Qwen/Qwen3-8B", rank=32
)

# Sampling client (text generation)
sampling_client = service_client.create_sampling_client(
    base_model="Qwen/Qwen3-8B"
)

# Tokenizer
tokenizer = training_client.get_tokenizer()