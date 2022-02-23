import re
import itertools

def elaborateParser(parser, configs, parent):
    arg_handlers = {}

    def makeMetavars(argspecs):
        num_argspecs = len(argspecs)
        if num_argspecs == 0:
            return ''

        metametavars = []
        for argspec_idx in range(num_argspecs):
            argspec = argspecs[argspec_idx]
            final = argspec_idx == num_argspecs-1
            mmv = argspec.metametavar()
            # if there is only on arg and it is optional,
            # then argparse will add the brackets. But if there
            # is more than one, we need to add them because 
            # as far as argparse is concerned, they are all just
            # shmooshed together as one
            if final and num_argspecs != 1:
                mmv = ''.join(['[',mmv,']'])
            metametavars.append(mmv)

        metavar = None
        if len(metametavars):
            metavar = ':'.join(metametavars)

        return metavar

    def enumerate_arg_choices(argspecs):
        choices = None
        set_choices_list = [ v.choices() for v in argspecs ]
        set_choices = None
        if not None in set_choices_list:
            set_choices = [
                ':'.join(
                    [str(x) for x in t]
                ) for t in itertools.product(*set_choices_list)
            ]

        get_choices_list = set_choices_list
        get_choices = None
        if len(get_choices_list):
            get_choices_list.pop()
        if len(get_choices_list) and not None in get_choices_list:
            get_choices = [
                ':'.join(
                    [str(x) for x in t]
                ) for t in itertools.product(*get_choices_list)
            ]

        if get_choices is not None and set_choices is not None:
            choices = set_choices + get_choices
        return choices


    def make_parseargs_generic(parser_group, gconfig):
        for name, config in gconfig.get('commands',{}).items():
            aname = re.sub(r'_','-',name)
            argspecs = config.get('argspecs',())
            num_argspecs = len(argspecs)
            arg_handlers[name] = getattr(parent, name)

            flag_name = '--' + aname
            if num_argspecs == 0:
                parser_group.add_argument(
                    flag_name,
                    action='store_true',
                    help=config.get('help'),
                ) 

            else:
                choices = enumerate_arg_choices(argspecs)
                metavar = makeMetavars(argspecs)

                if num_argspecs == 1:
                    parser_group.add_argument(
                        flag_name,
                        nargs='?',
                        metavar=metavar,
                        const='',
                        type=str,
                        choices=choices,
                        help=config.get('help',None), 
                    )
                else:
                    parser_group.add_argument(
                        flag_name,
                        nargs=1,
                        metavar=metavar,
                        type=str,
                        choices=choices,
                        help=config.get('help',None), 
                    )


    parser_groups = {}

    for gname, gconfig in configs.items():
        if not gname in parser_groups:
            parser_group = parser.add_argument_group(
                title=gconfig.get('name',''),
                description=gconfig.get('description',None),
            )
            parser_groups[gname] = parser_group
        else: 
            parser_group = parser_groups[gname]

        make_parseargs_generic(parser_group, gconfig)

    return arg_handlers

