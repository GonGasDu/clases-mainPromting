import torch
from transformers import pipeline

print("Cargando modelo en GPU...")

# Crear un generador de texto que use la GPU
generator = pipeline(
    "text-generation",
    model="gpt2",
    device=0  # 0 = primera GPU
)

print("Generando texto...")
resultado = generator(
    "La inteligencia artificial en Argentina",
    max_length=100,
    num_return_sequences=1
)

print("\n--- RESULTADO ---")
print(resultado[0]['generated_text'])

# Ver cuánta memoria GPU usaste
print(f"\nMemoria GPU usada: {torch.cuda.memory_allocated(0) / 1e9:.2f} GB")
print(f"Memoria GPU disponible: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
