# PYTEST DECARATOR
Dekoratörleri kısaca parametre olarak fonksiyon alan, geriye fonksiyon döndüren fonksiyonlar olarak tanımlayabiliriz. 
<pre>
@pytest.fixture:  Dekaratör testlerinizde kullanılmak üzere bir fixture oluştarmanızı sağlar. Test yazılımımız tarafından açıkça çağrıldıklarında test için veri ve çok çeşitli değer türleri sağlayabilirler. Oluşturulan sahte verileri birden çok testte kullanabilirsiniz.
@pytest.mark.parametrize: Aynı testin farklı parametrelerle çalışmasını sağlamaktadır.
@pytest.mark.skip: Testin geçilmesini sağlar
@pytest.mark.xfail: Bu dekoratör, bir testin başarısız olmasını beklediğinizi belirtir. Bu, hataların düzeltilmesi gereken testler üzerinde çalışırken yararlıdır.
@pytest.mark.timeout: Dekaratör , bir testin belirli bir sürede tamamlanmasını sağlar
@pytest.exit: Test sürecisinden çıkarır
</pre>
