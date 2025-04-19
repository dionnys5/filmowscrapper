# 🎬 Filmow Web Scraper

This is a **Web Scraper** built with **Scrapy** to extract movie data from [Filmow](https://filmow.com/filmes-todos/).  
It crawls multiple pages of the movie list, visits each individual movie page, and collects information such as title, original title, release year, cast, average rating, and number of votes.

---

## 📦 Technologies

- Python 3.10+
- Scrapy
- JSON (output format)

---

## 📄 Extracted Data

Each movie entry includes the following fields:

| Field              | Description                             |
|-------------------|-----------------------------------------|
| `titulo`          | Main title of the movie                 |
| `titulo_original` | Original title (if available)          |
| `ano`             | Release year                            |
| `elenco`          | List of cast members                    |
| `media_geral`     | Average user rating on Filmow           |
| `qtd_votos`       | Number of votes received                |

---

## 🚀 How to Run

### 1. Clone the project
```bash
git clone https://github.com/your-username/filmow-scraper.git
cd filmow-scraper
