from ex_services.regex_utils import RegexUtils

class ExMetadata():
	def __init__(self):
		self.title = None
		self.date = None
		self.rounds = None
		self.amrap = None
		self.rep_scheme = None
		self.rx_plus = None
		self.rx = None
		self.scaled = None
		self.male = None
		self.female = None
		self.scoring = None
		self.notes = None

	@property
	def has_many(self):
		return ['amrap']


	# i am trying to handle for a workout having many components.
	# that is, two different sets of rounds or AMRAPS
	# rounds and amraps are stored on the metadata level...
	# it is possible, perhaps that these need to simply move to the exercise level
	# they can be their own new type. so we have ex_data, ex_metadata, and ex_rounds
	# or at least they are checked differently!
	# i think the has_many will need to be deleted and this logic moved elsewhere 
	# need a different example. the 13 is too complex to begi nwith the "pause"/breaker of 1-mile ruck
	# though i think it is more akin to stages
	# so a workout has a stage property. it is none for most
	# but for some it's more than one
	# so ex_data is really ex_stage or ex_strucutre
	# suually it's 1:1, one ex_data is made up of one ex_structure
	# but some ex_data are made up of multiple ex_strcuture
	# in the case of the 13, stage 1 is amrap
	# stage 2 is ruck 1 mile, stage 3 is amrap
	def set(self, line):
		for attr, value in vars(self).items():
			if attr == "notes" or (value and attr not in self.has_many):					
				continue
			match = RegexUtils.try_match(line, attr)
			if match:
				if attr == 'amrap' and value:
					print("second match on amrap")
				setattr(self, attr, match)
				if attr != "title":
					return True
		return False