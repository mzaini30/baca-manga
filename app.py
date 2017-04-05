import glob, re, os

lokasi = "/sdcard/Download/baca manga/"
buatfile = []
filehtml = []
nyarigambar = []
css = """<style>
img {
	display: none;
}
img[src*=jpg],
img[src*=png],
img[src*=gif]{
	display: block;
	width: 100%;
}
</style>"""
    
html = glob.glob(lokasi+"*.html")
for x in html:
    os.remove(x)

folder = glob.glob(lokasi+"*/")

for x in folder:
    x = re.sub(r""+lokasi, r"hdhsbbshs", x)
    x = re.sub(r"/", r".html", x)
    x = re.sub(r"hdhsbbshs", r""+lokasi, x)
    buatfile.append(x)

for x in buatfile:
    filehtml.append(open(x, "w"))
    
for n, x in enumerate(folder):
    nyarigambar.append(glob.glob(x+"*"))
    for j, q in enumerate(nyarigambar[n]):
        nyarigambar[n][j] = re.sub(r""+lokasi, r"", q)
    
for n, x in enumerate(filehtml):
    x.write(css)
    x.write("<body onclick='document.body.webkitRequestFullScreen()' style='position: fixed; width: 100%; height: 100%; overflow: auto;'>")
    x.write("<center>")
    for q in nyarigambar[n]:
        x.write("<img src='"+q+"'/>")
    x.write("</center>")
    x.write("</body>")