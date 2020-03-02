from .coin import *
from .cplex import  *
from .gurobi import *
from .glpk import *
from .choco import *
from .mipcl import *
from .mosek import *
from .scip import *
from .xpress import *
from .core import cplex_dll_path, coinMP_path, config_filename, Parser

# Default solver selection
if PULP_CBC_CMD().available():
    LpSolverDefault = PULP_CBC_CMD()
elif GLPK_CMD().available():
    LpSolverDefault = GLPK_CMD()
elif COIN_CMD().available():
    LpSolverDefault = COIN_CMD()
else:
    LpSolverDefault = None

def setConfigInformation(**keywords):
    """
    set the data in the configuration file
    at the moment will only edit things in [locations]
    the keyword value pairs come from the keywords dictionary
    """
    #TODO: extend if we ever add another section in the config file
    #read the old configuration
    config = Parser()
    config.read(config_filename)
    #set the new keys
    for (key,val) in keywords.items():
        config.set("locations",key,val)
    #write the new configuration
    fp = open(config_filename,"w")
    config.write(fp)
    fp.close()


def configSolvers():
    """
    Configure the path the the solvers on the command line

    Designed to configure the file locations of the solvers from the
    command line after installation
    """
    configlist = [(cplex_dll_path, "cplexpath", "CPLEX: "),
                  (coinMP_path, "coinmppath", "CoinMP dll (windows only): ")]
    print("Please type the full path including filename and extension \n" +
          "for each solver available")
    configdict = {}
    for (default, key, msg) in configlist:
        value = input(msg + "[" + str(default) + "]")
        if value:
            configdict[key] = value
    setConfigInformation(**configdict)