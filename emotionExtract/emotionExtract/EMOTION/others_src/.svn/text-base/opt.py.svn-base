from optparse import OptionParser

def fun(filename,x,y):
    print filename
    print x+y

def fun_list(list):
    sum=0 
    for i in list:
	sum+=int(i)
    print sum 
    
def sel_ch(i):
    print "choice="+i

def foo_callback(option, opt, value, parser):
  setattr(parser.values, option.dest, value.split(','))

def main():
    usage ="usage:%prog [options] arg"
    parser = OptionParser(usage=usage)
    parser.add_option("-c",type="choice",choices=['1','2','3'],dest="step")
    parser.add_option("-f","--file",dest="filename",type="string")
    parser.add_option("-v","--verse",dest="verser",type="int")
    parser.add_option("-l","--list",type="string",dest="op_list",action="callback",callback=foo_callback)
    (options,args)=parser.parse_args()
    sel_ch(options.step)
    #fun(options.filename,int(options.verser,args[0]))
    
    
if __name__=="__main__":
    main()
    

