# Sadece Selenium İçin Yaptığım Mükkemmel Bir Proxy Çekme Ve Test Etme Programı
![enter image description here](https://i.pinimg.com/originals/ab/03/14/ab03149e8d88df694b0a91dc738a3890.gif)
Seleniumda eğer drivere proxy eklemek isterseniz eğer driver chrome ise argüman ekleyerek bu olayı çözebilirsiniz.

    options.add_argument("--proxy-server=192.168.1.1:1")
**Tabikide Bu Kadar Basit Değil !** Ekleyeceğiniz proxynin protokolüde önemlidir. genelde socks4 ve 5 selenium için iyi sonuç verir. **Normalde yaptığınız proxy rest(get) istekleri ile seleniumda tamamen doğru bir sonuç ALAMAZSINIZ.** 

Her neyse üstte anlatmaya çalıştığım şey her doğru denilen proxy seleniumda çalışmaz **ama bu scriptin doğru dediği çalıştırır**

    python scrap.py

Thread çalıştırma süresi ve max proxy delaylarını belirledikten sonra doğru olan proxyleri sizin için **çalışanproxyler.txt** olarak kaydeder. bu arada proxy'i normal şekide kaydetmez. seleniumda hazır kullanım için kaydeder sizede AŞŞŞIRI kolaylık sağlamış olur.
mesela :

> --proxy-server=socks4://1.10.189.84:44452  
--proxy-server=socks4://1.179.181.213:30500  
--proxy-server=socks4://1.10.188.93:37389

## Teşekküre Gerek Yok .d
