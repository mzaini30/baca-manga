import glob

lokasi = "/sdcard/Download/baca manga/"
folder = raw_input("Masukkan nama folder: ")

data = glob.glob(lokasi+folder+"/*.jpg")
hasil = open(lokasi+"output.html", "w")

hasil.write("<title>"+folder+"</title>")
hasil.write("<body onclick='document.body.webkitRequestFullScreen()' style='position: fixed; width: 100%; height: 100%; overflow: auto;'>")
hasil.write("<center>")
for x in data:
    hasil.write("<img src='"+x+"' width='100%'/>")
hasil.write("</center>")
hasil.write("</body>")