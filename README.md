DynIP
=====

This script provides a way to multiple update the IP of domain names from ClouDNS.
It works on Linux, Widows, OS X, Android. Unix based systems has native support for python,
on Windows you need to install [python](https://www.python.org/downloads/windows/)

## Downloading

Using git

    git clone https://github.com/physicalit/ClouDNS-dynIP.git

Archive [download](https://github.com/physicalit/ClouDNS-dynIP/archive/master.zip)

## Configuring

Configure with the links given by ClouDNS the [config.py](https://github.com/physicalit/ClouDNS-dynIP/blob/master/config.py#L11#L13) file. In `config.py` and `dynip-all.py` the links are mandatory to be ordered from `100` to `n`.
Configure the [dynip-all.py](https://github.com/physicalit/ClouDNS-dynIP/blob/master/dynip-all.py#L24) file  to have the same number as the number of the links, depends on with case scenario you will use the script

The file [dynip-all.py](https://github.com/physicalit/ClouDNS-dynIP/blob/master/dynip-all.py#L12#L25) it is used without
a config file, it's recommended for cron jobs.

## Different case uses

* Having just a config file and running it remotely:

      #getting the `config.py` file
      wget https://raw.githubusercontent.com/physicalit/ClouDNS-dynIP/master/config.py
      #After you have edited the config file run:
      curl -s https://raw.githubusercontent.com/physicalit/ClouDNS-dynIP/master/dynip.py | python
      #You need to run the above command in the same working directory as the config file

* Having all the files in the same working directory

    ./dynip.py
    or
    ./dynip-all.py

## Troubleshooting

`Error`

    Traceback (most recent call last):
    File "<stdin>", line 12, in <module>
    ImportError: No module named config

You don't have the config.py file in the working directory

## Acknowledgement

  [StackOverflow](https://stackoverflow.com/questions/33726806/python-syntaxerror-cant-assign-to-literal)

## Licensing

The project is licensed under the MIT license.
