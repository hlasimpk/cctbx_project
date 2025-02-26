from __future__ import absolute_import, division, print_function

import sys, os, traceback

def run():
  try:
    """
    utility function for passing keyword arguments more directly to hklview_frame.HKLViewFrame()
    """
    from crys3d.hklviewer import hklview_frame
    #import time; time.sleep(15) # enough for attaching debugger
    # dirty hack for parsing a file path with spaces of a browser if not using default
    args = sys.argv[1:]
    sargs = " ".join(args)
    qchar = "'"
    if sargs.find("'") > -1:
      quote1 = sargs.find(qchar)
      if sargs[ quote1 + 1:].find(qchar) < 0:
        raise Sorry("Missing quote in arguments")
      quote2 = sargs[ quote1 + 1:].find(qchar) + quote1 + 1
      space1 = sargs[ :quote1].rfind(" ")
      arg = sargs[space1 +1: quote2 +1]
      sargs2 = sargs.replace(arg,"")
      args = sargs2.split(" ")
      arg = arg.replace("'","")
      arg = arg.replace('"',"")
      arg = arg.replace('\\', '/') # webbrowser module wants browser paths having unix forward slashes
      args.append(arg)

    kwargs = dict(arg.split('=') for arg in args if '=' in arg)
    sysargs = []
    #check if any argument is a filename
    for arg in args:
      if '=' not in arg:
      # if so add it as a keyword argument
        if os.path.isfile(arg):
          kwargs['hklin'] = arg
        else:
          sysargs.append(arg)

    myHKLview = hklview_frame.HKLViewFrame(*sysargs, **kwargs)
    return myHKLview # only necessary for aiding debugging or line profiling
  except Exception as e:
    print( str(e) + "\n" + traceback.format_exc(limit=10))
    exit(-42)


if __name__ == '__main__':
  myHKLview = run()
