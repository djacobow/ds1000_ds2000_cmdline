# ds1000_ds2000_cmdline

Library and command-line utility for controlling the Rigol DS10xxZ and DS2xxx
series scopes.  It also facilitates screen capture and saving and restoring
complete state.

This is a work in progress, but the functions that are implemented so far
seem to work.

## dependencies and libraries

This library uses Python3, but other than the standard libraries, its has
no extra deps whatsoever, not SCPI or VISA or anything like that.

If your scope is on your home network, you should be able to simple provide
the IP address and be off to the races.

## Use

The library is called `dslib` and when you instantiate an object
for `RigolScope` type, you will have to provide a "personality" that
you want: right now, either `ds1k` or `ds2k` depending on the scope
you have.

There are two example command-line utilities:
`ds1_cmd.py` and `ds2_cmd.py` which do this for you, and so give
you options and behavior appropriate for that scope.

## Examples:

First, let me suggest running

```sh
./ds1_cmd.py --help
```

This will print out the many command options that are available to you.
I will be adding more over time.

You can make a screenshot with:

```sh
./ds1_cmd.py --capture foo.png
```

You can see set the vertical scale is for channel 3 to 10V/div by saying:

```sh
./ds1_cmd.py --ch-scale 3:10
```

You can read the horizontal timebase by:

```sh
./ds1_cmd.py --horiz-scale
```
The response will always be in the form of a json blob.

In general, if something is settable and queryable simple provide the argument
to set it, and leave it out to query it.

## TODO

Support for neither scope is complete.

For the DS10xxz, I need to add the commands for interaction with:
    * the logic analyzer
    * signal generator
    * waveform store and restore
    * pass fail stuff

For teh DS2xxxx, I need to do all the same stuff plus:
    * trigger modes for the decoders
    * measurement commands

Mostly this is just tedious work of going through the manual and adding
all the commands along with the validators for them.

I don't have scopes with LA's or the signal generators, however,
so I might not ever get around to supporting those commands, as I have
no way to test them.


