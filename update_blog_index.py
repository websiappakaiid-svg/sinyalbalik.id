import os, re

blog_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

# All articles 21-50 with their info
new_articles = [
    ("iphone-jepang-no-service.html", "https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?w=200&h=150&fit=crop", "iPhone Jepang", "Kenapa iPhone dari Jepang Sering No Service?", "iPhone Jepang shutter, carrier lock, dan cara fixnya."),
    ("iphone-korea-tidak-ada-sinyal.html", "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=200&h=150&fit=crop", "iPhone Korea", "iPhone dari Korea Tidak Ada Sinyal? Ini Alasannya", "Masalah KT/SKT lock dan cara mengatasinya."),
    ("iphone-amerika-indonesia.html", "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=200&h=150&fit=crop", "iPhone Amerika", "iPhone dari Amerika Bisa Dipakai di Indonesia?", "Kompatibilitas, eSIM only, dan solusinya."),
    ("samsung-inter-imei-terblokir.html", "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=200&h=150&fit=crop", "Samsung inter", "Samsung Inter IMEI Terblokir: Sama Seperti iPhone?", "Samsung inter juga kena blokir IMEI."),
    ("reset-network-settings-iphone.html", "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=200&h=150&fit=crop", "Reset network", "Cara Reset Network Settings iPhone yang Benar", "Panduan reset jaringan tanpa hapus data."),
    ("iphone-sinyal-hilang-timbul.html", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=200&h=150&fit=crop", "Sinyal hilang timbul", "iPhone Sinyal Hilang Timbul, Ini 5 Penyebabnya", "5 penyebab sinyal tidak stabil dan solusinya."),
    ("aktivasi-sinyal-iphone-aman.html", "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=200&h=150&fit=crop", "Aktivasi aman", "Apakah Aktivasi Sinyal iPhone Aman? Fakta Lengkap", "Review keamanan layanan aktivasi sinyal."),
    ("imei-iphone-diblokir.html", "https://images.unsplash.com/photo-1578345218746-50a229b3d0f8?w=200&h=150&fit=crop", "IMEI diblokir", "Apa yang Terjadi Kalau IMEI iPhone Diblokir?", "Dampak dan solusi IMEI yang terblokir."),
    ("cek-iphone-inter-atau-resmi.html", "https://images.unsplash.com/photo-1591337676887-a217a6c6c7c7?w=200&h=150&fit=crop", "Cek iPhone", "Cara Cek iPhone Inter atau Resmi Tanpa Ribet", "4 cara mudah cek iPhone inter vs resmi."),
    ("iphone-bekas-luar-negeri.html", "https://images.unsplash.com/photo-1567581935884-3349723552ca?w=200&h=150&fit=crop", "iPhone bekas", "iPhone Bekas dari Luar Negeri: Worth It atau Tidak?", "Review plus minus beli iPhone bekas inter."),
    ("harga-iphone-inter-murah.html", "https://images.unsplash.com/photo-1607936854279-55e8a4c64888?w=200&h=150&fit=crop", "Harga iPhone", "Kenapa Harga iPhone Inter Lebih Murah?", "Rahasia kenapa iPhone inter lebih murah."),
    ("iphone-15-inter-indonesia.html", "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=200&h=150&fit=crop", "iPhone 15", "iPhone 15 Inter di Indonesia: Bisa Sinyal?", "Panduan lengkap iPhone 15 inter di Indonesia."),
    ("mode-pesawat-iphone-no-service.html", "https://images.unsplash.com/photo-1436491865332-7a61a109db05?w=200&h=150&fit=crop", "Mode pesawat", "Mode Pesawat Trick untuk iPhone No Service", "Kapan mode pesawat berhasil dan kapan tidak."),
    ("imei-blacklist-vs-belum-terdaftar.html", "https://images.unsplash.com/photo-1633265486064-086b219458ec?w=200&h=150&fit=crop", "IMEI blacklist", "IMEI Blacklist vs Belum Terdaftar", "Perbedaan dua status IMEI yang sering tertukar."),
    ("iphone-inter-provider-indonesia.html", "https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=200&h=150&fit=crop", "Provider", "Bisakah iPhone Inter Pakai Semua Provider?", "Kompatibilitas provider Indonesia untuk iPhone inter."),
    ("pengalaman-beli-iphone-inter.html", "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=200&h=150&fit=crop", "Pengalaman beli", "Pengalaman Beli iPhone Inter di Marketplace", "Review jujur dan tips beli iPhone inter online."),
    ("esim-vs-aktivasi-imei.html", "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=200&h=150&fit=crop", "eSIM vs IMEI", "eSIM vs Aktivasi IMEI", "Perbandingan eSIM dan aktivasi sinyal sebagai solusi."),
    ("tanda-iphone-kena-blokir-imei.html", "https://images.unsplash.com/photo-1523206489230-c012c64b2b48?w=200&h=150&fit=crop", "Tanda blokir", "Tanda-Tanda iPhone Kena Blokir IMEI", "5 tanda iPhone terdampak blokir IMEI."),
    ("perpanjang-sinyal-iphone-inter.html", "https://images.unsplash.com/photo-1553406830-ef2513450d76?w=200&h=150&fit=crop", "Perpanjang sinyal", "Cara Perpanjang Sinyal iPhone Inter", "Tips agar sinyal tidak expired."),
    ("iphone-inter-garansi-apple.html", "https://images.unsplash.com/photo-1621768216002-5ac171876625?w=200&h=150&fit=crop", "Garansi Apple", "iPhone Inter Bisa Dapat Garansi Apple?", "Fakta garansi Apple untuk unit internasional."),
    ("oppo-xiaomi-blokir-imei.html", "https://images.unsplash.com/photo-1546054454-aa26e2b734c7?w=200&h=150&fit=crop", "Oppo Xiaomi", "Oppo/Xiaomi Juga Kena Blokir IMEI?", "Bukan cuma iPhone — semua HP inter kena."),
    ("aturan-imei-2026.html", "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&h=150&fit=crop", "Aturan 2026", "Aturan IMEI 2026: Apa yang Berbeda?", "Update terbaru regulasi IMEI 2026."),
    ("cek-imei-online-tanpa-hp.html", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=200&h=150&fit=crop", "Cek IMEI online", "Cara Cek IMEI Tanpa HP (Online)", "3 cara cek IMEI tanpa pegang HP langsung."),
    ("iphone-dual-sim-inter.html", "https://images.unsplash.com/photo-1587033411391-5d9e51cce126?w=200&h=150&fit=crop", "Dual SIM", "iPhone Dual SIM Inter: 2 IMEI Kena Blokir?", "Penjelasan IMEI1, IMEI2 pada iPhone inter."),
    ("risiko-iphone-inter-tanpa-sinyal.html", "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=200&h=150&fit=crop", "Risiko", "Risiko Pakai iPhone Inter Tanpa Sinyal", "5 risiko besar tanpa aktivasi sinyal."),
    ("iphone-singapore-masuk-indonesia.html", "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=200&h=150&fit=crop", "iPhone SG", "iPhone dari Singapore Masuk Indonesia", "Panduan lengkap iPhone SG di Indonesia."),
    ("biaya-daftar-imei-bea-cukai.html", "https://images.unsplash.com/photo-1436491865332-7a61a109db05?w=200&h=150&fit=crop", "Biaya IMEI", "Berapa Biaya Daftar IMEI di Bea Cukai?", "Breakdown biaya dan pajak di Bea Cukai 2026."),
    ("cek-status-imei-kemenperin.html", "https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?w=200&h=150&fit=crop", "Kemenperin", "Cara Cek Status IMEI di Kemenperin", "Step-by-step cek IMEI di website resmi."),
    ("facetime-iphone-tanpa-sinyal.html", "https://images.unsplash.com/photo-1522125670776-3c7abb882bc2?w=200&h=150&fit=crop", "FaceTime", "FaceTime Tanpa Sinyal: Bisa atau Tidak?", "Fitur Apple yang butuh dan nggak butuh sinyal."),
    ("panduan-aktivasi-sinyal-2026.html", "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=200&h=150&fit=crop", "Panduan 2026", "Panduan Lengkap Aktivasi Sinyal HP 2026", "Ultimate guide aktivasi sinyal lengkap."),
]

# Generate HTML cards
cards_html = ""
for href, img, alt, title, desc in new_articles:
    cards_html += f'<a href="{href}" class="article-card"><img src="{img}" loading="lazy" alt="{alt}"><div class="ac-text"><h3>{title}</h3><p>{desc}</p></div></a>\n'

# Read current index
idx_path = os.path.join(blog_dir, 'index.html')
with open(idx_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before </div> (closing article-list)
insert_point = content.find('</div>\n<footer')
if insert_point == -1:
    insert_point = content.find('</div>')
content = content[:insert_point] + cards_html + content[insert_point:]

with open(idx_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Added {len(new_articles)} article cards to blog index!")
