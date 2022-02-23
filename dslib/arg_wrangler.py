class ArgumentWrangler(object):
    def __init__(self, config, args):
        self._config = config
        self._inargs = args
        self._name = config.get('name','<unknown>')
        self.wrangle()

 
    def wrangle(self):
        argspecs = self._config.get('argspecs',())
        vcount = len(argspecs)
        acount = len(self._inargs)
    
        # if this command had one (optional) argument, and it is
        # not present, we just make sure the count is set to 0
        if acount == 1 and isinstance(self._inargs[0],str) and len(self._inargs[0]) == 0:
            acount = 0
    
        # one argument can be either really one argument, or it can
        # be a ':' concatenated series of arguments. Try to split on
        # colons, and if we get more than we started with, we know
        # that's what we had
        args = self._inargs
        if acount == 1:
            splitargs = self._inargs[0].split(':')
            splitcount = len(splitargs)
            if splitcount > 1:
               acount = splitcount
               if acount > vcount:
                   raise Exception(f'For function {self._name}: Provided argument {args[0]} splits into {acount} parts; too many for required {vcount} arguments')
               args = splitargs
    
        # now that we have (maybe) split the args, let's try to convert
        # them to the types the argspec expects
        converted_args = []
        for i in range(acount):
            converted_args.append(self.convert_to_type(argspecs[i].ttype(), args[i]))
        args = converted_args
    
        if acount < (vcount - 1):
            raise Exception(f'For function {self._name}: expects {vcount} (set) or {vcount-1} (get) arguments, only {acount} provided')
       
        # now make sure the arguments are actually acceptable to the command
        # argspec raises if not
        for i in range(acount):
            (ok, reason) = argspecs[i].validate(args[i])
            if not ok:
                raise Exception(f'For function {self._name} argument {i}: {reason}')
    
        self._adict = { f'a{i}' : args[i] for i in range(acount) }
        self._vcount = vcount
        self._acount = acount
        self._outargs = args

        cmd = self._config.get('cmd')
        func = self._config.get('func')
        if func is not None:
            pass
        elif cmd is not None:
            self._is_query = re.search(r'.*\?', cmd)
        else:
            self.expand_cmd_strs(self._config, vcount)
            self._is_query = vcount > 0 and acount == (vcount -1)
 

    def expand_cmd_strs(self, config, vcount=None):
        base_str = config.get('base_str')
        if config.get('q_str') is None:
            if base_str is None:
               raise Exception('Either q_str or base_str must be set')
            else:
               config['q_str'] = base_str + '?'

        if config.get('set_str') is None:
            if base_str is None:
               raise Exception('Either set_str or base_str must be set')
            else:
               if vcount is None:
                   config['set_str'] = base_str + ' {a0}'
               else:
                   config['set_str'] = base_str + f' {{a{vcount-1}}}'


    def convert_to_type(self, tt, r_raw):
        if tt=='float' or tt==float:
            return float(r_raw)
        elif tt=='int' or tt==int:
            return int(r_raw)
        return r_raw

    def convert_to_rtype(self, config, r_raw):
        return self.convert_to_type(config.get('rtype','str'), r_raw)

    def acount(self):
        return self._acount

    def vcount(self):        
        return self._vcount

    def isQuery(self):
        return self._is_query

    def argdict(self):
        return self._adict
