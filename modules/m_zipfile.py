### zipfile modülü hakkında

+ Zip dosyası olup olmadığını kontrol etmek

```python
import zipfile
filename = "file.zip"
zipfile.is_zipfile(filename)

```

+ Zip dosyasının parolasını açmak

```python
import zipfile
filename = "file.zip"
zip_file = zipfile.ZipFile(zipfilename)
zip_file.extractall(pwd=password)

```

