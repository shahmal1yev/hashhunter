# Hash Hunter (hash-identifier)

Hash Hunter mövcud "hash" dəyərlərinin hansı alqoritmə məxsus olduğunu hərhansı bir onlayn alətə müraciət etmədən təyin
etmək üçün Python
proqramlaşdırma dilində yazılmış bir CLI (Command Line Interface) alətidir.

![img_1.png](../build/hashhunter/img.png)

### Kimlər üçündür?

- Bu alət, hash dəyərlərini analiz etmək istəyən kibertəhlükəsizlik mütəxəssisləri üçün idealdır.
- Hash siyahılarını tez və asan şəkildə analiz etmək istəyən hər kəs üçün uyğundur.
- Hash dəyərlərini daha yaxşı anlamaq və analiz etmək istəyən hər kəs bu alətdən faydala bilər.

### Yeni Xüsusiyyət: Hash List Paslanması

HashHunter'ın ən yeni xüsusiyyəti istifadəçilərə hash siyahısını birbaşa alətə paslamağa imkan verməsidir. Bu xüsusiyyət
hash
siyahılarını müvafiq fayllarda qruplaşdırır və onları hashcat ilə istifadə etmək üçün daha əlçatan edir.

### İstifadəsi

- Mövcud hash dəyərlərinin hansı alqoritmə məxsus olduğunu müəyyənləşdirin və yalnız ən uyğun hash alqoritm qruplarını
  yadda saxlayın:

```shell
hashhunter -H path/to/hash_list.txt --group
```

- Müəyyən edilmiş fayldan hash dəyərlərinin hansı alqoritmə məxsus olduğunu müəyyənləşdirin və həm ən mümkün, həm də ən
  az mümkün hash qruplarını yadda saxlayın:

```shell
hashhunter -H path/to/hash_list.txt --group -a
```

- Mövcud hash siyahısındakı dəyərlərin hansı alqoritmlərə məxsus olduqlarını müəyyənləşdirin və bütün çıxışı düz mətn
  olaraq bir faylda saxlayın:

```shell
hashhunter -H path/to/hash_list.txt -pO path/to/output.txt
```

### Parametrlər

| Parameter          | Shortcut | Description                                                                                                           |
|--------------------|----------|-----------------------------------------------------------------------------------------------------------------------|
|                    | **-H**   | Müəyyən etmək üçün heşləri ehtiva edən fayla gedən yol. Mütləq parametr.                                              |
| **--plain-output** | **-pO**  | Bütün çıxışı düz mətn olaraq bir faylda saxlamaq üçün istifadə olunur.                                                |
| **--group**        | **-g**   | Hash dəyərlərini qruplaşdırmaq və onları HashCat "attack mode"larına əsaslanan adlarla saxlamaq üçün istifadə olunur. |
| **--all**          | **-a**   | Ən çox və ən az mümkün hash qruplarını saxlamaq üçün istifadə olunur.                                                 |

### Dəstəklənən Alqoritmlər

- MD4
- MD5
- Half MD5
- NTLM
- SHA1
- SHA2-224
- SHA2-256
- SHA2-384
- SHA2-512
- SHA3-224
- SHA3-256
- SHA3-384
- SHA3-512
- Keccak-224
- Keccak-256
- Keccak-384
- Keccak-512
- RIPEMD160,
- BLAKE2b512
- GOST R 34.11-2012 (Streebog) 256-bit
- GOST R 34.11-2012 (Streebog) 512-bit
- Whirlpool

### Tərtibatçılar

- [@shahmal1yev](https://www.github.com/shahmal1yev)
- [@blackploit](https://www.github.com/blackploit)