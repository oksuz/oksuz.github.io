---
layout: post
title: "Silex CORS Request Desteği"
date: 2017-01-09 14:56:00
tags: silex cors
comments: true
---

Silex micro framework ile cors isteklere cevap vermek için __after middleware__'ini kullanabiliriz.

```php
$app->after(function (\Symfony\Component\HttpFoundation\Request $request, \Symfony\Component\HttpFoundation\Response $response) {
   $response->headers->add(array(
       "Access-Control-Allow-Origin" => "*",
       "Access-Control-Allow-Methods" => "GET, POST, PUT, DELETE, OPTIONS, HEAD",
       "Access-Control-Request-Method" => "OPTIONS",
       "Access-Control-Allow-Headers" => "x-access-token, X-Requested-With, origin, Content-Type, Accept, Authorization"
   ));
});
```

böylelikle her istek için sunucudan dönen cevap header'ina yukarıdaki değerleri eklemiş olduk.

`Access-Control-Request-Method` headerinda belirttigimiz kontrol metoduna ilişkin olarak aşağıdaki gibi tüm option sorgularina cevap verecek birde route eklememiz gerekli.


```php
$app->options("{anything}", function () {
   return new \Symfony\Component\HttpFoundation\Response(null, 204);
})->assert("anything", ".*");
```

bu route'u ekledikten sonra silex uygulamamız CORS isteklere cevap verebilir hale gelecektir.
