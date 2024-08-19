import pandas as pd

# Excel dosyasını yükleyin
file_path = 'Ürünler_1724095492.xlsx'  # Dosya yolunuza göre güncelleyin
df = pd.read_excel(file_path)

# 'Ürün Kodu |code|' sütununda 3500 ile başlamayanlara 'BTMY' ekleyin
df['Ürün Kodu |code|'] = df['Ürün Kodu |code|'].apply(lambda x: f'BTMY{x}' if not str(x).startswith('3500') else x)

# Güncellenmiş dosyayı kaydedin
output_file_path = 'Modified_Ürünler.xlsx'  # Kaydetmek istediğiniz dosya adı
df.to_excel(output_file_path, index=False)

print(f"Güncellenmiş dosya {output_file_path} olarak kaydedildi.")
