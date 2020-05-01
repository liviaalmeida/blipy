from Http import Postmaster
from Type import Resource

class AIPostmaster(Postmaster):
	def __init__(self, authorization):
		super().__init__(authorization, 'ai')
	
	def getIntent(self, intentId):
		return super().Get(f'/intentions/{intentId}?deep=true')

	def getIntents(self):
		return super().GetAll('/intentions')

	def getEntity(self, entityId):
		return super().Get(f'/entities/{entityId}')
