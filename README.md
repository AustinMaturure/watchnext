# watchnext
script for recommending shows to watch 

## Prerequisites

- Python installed on your system
- SpaCy library (`spacy`) and the `en_core_web_md` language model.

You can install SpaCy and the model using the following commands:

```bash
pip install spacy

python -m spacy download en_core_web_md
```
## Usage

# Clone this repository to your local machine:
```bash
git clone https://github.com/AustinMaturure/watchnext
```

# Change your working directory to the cloned repository:
```bash
cd your-clone
```

# Install the required dependencies using the provided requirements.txt:
```bash
pip install -r requirements.txt
```

# Run the script:
```bash
python watch_next.py
```

## Usage

1. Ensure you have Python installed on your machine.
2. Install the required dependencies using the provided `requirements.txt` file.
3. Prepare a file (`movies.txt`) with movie titles and descriptions in the format `title:description`.
4. Run the script by providing a description, and it will recommend the most similar movie from the file.



```bash
python recommend_movie.py
```

## Dependencies
```bash
- spacy==3.1.3
- en-core-web-md==3.1.0

```

## Docker Usage

1. Build the Docker image:
```bash
docker build -t watch_next
```

```bash
docker run -it watch_next
```



