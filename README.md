# Wizard of Oz
====

Wizard of Oz with Animus SDK and Angular web app.

### App Structure
```
/
├── README.md
├── requirements.txt
├── main.py # Flask server (starts a server and launches the client app on a new web page)
├── animus_wrapper # Animus class wrapping Animus SDK functionality (one per user)
├── models # Path to classes and interfaces.
└── client # Angular project folder
    ├── dist (compiled version automatically goes here)
    ├── e2e (ignore)
    ├── karma.conf.js (ignore)
    ├── node_modules (all installed packages files)
    ├── package.json (list of installed packages)
    ├── protractor.conf.js (ignore)
    ├── README.md
    ├── src (source code is here)
    ├── tsconfig.json (ignore)
    └── tslint.json (ignore)
```

Requirements
----

Install the following requisites:

- Python3
- NodeJs
- Angular-cli


Installation
----

Install python dependencies:
```sh
pip3 install flask
cd path/to/animus
pip3 install .
```

Install angular dependencies:
```sh
$ cd client
$ npm install
```


Deployment
----

Build Angular app with Angular-cli after every change:

```sh
$ cd client
$ ng build --prod
```

Start Flask server:
```sh
python main.py
```
