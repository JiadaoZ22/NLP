from NLP.Proj_MovieReview.stanford_parser_python_r22186.src.stanford_parser import parser as sp
parser = sp.Parser()
print (parser.parseToStanfordDependencies("this movie was utterly fantastic"))

# import jpype
#
# jpype.startJVM('/Library/Java/JavaVirtualMachines/jdk1.8.0_144.jdk')
# jpype.java.lang.System.out.println("hello world")
# jpype.shutdownJVM()

