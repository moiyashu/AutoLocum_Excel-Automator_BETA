from Modules.configuration import configuration_functions as cf

class dictionary_functions:
	def pydict_to_jsondict(pydict: dict):
		import json
		return json.dumps(pydict)
	
	def write_to_json_file(_dict: dict):
		with open('./outputs/dict.json', 'w') as json_file:
			import json
			json.dump(_dict, json_file, indent=4, sort_keys=True)
		return True

	def rename_period(name: str):
		keys, values, replacements_dict = cf.get_values_to_replace()
		if name in keys:
			for key in keys:
				if name == key:
					replaced_name = replacements_dict[key]
		else:
			replaced_name = name
		return replaced_name
