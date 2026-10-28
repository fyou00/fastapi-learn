from fastapi import FastAPI

# Inisialisasi aplikasi
app = FastAPI()

# Definisikan endpoint root (/)
@app.get("/")
def read_root():
    return {"message": "Halo! Proyek FastAPI berhasil berjalan di VS Code."}

# Definisikan endpoint dengan parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query_param": q}
