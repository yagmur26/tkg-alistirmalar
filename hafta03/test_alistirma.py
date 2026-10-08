# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama


def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0
    assert kargo_ucreti(500) == 0
    assert kargo_ucreti(400) == 50
    assert kargo_ucreti(0) == 50
    with pytest.raises(ValueError):
        kargo_ucreti(-500)


def test_muze_bileti():
    with pytest.raises(ValueError):
        bilet_fiyati(-6)
    assert bilet_fiyati(0) == 0
    assert bilet_fiyati(5) == 0
    assert bilet_fiyati(6) == 0
    assert bilet_fiyati(7) == 50
    assert bilet_fiyati(16) == 50
    assert bilet_fiyati(17) == 50
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(45) == 100
    assert bilet_fiyati(64) == 100
    assert bilet_fiyati(65) == 60
    assert bilet_fiyati(68) == 60

def test_ortalama_kontrol():
    with pytest.raises(ValueError):
        ortalama([])
    assert ortalama([90,80]) == 85
    assert ortalama([60,70,50]) == 60
    assert ortalama([30,25]) == 27.5
    assert ortalama([66.7, 32.8]) == 49.75 