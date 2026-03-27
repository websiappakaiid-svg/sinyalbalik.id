import os, re

blog = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

# Map of files that need new unique images (keeping first occurrence, replacing duplicates)
replacements = {
    # photo-1556656793 used by: cara-cek-imei, iphone-inter-masuk, iphone-amerika, berapa-lama, harga-inter-murah, pengalaman-beli, iphone-inter-provider
    # Keep for cara-cek-imei, replace rest:
    'iphone-inter-masuk-indonesia.html': 'https://images.unsplash.com/photo-1580910051074-3eb694886f1b?w=800&h=400&fit=crop',
    'iphone-amerika-indonesia.html': 'https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=800&h=400&fit=crop',
    'berapa-lama-aktivasi-sinyal.html': 'https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?w=800&h=400&fit=crop',
    'harga-iphone-inter-murah.html': 'https://images.unsplash.com/photo-1607936854279-55e8a4c64888?w=800&h=400&fit=crop',
    'pengalaman-beli-iphone-inter.html': 'https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=800&h=400&fit=crop',
    'iphone-inter-provider-indonesia.html': 'https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=800&h=400&fit=crop',
    
    # photo-1512054502232 used by: esim-iphone-inter, imei-tidak-terdaftar, apa-itu-imei, imei-iphone-diblokir, mode-pesawat, esim-vs-aktivasi
    # Keep for esim-iphone-inter, replace rest:
    'imei-tidak-terdaftar-solusi.html': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=800&h=400&fit=crop',
    'apa-itu-imei.html': 'https://images.unsplash.com/photo-1544027993-37dbfe43562a?w=800&h=400&fit=crop',
    'imei-iphone-diblokir.html': 'https://images.unsplash.com/photo-1578345218746-50a229b3d0f8?w=800&h=400&fit=crop',
    'mode-pesawat-iphone-no-service.html': 'https://images.unsplash.com/photo-1436491865332-7a61a109db05?w=800&h=400&fit=crop',
    'esim-vs-aktivasi-imei.html': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=400&fit=crop',
    
    # photo-1601784551446 used by: iphone-no-service-penyebab, iphone-mencari-terus, iphone-sinyal-hilang
    # Keep for iphone-no-service, replace rest:
    'iphone-mencari-terus.html': 'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=800&h=400&fit=crop',
    'iphone-sinyal-hilang-timbul.html': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop',
    
    # photo-1563203369 used by: aktivasi-sinyal-iphone, iphone-no-service-setelah-update, perpanjang-sinyal, aktivasi-sinyal-aman
    # Keep for aktivasi-sinyal-iphone, replace rest:
    'iphone-no-service-setelah-update.html': 'https://images.unsplash.com/photo-1573152143286-0c422b4d2175?w=800&h=400&fit=crop',
    'perpanjang-sinyal-iphone-inter.html': 'https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&h=400&fit=crop',
    'aktivasi-sinyal-iphone-aman.html': 'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=800&h=400&fit=crop',
    
    # photo-1592899677977 used by: iphone-inter-tidak-ada-sinyal, iphone-cuma-bisa-wifi, reset-network
    # Keep for iphone-inter-tidak-ada-sinyal, replace rest:
    'iphone-cuma-bisa-wifi.html': 'https://images.unsplash.com/photo-1526498460520-4c246339dccb?w=800&h=400&fit=crop',
    'reset-network-settings-iphone.html': 'https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&h=400&fit=crop',
    
    # photo-1510557880182 used by: perbedaan-iphone-inter-resmi, sim-tidak-didukung, tanda-blokir-imei
    # Keep for perbedaan, replace rest:
    'sim-tidak-didukung-iphone.html': 'https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=800&h=400&fit=crop',
    'tanda-iphone-kena-blokir-imei.html': 'https://images.unsplash.com/photo-1523206489230-c012c64b2b48?w=800&h=400&fit=crop',
    
    # photo-1491933382434 used by: beli-iphone-murah, tips-beli, iphone-bekas, iphone-inter-garansi
    # Keep for beli-iphone-murah, replace rest:
    'tips-beli-iphone-inter.html': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=800&h=400&fit=crop',
    'iphone-bekas-luar-negeri.html': 'https://images.unsplash.com/photo-1567581935884-3349723552ca?w=800&h=400&fit=crop',
    'iphone-inter-garansi-apple.html': 'https://images.unsplash.com/photo-1621768216002-5ac171876625?w=800&h=400&fit=crop',
    
    # photo-1589829545856 used by: aturan-imei, blokir-imei-vs-lock, imei-blacklist-vs
    # Keep for aturan-imei, replace rest:
    'blokir-imei-vs-lock-operator.html': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=400&fit=crop',
    'imei-blacklist-vs-belum-terdaftar.html': 'https://images.unsplash.com/photo-1633265486064-086b219458ec?w=800&h=400&fit=crop',
}

count = 0
for filename, new_url in replacements.items():
    fp = os.path.join(blog, filename)
    if not os.path.exists(fp):
        print(f'SKIP (not found): {filename}')
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find and replace the hero image URL
    old = re.search(r'(https://images\.unsplash\.com/photo-[^?\"]+)\?w=800&h=400&fit=crop(" alt="[^"]*" class="hero-img")', content)
    if old:
        old_url = old.group(1) + '?w=800&h=400&fit=crop'
        content = content.replace(old_url, new_url, 1)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'FIXED: {filename}')
    else:
        print(f'NO MATCH: {filename}')

print(f'\nFixed {count} duplicate images!')
