---
layout: post
title: "Jekyll ve Github Kullanarak Bloğunuzu Oluşturun"
date: 2015-01-11 19:06:00
tags: jekyll github blog
---

Merhabalar,

ne zamandır çok ama çok sade bir blog sistemi kullanmak istiyordum, wordpressden sıkılmıştım internette gezerken github bloglarını görüyor ve sadeliklerine hayran kalıyordum. Bu hafta sonu vakit buldum araştırmalara başladım ve `jekyll` ile karşılaştım. 

## Başlayalım
------------------------
__Jekyll Nedir ?__

`jekyll` sizlerin [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) ya da [Textile](http://redcloth.org/textile) formatında yazdğınız metinleri statik dosyalar (html) haline getiren, veritabanına ihtiyaç duymayan ruby dili ile yazılmış bir site oluşturucudur. 
Aynı zamanda [Github Pages](https://pages.github.com/) `jekyll'i` desteklemektedir. 


__Github Sayfanızı Oluşturmak__

Bunun için github hesabınıza giriş yaparak, sağ üst köşede bulunan `+` butonuna tıklayarak yeni bir repository oluşturmalısınız. Reponuzun adı `githubKullaniciAdiniz.github.io` formatına uygun olmalıdır. 
Örneğin benim github sayfam için repo adım `oksuz.github.io`'dur. Sonrasında ~30 dakika içinde `http://githubKullaniciAdiniz.github.io` adresinden sayfanıza ulaşabiliyor olacaksınız.


## Kurulum
------------------------

Belkide sevmeyeceğiniz tek kısım burası, `bir blog için bu kadar çok şey kurulur mu ?` dediğinizi duyar gibiyim ama markdown formatında yazma keyfine değiyor

```bash
sudo apt-get install git gem ruby ruby-dev nodejs
# ruby paketleri
sudo gem install jekyll jekyll-sitemap redcarpet
```

__Bloğumuzu Oluşturalım__

Aşağıdaki komutu uyguladıktan sonra `site_klasoru` altında bloğunuzun dosyaları oluşmuş olacak,

```bash
jekyll new site_klasoru
# daha sonra bu dizine geçelim
cd site_klasoru
# ardından sitemizi build edip yayina sokalım
jekyll build # olustur
jekyll serve # yayinla
```

Artık `127.0.0.1:4000` adresinden bloğunuzu önizleyebilirsiniz.

__* İpucu:__ `jekyll serve` komutunu verdikten sonra jekyll sizin için değişikleri takip edecek ve otomatik olarak build işlemini yapacaktır. Bu her yaptığınız değişiklikten sonra build ve serve işlemini tekrar yapmak zorunda değilsiniz demektir.

__Klasör Yapısı ve Dosyalar__

`_config.yml` dosyası sitemizin ayarlarının bulunduğu dosyadır. `_posts` klasörü markdown ya da textile formatında yazmış olduğumuz yazıları içermektedir. `_site` klasörü oluşturulan statik dosyaları barındırıyor. Aynı zamanda sitenizin ana dizine ekleyeceğiniz her bir `*.md` dosyası ya da `klasor/*.md` dosyası `_sites` altına eklenecektir. Örnek vermek gerekirse,

`site_klasoru/`__hakkimda.md__ --> siteniz.com/__hakkimda.html__
`site_klasoru/`__deneme/yazilar.md__ --> siteniz.com/__deneme/yazilar.html__

__* İpucu:__ `site_klasorune` eklediğiniz bir dosyanın oluşturma esnasında `_site` altına taşınmasını istemiyorsanız `_config.yml`'da `exclude` dizinine ekleyebilirsiniz;

```yaml
exclude: ["README.md", "log", "lib", "herhangibirsey.md"]

```

__* İpucu:__ Github bildiğim kadarıyla __redcarpet__ markdown parserini kullanıyor, eğer github markdown formatında yazmaya alışıksanız, `_config.yml`'da aşağıdaki değişkliği yapmalısınız:

```yaml
markdown:    redcarpet

redcarpet:
  extensions: ["no_intra_emphasis", "fenced_code_blocks", "autolink", "tables", "with_toc_data"]

```

## Bloğumuzu Yayına Sokalım
--------------------------

Yayına sokma işleminin github kısmı aslında basit, projenizi github.com'a push etmekten hiç farkı yok. Aşağıdaki komutları uygulayarak bloğumuzu canlıya alalım.

```bash
git init . # bu aşama sadece ilk committe yapılacak
git add .
git commit -m "ilk commit"
git remote add origin http://github.com/username/username.github.io.git # bu aşama sadece ilk committe yapılacak
git push origin master
```
#### Dikkat : 

`_site` `.saas_cache` gibi klasörleri `.gitignore` dosyanıza ekleyin ve commit etmeyiniz. Github `jekyll build` işlemini sizin için yapacaktır.


## Kendi Hostumuza Deploy
--------------------------
-- Eklenecek 


## Wordpess yazılarını jekyll'e import etmek
--------------------------
-- Eklenecek


__Dipnot:__

Bu makaleyi istediğiniz gibi çoğaltabilir, kopyalayabilir ve kaynak göstermeden kullanabilirsiniz. Makalenin MD haline [bu](https://github.com/oksuz/oksuz.github.io/blob/master/_posts/2015-01-11-jekyll-ve-github-kullarak-kendi-blogunuzu-olusturun.md) adresten ulaşabilirsiniz. Makalenin geliştirmesine katkıda bulunmak için __github__ üzerinden [oksuz/oksuz.github.io](https://github.com/oksuz/oksuz.github.io/) reposuna `pull request` gönderebilirsiniz.