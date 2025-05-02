import random

def analyze_hair(image_path):
    kondisi = random.choice([
        "Rambut tipis di bagian atas kepala.",
        "Rambut terlihat sehat, tapi butuh perawatan akar.",
        "Terlihat tanda-tanda kebotakan dini.",
        "Rambut kering dan bercabang.",
        "Rambut lepek karena produksi minyak berlebih."
    ])

    rekomendasi = "Gunakan Hair Tonic, Serum & Shampoo Herbal Green Angelica."
    return {
        "kondisi": kondisi,
        "rekomendasi": rekomendasi
    }
