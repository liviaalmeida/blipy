# blipy

Blipy is a http requester made specifically to be used with [BLiP.ai](https://portal.blip.ai/) endpoints, with some requests right out of the box. Available endpoints can be found in [BLiP documentation](https://docs.blip.ai).

  - Instantiate requesters classes using the bot key
  - No need to request all resources manually
  - Magic

## Installation

Use `pip` to install the package.

```sh
$ pip install blipy
```

## Modules

Blipy offers the following modules.

| Modules | Description |
| ------ | ------ |
| Types | Contains base types for the package |
| Http | Requesters like Lime and Postmaster |
| Postmasters | Pre configured Postmasters |

### Types

Base types are used to have more control on operations over data

#### Data
```python
Data.new(method, uri, toId, resourceType = None, resource = None)
```
Used by Lime client to output a json body to every request

#### Date
```python
Date.new(year, month, day, hour = 0, minute = 0, second = 0)
```
Outputs a date in the format of a Lime QueryString

```python
Date.interval(startDate, endDate)
```
Outputs an object with keys `startDate` and `endDate`

#### Method
Dictionary to store the Lime methods used in requests

#### Response
Class of serializable data to store Lime responses

#### Resource
Class of serializable data to store Lime resources, which are part of responses

#### Serializable
Serializable receives a json and creates a new object such as its members are capitalized keys of that json. This enables storing any json as an object without using Python's reserved words such as `from` and `id`

#### URI
```python
new(baseuri, params = None)
```
Outputs an encoded URI to use with Lime, receiving `params` as a dictionary such as each param will be incorporated to the URI as `key=value`

### Http

HTTP clients used to make requests to Lime. They require a bot authorization key, which can be obtained [here](https://docs.blip.ai/#http). Just copy and paste.

#### Lime
Stardand Lime client to make any request

```python
lime = Lime(authorization)
```
Creates a new instance of lime using a bot authorization key

```python
lime.Get(uri, toId)
```
Returns a response to a get command to `uri` and receiver `toId`

```python
lime.Set(uri, toId, resourceType, resource)
```
Returns a response to a set command to `uri` and receiver `toId`, with `resource` of `resourceType`

```python
lime.Delete(uri, toId)
```
Returns a response to a delete command to `uri` and receiver `toId`

```python
lime.GetAll(uri, toId)
```
Returns a response with all resources to `uri` and receiver `toId`

```python
lime.SetAll(uri, toId, resourceType, resources)
```
Returns a response to a set of set commands to `uri` and receiver `toId`, with multiple `resources` of `resourceType`

```python
lime.DeleteAll(uri, toId, ids)
```
Returns a response to a set of delete commands to `uri` and receiver `toId`, with `ids` of resources to be deleted

#### Postmaster
A `Postmaster` is responsible for handling messages inside an application. The only difference between `Postmaster` and `Lime` is that the parameter `toId` gets subtracted, since the postmaster is a receiver of fixed identity of name `postmaster@APPLICATION_NAME.msging.net` where `APPLICATION_NAME` is the name of the corresponding application

```python
pm = Postmaster(authorization, name)
```
Creates a new postmaster client to send requests to postmaster@`name`.msging.net

### Postmasters
Pre configured postmaster with the most common operations available

#### AIPostmaster
Client to send messages to AI application

```python
aip = AIPostmaster(authorization)
```
Creates a new instance of AI Postmaster using a bot authorization key

#### AnalyticsPostmaster
Client to send messages to Analytics application

```python
anp = AnalyticsPostmaster(authorization)
```
Creates a new instance of Analytics Postmaster using a bot authorization key

### Todos
 - Write tests
 - Complete available postmasters
 - Add more postmasters
