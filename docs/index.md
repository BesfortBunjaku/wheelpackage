# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

# Installation

To install MkDocs, run the following command from the command line:

``` shell
pip install mkdocs
```

# Creating a Project

Getting started is super easy. To create a new project, run the following command from the command line:


``` shell
mkdocs new my-project
cd my-project
```
or 

For current directory, if you are in the directory you want to create the project in, without additional directory
Run the following command from the command line:

``` shell
mkdocs new .        
```
or if you clone the repo, you can run the following command from the command line:

``` shell
pip install -r requirements.txt # install the requirements
```

Take a moment to review the initial project that has been created for you.

 
![Screenshot](images/initial-layout.png)

There's a single configuration file named `mkdocs.yml`, and a folder named `docs` that will contain your documentation source files (`docs` is the default value for the `docs_dir` configuration setting). Right now the `docs` folder just contains a single documentation page, named `index.md`.

MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it. Make sure you're in the same directory as the `mkdocs.yml` configuration file, and then start the server by running the `mkdocs serve` command:

``` shell
$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 160402 15:50:43 server:271] Serving on http://127.0.0.1:8000
[I 160402 15:50:43 handlers:58] Start watching changes
[I 160402 15:50:43 handlers:60] Start detecting changes
```

Open up http://127.0.0.1:8000/ in your browser, and you'll see the default home page being displayed:

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
