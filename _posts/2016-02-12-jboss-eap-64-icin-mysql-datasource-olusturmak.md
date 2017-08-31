---
layout: post
title: "JBOSS EAP 6.4 İçin Mysql Datasource Setup"
date: 2016-02-12 15:06:00
tags: mysql-datasource jboss javaee
comments: true
---

Merhabalar, asagida vermis oldugum mysql datasource konfigurasyonu __JBoss EAP 6.4__ surumunde denenmistir.

### Dizin Yapisi
------------------------

Mysql database driver olarak [Connector/j'yi](https://dev.mysql.com/downloads/connector/j/) indiriniz.
zip icinden cikan `mysql-connector-java-VERSION-bin.jar` dosyasini ve olusturacaginiz `module.xml` dosyasini
$JBossHome/modules klasoru altina asagidaki gibi olusturunuz

```bash
com/
└── mysql
    └── main
        ├── module.xml
        └── mysql-connector-java-5.1.38-bin.jar
```

### Konfigurasyon Dosyalari
------------------------

Asagidaki eklemeleri ilgili konfigurasyon dosyalarina ekleyiniz


__$JBossHome/modules/com/mysql/main/module.xml__


```xml
<?xml version="1.0" encoding="UTF-8"?>
<module xmlns="urn:jboss:module:1.0" name="com.mysql">
    <resources>
        <resource-root path="mysql-connector-java-5.1.38-bin.jar" />
    </resources>
    <dependencies>
        <module name="javax.api" />
        <module name="javax.transaction.api" />
    </dependencies>
</module>
```

__$JBOSSHome/standalone/configuration/standalone.xml__

datasources/drivers node'u altina mysql driver'i ekleyiniz.


```xml
<drivers>
    <driver name="h2" module="com.h2database.h2">
        <xa-datasource-class>org.h2.jdbcx.JdbcDataSource</xa-datasource-class>
    </driver>

    <driver name="mysql" module="com.mysql"/>

</drivers>
```

ayrica datasources node'u altina yeni bir datasource olarak mysql datasource'unuzu ekleyiniz.


```xml
<datasource jndi-name="java:jboss/datasources/mysqlDS" pool-name="mysqlDS" enabled="true">
    <connection-url>jdbc:mysql://localhost:3306/DATABASE_NAME?useSSL=false</connection-url>
    <driver>mysql</driver>
    <pool>
        <min-pool-size>10</min-pool-size>
        <max-pool-size>100</max-pool-size>
        <prefill>true</prefill>
    </pool>
    <security>
        <user-name>root</user-name>
        <password>1</password>
    </security>
</datasource>
```

Datasource'unuza ait poolsize/ssl/database_name gibi alanlari kendize gore ozellestirmeyi unutmayiniz.

Kolay gelsin
