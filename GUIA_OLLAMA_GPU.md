# 🚀 Guía: Ollama + GPU en Windows

## ¿Por qué Ollama?
- ✅ **GPU automática**: Detecta y usa CUDA/GPU sin configuración
- ✅ **Sin compilación**: Funciona directamente, sin necesidad de compilar
- ✅ **Múltiples modelos**: Descarga modelos instantáneamente
- ✅ **Rápido**: CPU y GPU optimizados

---

## Instalación (pasos rápidos)

### 1️⃣ Descargar Ollama
1. Ve a: https://ollama.ai
2. Haz clic en **"Download"** → selecciona **Windows**
3. Ejecuta el instalador

### 2️⃣ Verificar instalación
Abre PowerShell y ejecuta:
```powershell
ollama --version
```
Debería mostrar algo como: `ollama version 0.x.x`

### 3️⃣ Descargar un modelo
En PowerShell, ejecuta:
```powershell
ollama pull llama2
```

O si prefieres un modelo más pequeño/rápido:
```powershell
ollama pull neural-chat  # Modelo pequeño
ollama pull mistral      # Modelo grande y bueno
```

---

## Usar en el notebook

### Opción A: Terminal dividida (RECOMENDADO)

1. **Terminal 1** (sin cerrar):
   ```powershell
   ollama serve
   ```
   Verás: `Listening on 127.0.0.1:11434`

2. **Terminal 2** (nueva):
   ```powershell
   cd "C:\Users\gonza\proyectos\proyectosia\clases-mainPromting"
   .venv\Scripts\Activate.ps1
   jupyter notebook
   ```

3. En el notebook:
   - Asegúrate que `BACKEND = "ollama"`
   - Ejecuta las celdas normalmente
   - ¡GPU se usa automáticamente! 🎉

### Opción B: Usar directamente sin servicio

Si no quieres otra terminal abierta:
```powershell
# Ejecuta esto ANTES de correr el notebook
ollama serve &
# Luego abre el notebook
```

---

## Verificar que GPU está funcionando

En el notebook, después de ejecutar las celdas, verás:
```
🚀 Conectando a Ollama...
✅ Ollama disponible. Modelos: ['llama2:latest']
```

Si ves mensajes sobre GPU en tu terminal de `ollama serve`, significa que está usando GPU. 🚀

---

## Cambiar modelo

En la celda `BACKEND = "ollama"`, modifica:
```python
OLLAMA_MODEL = "llama2"  # Cambiar a otro modelo
```

Modelos populares:
- `llama2` - 7B, rápido
- `mistral` - 7B, buena calidad
- `neural-chat` - 7B, optimizado para chat
- `dolphin-mixtral` - Más potente

```powershell
ollama pull dolphin-mixtral  # Descargar el modelo
```

---

## Troubleshooting

### ❌ Error: "No se puede conectar a Ollama"
```
Solución: En otra terminal, ejecuta:
ollama serve
```

### ❌ El modelo es muy lento
```
Cambiar a modelo más pequeño:
ollama pull neural-chat
```

### ❌ GPU no se usa (solo CPU)
```
1. Verifica que CUDA Toolkit esté instalado
2. Instala ollama nuevamente (detecta GPU al instalar)
3. En terminal, verás logs de GPU si funciona
```

### ❌ "Model not found"
```
Primero descarga el modelo:
ollama pull llama2
```

---

## Para volver a llama-cpp-python (CPU)

Si quieres volver a la versión local sin Ollama:
```python
BACKEND = "local"  # En lugar de "ollama"
```

Pero **Ollama es más fácil** 😉

---

## Links útiles
- 🏠 Ollama: https://ollama.ai
- 📚 Modelos disponibles: https://ollama.ai/library
- 🐛 Issues: https://github.com/jmorganca/ollama/issues
