# watchnext
script for recommending shows to watch 

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
- you can also install using requirements.txt
```

## Docker Usage

1. Build the Docker image:
```bash
docker build -t watch_next
```

```bash
docker run -it watch_next
```



