# ==========================================
#       PROFILE KELOMPOK 3
# ==========================================

print("=" * 50)
print("             PROFILE KELOMPOK 3")
print("=" * 50)

print("\nMata Pelajaran : Koding dan Kecerdasan Artifisial")
print("Kelas           : X TKJ 3")
print("Kelompok        : 3")

print("\n" + "-" * 50)
print("              ANGGOTA KELOMPOK")
print("-" * 50)

anggota = [
    ("Naufal Faiz Yonayulita", "32"),
    ("Dzikri Anandito Viali Shohada", "09"),
    ("Dhea Amelia Putri", "08"),
    ("Gilang Alfaro", "13"),
    ("Rui Alpian", "40"),
    ("Fardan Alfaqih", "11")
]

for i, (nama, absen) in enumerate(anggota, 1):
    print(f"{i}. {nama}")
    print(f"   No. Absen : {absen}")

print("\n" + "=" * 50)
print("              TENTANG KELOMPOK")
print("=" * 50)

print("""
Kelompok 3 merupakan kelompok siswa kelas X TKJ 3
yang bekerja sama dalam menyelesaikan tugas mata
pelajaran Koding dan Kecerdasan Artifisial.

Kami mengutamakan kerja sama, komunikasi, tanggung
jawab, dan saling menghargai dalam mengerjakan tugas.
""")

print("=" * 50)
print("        TERIMA KASIH TELAH MELIHAT")
print("              PROFILE KELOMPOK 3")
print("=" * 50)
