from blipy.Types import Data, Method, Response
from requests import post

BLIP_COMMANDS = 'https://msging.net/commands'
BLIP_TAKE_MAX = 100

class HttpLime():
	def __init__(self, authorization):
		self.header = {
			'Authorization': f'Key {authorization}',
			'Content-Type': 'application/json'
		}

	def __sendCommand(self, method, uri, toId, resourceType = None, resource = None):
		data = Data.new(method, uri, toId, resourceType, resource)
		return Response(post(BLIP_COMMANDS, data=data, headers=self.header))

	def Get(self, uri, toId):
		return self.__sendCommand(Method.Get, uri, toId)

	def Set(self, uri, toId, resourceType, resource):
		return self.__sendCommand(Method.Set, uri, toId, resourceType, resource)

	def Delete(self, uri, toId):
		return self.__sendCommand(Method.Delete, uri, toId)

	def GetAll(self, uri, toId):
		updateUri = lambda uri, skip: f'{uri}?$skip={skip}&$take={BLIP_TAKE_MAX}'
		response = self.__sendCommand(Method.Get, updateUri(uri, 0), toId)
		resource = response.Resource
		skip = resource.Total
		getMore = resource.Total == BLIP_TAKE_MAX
		while getMore:
			moreResource = self.__sendCommand(Method.Get, updateUri(uri,skip), toId).Resource
			resource.addItems(moreResource)
			skip += moreResource.Total
			getMore = moreResource.Total == BLIP_TAKE_MAX
		return response

	def SetAll(self, uri, toId, resourceType, resources):
		completed = []
		for resource in resources:
			response = self.__sendCommand(Method.Set, uri, toId, resourceType, resource)
			if response.Success:
				contentId = response.Resource.Id
				completed.append(contentId)
			else:
				self.DeleteAll(uri, toId, completed)
				raise Exception('Error occured while trying to set all resource')
		return completed

	def DeleteAll(self, uri, toId, ids):
		uriWithId = lambda uri, uriId: f'{uri}/{uriId}'
		responses = []
		for uriId in ids:
			responses.append(self.__sendCommand(Method.Delete, uriWithId(uri,uriId), toId))
		return responses

class Postmaster(HttpLime):
	def __init__(self, authorization, name):
		super().__init__(authorization)
		self.identity = f'postmaster@{name}'

	def Get(self, uri):
		return super().Get(uri, self.identity)
	
	def Set(self, uri, resourceType, resource):
		return super().Set(uri, self.identity, resourceType, resource)

	def Delete(self, uri):
		return super().Delete(uri, self.identity)
	
	def GetAll(self, uri):
		return super().GetAll(uri, self.identity)
	
	def SetAll(self, uri, resourceType, resources):
		return super().SetAll(uri, self.identity, resourceType, resources)
	
	def DeleteAll(self, uri, ids):
		return super().DeleteAll(uri, self.identity, ids)