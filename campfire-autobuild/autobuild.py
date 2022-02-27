import os
import os.path
import re

contents_dir = "contents"
saving_dir = "reqs"
file_contents = os.listdir("contents")

function_template = """
def %s(%s):
    params = {
        %s
    }
    return campreq(params%s)%s"""

program_template = (
    "# This file was generated automatically\n"
    "# using other files prepared for generation\n\n"
    "from ._abcollect import *\n%s"
)

additional_types = {
    "timestamp": "get_timestamp",
    "deltastamp": "get_deltastamp",
}
resource_type = "resource"
resources_type = "resources"

def make_function(content):
    lines = content.split("\n")
    
    title = lines[0].split()
    request_name = title[1]
    function_name = title[2]
    
    returning_key = lines[-2][1:] if lines[-2].startswith(":") else None
    
    args_ier = (lines[1:-2] if returning_key else lines[1:-1])
    
    req_resources = []
    
    function_args = []
    request_args = []
    request_default_args = []
    for arg_ier in args_ier:
        if arg_ier.startswith("+"):
            arg_request, arg_default = arg_ier[1:].split()
            request_default_args.append((arg_request, arg_default))
        else:
            argsplit = arg_ier.split()
            if argsplit[0] == resource_type:
                arg_type, arg_name = argsplit
                arg_required = arg_name.startswith("*")
                if arg_required:
                    arg_name = arg_name[1:]
                req_resources.append((arg_name, "FLAG_RESOURCE_REQUIRED" if arg_required else "FLAG_RESOURCE_NO_REQUIRED"))
                function_args.append((arg_name,))
                continue
            elif argsplit[0] == resources_type:
                arg_type, arg_name = argsplit
                arg_required = arg_name.startswith("*")
                if arg_required:
                    arg_name = arg_name[1:]
                req_resources.append((arg_name, "FLAG_RESOURCE_REQUIRED_LIST" if arg_required else "FLAG_RESOURCE_LIST"))
                function_args.append((arg_name, "list"))
                continue
            else:
                arg_type, arg_request, arg_name = argsplit
            
            if arg_type in additional_types:
                function_args.append((arg_name,))
                request_args.append((arg_request, additional_types[arg_type], arg_name))
            else:
                function_args.append((arg_name, arg_type))
                request_args.append((arg_request, arg_type, arg_name))
    
    function_args = [ ("%s: %s" % arg) if len(arg) == 2 else arg[0] for arg in function_args ]
    request_params = (
        [ '"%s": %s(%s)' % param for param in request_args ] +
        [ '"%s": %s' % param for param in request_default_args ] +
        [ '"J_REQUEST_NAME": "%s"' % request_name ]
    )
    req_resources = [ "(%s, %s)" % res for res in req_resources ]
    returning_key = '["%s"]' % returning_key if returning_key else ""
    
    return function_template % (
        function_name,
        ", ".join(function_args),
        ",\n        ".join(request_params),
        (", FLAG_DATAOUTPUT, resources = (%s,)" % ", ".join(req_resources)) if len(req_resources) > 0 else "",
        returning_key
    )

for file in file_contents:
    with open(os.path.join(contents_dir, file), "r") as f:
        lines = f.read()
    
    # getting position of defeds (functions) in file
    def_pos = [ defed.start() for defed in re.finditer("#def", lines) ]
    fed_pos = [ defed.end() for defed in re.finditer("#fed", lines) ]
    defeds_pos = zip(def_pos, fed_pos)
    
    # getting defeds content
    defeds = [ lines[pos[0]:pos[1]] for pos in defeds_pos ]
    
    functions = [ make_function(defed) for defed in defeds ]
    program = program_template % "\n".join(functions)
    
    filename = os.path.join(saving_dir, file.split(".")[0] + ".py")
    with open(filename, "w") as f:
        f.write(program)
    
    print("Built " + filename)