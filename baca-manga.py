import glob, re, os

tanya = """Di manakah Anda akan menampilkan manga ini?

1. Android
2. Windows

Jawaban (1/2): """
tanya = raw_input(tanya)

lokasi = ""
buatfile = []
filehtml = []
nyarigambar = []
enter = "\n"
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
    if tanya == "1":
    	x = re.sub(r"/", r".html", x)
    elif tanya == "2":
    	x = re.sub(r"\\", r".html", x)
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
    if tanya == "1":
    	x.write("<body onclick='document.body.webkitRequestFullScreen()' style='position: fixed; width: 100%; height: 100%; overflow: auto;'>")
    elif tanya == "2":
    	x.write("<body>")
    x.write(enter)
    x.write("<center>")
    x.write(enter)
    for q in nyarigambar[n]:
        x.write("<img src='"+q+"'/>")
        x.write(enter)
    x.write("</center>")
    x.write(enter)
    x.write("</body>")