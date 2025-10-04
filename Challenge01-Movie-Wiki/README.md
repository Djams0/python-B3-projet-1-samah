## Challenge 01 - Movie Wiki

![](https://images.unsplash.com/photo-1524712245354-2c4e5e7121c0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80)
Picture by [Karen Zhao](https://unsplash.com/photos/jLRIsfkWRGo)

## Objectives

Serialize and deserialize JSON files

## Guidelines

The file `input/wiki_movie_plots.json` contains a list of 32432 movies with various informations (release date, origin, director, etc.). It is a **big file** so don't try to display it entirely !

- Write a function `load_movie_list()` to deserialize the file.
- Write a function `classify()` to select movies by origin
- Write a function `save_movie_list()`to serialize our data in a JSON file.
- Put everything together in the `main()` function : the goal in the create a new JSON file in the `output` folder containing only British movies