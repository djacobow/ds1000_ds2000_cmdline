# ds1000z_cmdline

Library and command-line utility for controlling the Rigol DS10xxZ series scopes.
It also facilitates screen capture.

This is a work in progress, but the functions that are implemented so far
seem to work.

## dependencies and libraries

This library uses Python3, but other than the standard libraries, its has
no extra deps whatsoever, not SCPI or VISA or anything like that.

If you scope is on your home network, you should be able to simple provide
the IP address and be off to the races.

## Examples:

First, let me suggest running

```sh
./ds_cmd.py --help
```

This will print out the many command options that are available to you.
I will be adding more over time.

You can make a screenshot with:

```sh
./ds_cmd.py --capture foo.png
```

You can see set the vertical scale is for channel 3 to 10V/div by saying:

```sh
./ds_cmd.py --ch-scale 3:10
```

You can read the horizontal timebase by:

```sh
./ds_cmd.py --horiz-scale
```
The response will always be in the form of a json blob.

In general, if something is settable and queryable simple provide the argument
to set it, and leave it out to query it.

### Lots more to do...
