#import module Enivornment and FileSystemLoader from jinja2 package
from jinja2 import Environment, FileSystemLoader

#import yaml file
import yaml

#Loads templates from the current folder and create template environment
ENV = Environment(loader=FileSystemLoader('.'))

#load template from this environment
template = ENV.get_template("template.j2")

#open the file, load the yaml configuration and print the rendering
with open("data.yml") as f:    
	interfaces = yaml.load(f)    
	print(template.render(interface_list=interfaces))
