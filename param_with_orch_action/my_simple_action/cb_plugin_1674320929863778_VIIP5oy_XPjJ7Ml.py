"""
This is a working sample CloudBolt plug-in for you to start with. The run method is required,
but you can change all the code within it. See the "CloudBolt Plug-ins" section of the docs for
more info and the CloudBolt forge for more examples:
https://github.com/CloudBoltSoftware/cloudbolt-forge/tree/master/actions/cloudbolt_plugins
"""
from common.methods import set_progress


param1="{{ param1 }}"
param2= {{ param2 }}


def run(job, *args, **kwargs):
    set_progress(f"param1: {param1}")
    set_progress(f"param2: {param2}")

    return "SUCCESS", "Sample output message", ""