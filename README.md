# 🎬 Movie Recommender System (Content-Based Filtering)

This project is a content-based movie recommender system built using the TMDB 5000 Movie Dataset. It suggests movies that are **textually and thematically similar** based on genres, cast, keywords, and more.

> 🧪 Deployed here: [Click to Try the Live App](https://movierecommendersystem-your-link.streamlit.app/)

---

## 📌 Objective

To build a simple, explainable movie recommender system using **NLP techniques**, vectorization, and similarity metrics — without requiring any user ratings or behavior data.

---

## 📁 Dataset Used

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Source: [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🧠 How It Works (Step-by-Step Logic)

### 🔹 Step 1: Data Cleaning & Merging
- Merged movie and credits dataset on `title`.
- Extracted useful features: `overview`, `genres`, `keywords`, `cast`, and `crew`.
- Cleaned up list-like strings using `ast.literal_eval()` and removed extra spaces between names.

### 🔹 Step 2: Feature Engineering
- From crew, extracted only the **director** name.
- From cast, took the **top 3 actors**.
- Created a unified `tags` column by combining overview, keywords, genres, cast, and director for each movie.
- Converted all text to lowercase and removed spaces (`Tom Hanks → tomhanks`) to keep multi-word names together.

### 🔹 Step 3: Text Processing
- Applied **NLTK’s PorterStemmer** to normalize words (e.g., “loved” → “love”, “fighting” → “fight”).
- Removed stopwords to improve relevancy of content.

### 🔹 Step 4: Vectorization
- Used **CountVectorizer** from `sklearn` with `max_features=5000`.
- Converted the "tags" column into a **matrix of token counts** (Bag-of-Words).
- This matrix represents each movie as a vector in high-dimensional space.

### 🔹 Step 5: Similarity Calculation
- Used **Cosine Similarity** to compute similarity scores between all movie vectors.
- Stored the similarity matrix for future use.

### 🔹 Step 6: Model Persistence
- Saved preprocessed data and similarity matrix as:
  - `movies.pkl` — Contains cleaned movie DataFrame
  - `similarity.pkl` — Cosine similarity matrix
- Used `pickle` to serialize and load these in the deployed app.

---

## 💻 How to Run Locally

```bash
git clone https://github.com/bhumilad/movie_recommender_system.git
cd movie_recommender_system
pip install -r requirements.txt
streamlit run app.py
