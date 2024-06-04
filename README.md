# Atorrent

Script em python que oferece uma interface simples de linha de comando para baixar e transmitir torrents utilizando o Aria2c e Webtorrent. 

![marmoset-1684719555872](https://github.com/oanderoficial/atorrent/assets/32654298/ac151e51-fd0e-4f7d-8494-b11ff14b81cd)

<h2> Dependências </h2>

- aria2c - https://aria2.github.io/
- colorama -https://pypi.org/project/colorama/
- webtorrent -https://github.com/webtorrent/webtorrent

<strong> Atorrent funções </strong>

```python
def download_torrent(link):
    os.system(f"aria2c {link}")

def download_bittorrent(link):
    os.system(f"aria2c {link}")

def stream_torrent(link):
    os.system(f"webtorrent {link} 0 1")
```

```txt
1. Download Torrent (link magnético)
```

```txt
2. Download de BitTorrent
```

```txt
3. Streaming de Torrents
```
